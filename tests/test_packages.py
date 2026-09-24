import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("package", ROOT / "scripts/package.py")
package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package)


class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "dist", "__pycache__"))

    def change(self, relative, mutate):
        path = self.root / relative
        data = json.loads(path.read_text())
        mutate(data)
        path.write_text(json.dumps(data))

    def test_wrong_environment_rejected(self):
        self.change("plugins/waveline/.mcp.codex.json", lambda d: d["mcpServers"]["waveline"].update(url="https://example.invalid/mcp"))
        with self.assertRaisesRegex(ValueError, "match environment"):
            package.validate(self.root)

    def test_nonproduction_config_rejected(self):
        self.change("environments.json", lambda d: d.update(test={"plugin": "waveline-test", "url": "https://example.invalid/mcp"}))
        with self.assertRaisesRegex(ValueError, "Only the production"):
            package.validate(self.root)

    def test_nonproduction_folder_rejected(self):
        (self.root / "plugins/waveline-test").mkdir()
        (self.root / "plugins/waveline-test/README.md").write_text("Not a public package")
        with self.assertRaisesRegex(ValueError, "Unexpected plugin folders"):
            package.validate(self.root)

    def test_embedded_token_rejected(self):
        self.change("plugins/waveline/.mcp.codex.json", lambda d: d["mcpServers"]["waveline"].update(headers={"Authorization": "Bearer synthetic-test"}))
        with self.assertRaisesRegex(ValueError, "credentials"):
            package.validate(self.root)

    def test_asset_escape_rejected(self):
        self.change("plugins/waveline/.codex-plugin/plugin.json", lambda d: d["interface"].update(logo="./../../VERSION"))
        with self.assertRaisesRegex(ValueError, "escapes"):
            package.validate(self.root)

    def test_release_tag_and_versions_rejected(self):
        with self.assertRaisesRegex(ValueError, "Release tag"):
            package.validate(self.root, tag="v9.9.9")
        self.change("plugins/waveline/.claude-plugin/plugin.json", lambda d: d.update(version="9.9.9"))
        with self.assertRaisesRegex(ValueError, "version mismatch"):
            package.validate(self.root)

    def test_missing_asset_rejected(self):
        (self.root / "plugins/waveline/assets/logo.svg").unlink()
        with self.assertRaisesRegex(ValueError, "Missing"):
            package.validate(self.root)

    def test_missing_sentiment_skill_rejected(self):
        (self.root / "plugins/waveline/skills/call-sentiment/SKILL.md").unlink()
        with self.assertRaisesRegex(ValueError, "Missing"):
            package.validate(self.root)

    def test_missing_contact_names_skill_rejected(self):
        (self.root / "plugins/waveline/skills/call-contact-names/SKILL.md").unlink()
        with self.assertRaisesRegex(ValueError, "Missing"):
            package.validate(self.root)

    def test_marketplace_escape_rejected(self):
        self.change(".claude-plugin/marketplace.json", lambda d: d["plugins"][0].update(source="../waveline"))
        with self.assertRaisesRegex(ValueError, "marketplace source"):
            package.validate(self.root)

    def test_missing_calls_and_messages_skill_rejected(self):
        (self.root / "plugins/waveline/skills/find-calls-and-messages/SKILL.md").unlink()
        with self.assertRaisesRegex(ValueError, "Missing"):
            package.validate(self.root)

    def test_missing_inbox_hours_skill_rejected(self):
        (self.root / "plugins/waveline/skills/inbox-hours/SKILL.md").unlink()
        with self.assertRaisesRegex(ValueError, "Missing"):
            package.validate(self.root)

    def test_grok_and_cursor_configs_carry_only_the_production_url(self):
        for mcp_file, mutate in ((mcp_file, mutate) for mcp_file in (".mcp.json", "mcp.json") for mutate in (lambda d: d["mcpServers"]["waveline"].update(url="https://example.invalid/mcp"),
                       lambda d: d["mcpServers"]["waveline"].update(oauth={"clientId": "waveline-codex"}),
                       lambda d: d["mcpServers"]["waveline"].update(headers={"Authorization": "Bearer synthetic-test"}))):
            with self.subTest(mcp_file=mcp_file):
                path = self.root / "plugins/waveline" / mcp_file
                original = path.read_text()
                self.change(f"plugins/waveline/{mcp_file}", mutate)
                with self.assertRaisesRegex(ValueError, "credentials"):
                    package.validate(self.root)
                path.write_text(original)

    def test_grok_and_cursor_manifests_rejected(self):
        grok, cursor = "plugins/waveline/.grok-plugin/plugin.json", "plugins/waveline/.cursor-plugin/plugin.json"
        for manifest, mutate, message in ((grok, lambda d: d.update(version="9.9.9"), "version mismatch"),
                                          (grok, lambda d: d.update(keywords=["waveline", "calls"]), "Waveline-scoped"),
                                          (grok, lambda d: d.update(hooks="./hooks.json"), "Unexpected manifest fields"),
                                          (grok, lambda d: d.update(mcpServers="./.mcp.codex.json"), "platform config"),
                                          (grok, lambda d: d.update(logo="../../VERSION"), "escapes"),
                                          (cursor, lambda d: d.update(version="9.9.9"), "version mismatch"),
                                          (cursor, lambda d: d.update(mcpServers="./.mcp.json"), "platform config"),
                                          (cursor, lambda d: d.update(skills="../other"), "bundled folder"),
                                          (cursor, lambda d: d.update(hooks="./hooks.json"), "Unexpected manifest fields"),
                                          (cursor, lambda d: d.update(displayName="Waveline Test"), "display name"),
                                          (".cursor-plugin/marketplace.json", lambda d: d["plugins"][0].update(source="../waveline"), "Cursor marketplace")):
            with self.subTest(manifest=manifest, message=message):
                original = (self.root / manifest).read_text()
                self.change(manifest, mutate)
                with self.assertRaisesRegex(ValueError, message):
                    package.validate(self.root)
                (self.root / manifest).write_text(original)

    def test_archives_deterministic_isolated_and_checksummed(self):
        # An accidentally present local credential file must never enter an archive.
        (self.root / "plugins/waveline/.env").write_text("SYNTHETIC_SECRET=do-not-package")
        (self.root / "plugins/waveline/skills/call-sentiment/.env").write_text("SYNTHETIC_SECRET=do-not-package")
        first = {p.name: p.read_bytes() for p in package.build(self.root)}
        second = {p.name: p.read_bytes() for p in package.build(self.root)}
        self.assertEqual(first, second)
        self.assertEqual(len(first), 2)
        for name, content in first.items():
            with zipfile.ZipFile(self.root / "dist" / name) as archive:
                self.assertIsNone(archive.testzip())
                files = archive.namelist()
                own_mcp = ".mcp.claude.json" if "-claude-" in name else ".mcp.codex.json"
                other_mcp = ".mcp.codex.json" if own_mcp == ".mcp.claude.json" else ".mcp.claude.json"
                self.assertIn(own_mcp, files)
                self.assertNotIn(other_mcp, files)
                self.assertIn("skills/call-sentiment/SKILL.md", files)
                self.assertIn("skills/call-contact-names/SKILL.md", files)
                self.assertIn("skills/inbox-hours/SKILL.md", files)
                self.assertIn("skills/manage-waveline/SKILL.md", files)
                self.assertIn("skills/find-calls-and-messages/SKILL.md", files)
                self.assertNotIn("skills/call-sentiment/.env", files)
                own = ".claude-plugin" if "-claude-" in name else ".codex-plugin"
                other = ".codex-plugin" if own == ".claude-plugin" else ".claude-plugin"
                self.assertIn(own + "/plugin.json", files)
                self.assertNotIn(other + "/plugin.json", files)
                self.assertNotIn(".env", files)
                # Grok and Cursor install from Git; their files never enter the Claude/Codex archives.
                for git_only in (".grok-plugin/plugin.json", ".cursor-plugin/plugin.json", ".mcp.json", "mcp.json"):
                    self.assertNotIn(git_only, files)
        for line in (self.root / "dist/SHA256SUMS.txt").read_text().splitlines():
            digest, name = line.split("  ")
            self.assertEqual(digest, hashlib.sha256(first[name]).hexdigest())
        release = (self.root / "dist/PRODUCTION-SHA256SUMS.txt").read_text().splitlines()
        self.assertEqual(len(release), 2)
        self.assertTrue(all("waveline-openai-" in line or "waveline-claude-" in line for line in release))


if __name__ == "__main__":
    unittest.main()
