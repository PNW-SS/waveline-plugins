# Waveline plugins

Connect Waveline to your AI assistant to find contacts, review customer calls and
messages, and read saved transcripts and summaries. Optional permissions allow
contact updates, notes, and explicitly approved text messages.

This repository contains the production Waveline plugin for Claude Code and
OpenAI-compatible clients. The service endpoint is `https://api.waveline.tel/mcp`.
Directory availability and client compatibility depend on the released service;
this repository alone does not establish a published directory listing.

## Connect

- [Claude setup](docs/claude.md)
- [OpenAI setup](docs/openai.md)
- [Plugin permissions and usage](plugins/waveline/README.md)

Sign in to Waveline and choose the workspace or inbox and permissions you intend
to share. Each accepted external recipient send costs US$0.01 before tax;
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
SHA-256 checksums. Each ZIP contains only its platform manifest, shared MCP
configuration, branding, README, and the Claude setup guide where applicable.
See [CI and releases](docs/ci.md).

Public package contributions must exclude operator runbooks, deployment
configuration, review-account information, and non-production connections.
