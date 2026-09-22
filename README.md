# Waveline plugins

Connect Waveline to your AI assistant to find contacts, review customer calls and
messages, and read saved transcripts and summaries. Optional permissions allow
contact updates, notes, and explicitly approved text messages.

When supported by the connected service, you can also ask for calls by saved
sentiment—for example, “Show calls with negative sentiment from last week.”
See the [sentiment search details](plugins/waveline/README.md#find-calls-by-sentiment).

This repository contains the production Waveline plugin for Claude Code and
OpenAI-compatible clients. The service endpoint is `https://api.waveline.tel/mcp`.
Directory availability and client compatibility depend on the released service;
this repository alone does not establish a published directory listing.

## Connect

- [Claude setup](docs/claude.md)
- [OpenAI setup](docs/openai.md)
- [Plugin permissions and usage](plugins/waveline/README.md)

Sign in to Waveline and approve the permissions you intend to share. The assistant
follows your current Waveline access. Each accepted external recipient send costs US$0.01 before tax;
existing messaging charges may also apply.

Support: [support@pnwsoftwaresolutions.com](mailto:support@pnwsoftwaresolutions.com).
See our [website](https://waveline.tel), [privacy policy](https://waveline.tel/privacy),
and [terms](https://waveline.tel/terms).

## Package development

Requires Python 3.11 or later, with no Python dependencies.

```sh
python scripts/package.py validate
python -m unittest discover -s tests -v
python scripts/package.py build
```

The build produces two production ZIPs in `dist/`, one per platform, with
SHA-256 checksums. Each ZIP contains only its platform manifest, platform-specific
MCP configuration, branding, README, bundled usage skills, and the Claude setup guide where applicable.
See [CI and releases](docs/ci.md).

Public package contributions must exclude operator runbooks, deployment
configuration, review-account information, and non-production connections.
