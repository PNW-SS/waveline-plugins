# Claude setup

This repository provides a Waveline plugin for Claude Code. It connects to
`https://api.waveline.tel/mcp` and requires a Waveline account.

## Claude Code

Add the repository marketplace, then install Waveline:

```text
/plugin marketplace add PNW-SS/waveline-plugins
/plugin install waveline@waveline-plugins
```

Use `/mcp` to authenticate and follow [the setup guide](../plugins/waveline/SETUP.md).
The package contains the public client configuration needed for authentication;
no shared secret should be entered into the package.

The production connection must be available for sign-in to complete.
Installation alone is not confirmation that the account is connected.
Cowork compatibility has not been verified.

## Hosted Claude

A Claude Code plugin installation does not add a hosted Claude connector.
Where custom connectors are available, add `https://api.waveline.tel/mcp` in
Claude's connector settings. Use OAuth client ID `waveline-claude` in advanced
settings and leave the client secret empty. Then sign in to Waveline and
authorize the intended access.

For connection problems, contact
[support@pnwsoftwaresolutions.com](mailto:support@pnwsoftwaresolutions.com).
Do not send passwords, verification codes, or access tokens.

[Claude plugin documentation](https://code.claude.com/docs/en/plugins)
