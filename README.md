# Waveline plugins

One repository for Waveline's OpenAI and Claude plugin packages. Each environment
has one MCP configuration and two platform manifests. The MCP server, OAuth,
permissions, messaging, and billing remain in the Waveline application repositories.

Source: [PNW-SS/waveline-plugins](https://github.com/PNW-SS/waveline-plugins)
(private). The default branch is `develop`; changes progress through `staging`,
`alpha`, and `main`. Plugin installation, authentication, and directory submission
remain separate. Package validation does not establish live server or OAuth compatibility.

## Structure

```text
.agents/plugins/marketplace.json  OpenAI/Codex repository marketplace
.claude-plugin/marketplace.json  Claude repository marketplace
plugins/
  waveline/                     Production
  waveline-alpha/                Alpha
  waveline-staging/              Staging
  waveline-local/                Local through the existing HTTPS tunnel
    .codex-plugin/plugin.json    OpenAI compatibility manifest
    .claude-plugin/plugin.json   Claude manifest
    .mcp.json                   Shared remote server configuration
    assets/                     Bundled Waveline branding
    SETUP.md                    Claude connection setup guidance
environments.json               Environment names and expected MCP URLs
scripts/package.py              Offline validation and ZIP builds
tests/                          Packaging regression tests
docs/                           Setup, authentication, and release guidance
```

## Validate and build

Requires Python 3.11 or later; there are no Python dependencies.

```sh
python scripts/package.py validate
python -m unittest discover -s tests -v
python scripts/package.py build
```

Eight ZIP files and SHA-256 checksums are written to ignored `dist/`: one archive
per platform and environment. Each archive has its manifest and `.mcp.json` at the
expected relative paths, with no enclosing folder. Files are allowlisted, and
the other platform's manifest, submission materials, and local files are omitted.

Claude's own validator also runs in CI, pinned to the locally verified CLI version:

```sh
claude plugin validate --strict plugins/waveline
claude plugin validate --strict .claude-plugin/marketplace.json
```

## Getting connected

- [Environment URLs and isolation](docs/environments.md)
- [OpenAI registration and local marketplace](docs/openai.md)
- [Hosted ChatGPT local connection and verification](docs/hosted-chatgpt.md)
- [Claude plugin and hosted connector setup](docs/claude.md)
- [CI, GitHub setup, and releases](docs/ci.md)
- [Production listing draft](plugins/waveline/submission/listing.md)
- [Public submission process and readiness](docs/public-submission.md)
- [Unexecuted hosted review scenarios](plugins/waveline/submission/reviewer-cases.json)

The local hosted ChatGPT registration and a read-only connection/inbox smoke test
are verified; see the linked testing guide for results. Account-specific IDs are
retained privately. Other
environment registrations and public submission remain pending.
The local desktop package has a separate pre-registered OAuth client. The other
packages now declare `waveline-desktop`, whose backend registration is prepared
for deployment; see [native OAuth](docs/native-desktop-oauth.md).
Live native and hosted verification remain environment-specific.
Hosted client IDs cannot be reused with arbitrary native callback URLs. See the
setup guides before installing or advertising compatibility.

All environments authorize independently. An accepted external recipient send
adds US$0.01 before tax to workspace billing; existing messaging charges may also
apply. The backend owns charging and retry deduplication. Plugin configuration
does not create a payment transaction per message or sandbox a carrier send.

Original personal plugin copies and the existing personal marketplace remain
unchanged. Use this repository as the source for
future package edits; those old copies will not update automatically.
