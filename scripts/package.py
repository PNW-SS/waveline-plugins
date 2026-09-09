"""Offline validation and reproducible plugin packaging. Python 3.11+, no dependencies."""
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlsplit
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PLATFORMS = {"openai": ".codex-plugin", "claude": ".claude-plugin"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def local_file(folder, relative):
    require(isinstance(relative, str) and relative.startswith("./"), "Expected ./ relative path")
    path = folder / relative
    require(path.resolve().is_relative_to(folder.resolve()), f"Path escapes plugin: {relative}")
    require(path.is_file() and not path.is_symlink(), f"Missing or linked file: {path}")
    return path


def package_files(folder, platform):
    """Explicit allowlist prevents credentials and other host bindings entering archives."""
    paths = [folder / PLATFORMS[platform] / "plugin.json", folder / ".mcp.json", folder / "README.md"]
    paths += sorted((folder / "assets").glob("*.svg"))
    if platform == "claude":
        paths.append(folder / "SETUP.md")
    for path in paths:
        require(path.is_file() and not path.is_symlink(), f"Missing or linked package file: {path}")
        require(path.resolve().is_relative_to(folder.resolve()), f"Package path escapes: {path}")
    return sorted(paths)


def validate(root=ROOT, tag=None):
    version = (root / "VERSION").read_text().strip()
    require(re.fullmatch(r"\d+\.\d+\.\d+", version), "VERSION must be a stable x.y.z version")
    if tag is not None:
        require(tag == f"v{version}", "Release tag must match VERSION")
    environments = read_json(root / "environments.json")
    require(set(environments) == {"production", "alpha", "staging", "local"}, "Expected four environments")
    names, urls = [], []
    for environment, config in environments.items():
        name = "waveline" if environment == "production" else f"waveline-{environment}"
        require(config["plugin"] == name, f"Wrong plugin name for {environment}")
        url = urlsplit(config["url"])
        require(url.scheme == "https" and url.hostname and url.path == "/mcp"
                and not url.username and not url.password and not url.query and not url.fragment,
                f"Invalid MCP resource URL for {name}")
        names.append(name)
        urls.append(config["url"])
        folder = root / "plugins" / name
        require(read_json(folder / ".mcp.json") == {
            "mcpServers": {name: {"type": "http", "url": config["url"]}}
        }, f"MCP config must match environment and contain no credentials or extra servers: {name}")
        for platform, manifest_dir in PLATFORMS.items():
            manifest = read_json(folder / manifest_dir / "plugin.json")
            allowed = {"name", "version", "description", "author", "keywords", "mcpServers"}
            allowed |= {"interface"} if platform == "openai" else {"displayName"}
            require(set(manifest) <= allowed, f"Unexpected manifest fields in {platform}/{name}; review validator when adding capabilities")
            require(manifest["name"] == name and manifest["version"] == version, f"Name/version mismatch: {platform}/{name}")
            require(manifest["mcpServers"] == "./.mcp.json", "MCP reference must use shared config")
            require(manifest["description"].strip() and manifest["author"]["name"] == "Waveline", "Missing description/author")
            display = manifest["interface"]["displayName"] if platform == "openai" else manifest["displayName"]
            expected = "Waveline" if environment == "production" else f"Waveline {environment.title()}"
            require(display == expected, f"Wrong environment display name: {name}")
            if platform == "openai":
                for key in ("composerIcon", "logo", "logoDark"):
                    asset = local_file(folder, manifest["interface"][key])
                    require(asset.parent == folder / "assets" and asset.suffix == ".svg", "Assets must be bundled SVGs")
            package_files(folder, platform)
        require(not (folder / ".app.json").exists(), "Hosted app IDs require explicit registration and binding review")
    require(len(set(urls)) == 4, "Environments must have distinct URLs")
    require({p.name for p in (root / "plugins").iterdir()} == set(names), "Unexpected plugin folders")
    for platform, relative in [("openai", ".agents/plugins/marketplace.json"), ("claude", ".claude-plugin/marketplace.json")]:
        marketplace = read_json(root / relative)
        require(marketplace["name"] == "waveline-plugins", "Wrong marketplace name")
        entries = marketplace["plugins"]
        require([entry["name"] for entry in entries] == names, "Marketplace entries must match environment order")
        for entry in entries:
            expected = f"./plugins/{entry['name']}"
            if platform == "openai":
                require(entry["source"] == {"source": "local", "path": expected}, "Wrong marketplace source")
                require(entry["policy"] == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "Wrong install policy")
                require(entry["category"] == "Productivity", "Wrong category")
            else:
                require(entry["source"] == expected, "Wrong Claude marketplace source")
    return version, environments


def build(root=ROOT):
    version, environments = validate(root)
    output = root / "dist"
    output.mkdir(exist_ok=True)
    archives = []
    for config in environments.values():
        folder = root / "plugins" / config["plugin"]
        for platform in PLATFORMS:
            archive = output / f"{config['plugin']}-{platform}-{version}.zip"
            with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
                for path in package_files(folder, platform):
                    info = zipfile.ZipInfo(path.relative_to(folder).as_posix(), date_time=(2020, 1, 1, 0, 0, 0))
                    info.compress_type = zipfile.ZIP_DEFLATED
                    info.create_system = 3
                    info.external_attr = 0o100644 << 16
                    # Match Git's LF checkout so Windows/Linux text inputs package identically.
                    content = path.read_text(encoding="utf-8").replace("\r\n", "\n").encode("utf-8")
                    zf.writestr(info, content)
            archives.append(archive)
    def checksums(paths):
        return "".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n" for p in paths)
    (output / "SHA256SUMS.txt").write_text(checksums(archives), encoding="utf-8", newline="\n")
    production = [p for p in archives if p.name in {f"waveline-{platform}-{version}.zip" for platform in PLATFORMS}]
    (output / "PRODUCTION-SHA256SUMS.txt").write_text(checksums(production), encoding="utf-8", newline="\n")
    return archives


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["validate", "build"])
    parser.add_argument("--tag")
    args = parser.parse_args()
    try:
        validate(tag=args.tag)
        if args.command == "build":
            for archive in build():
                print(archive.relative_to(ROOT))
        else:
            print("All four environments and both marketplace formats validated.")
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(1, f"Validation failed: {error}\n")
