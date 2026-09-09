# Claude setup

There are two distribution paths: a remote MCP connector for hosted Claude, and
a plugin package for Cowork/Claude Code. Both refer to the same Waveline backend.
This repository includes actual Claude manifests and a marketplace, not just an
OpenAI package renamed for Claude.

## Hosted Claude custom connector

After the selected server is released and reachable, add its `/mcp` URL in
Claude's custom connector settings. If entering a pre-registered OAuth client,
the current hosted client is `waveline-claude`, with no shared secret and callback
`https://claude.ai/api/mcp/auth_callback`. Confirm the deployed registration
before use. Authorize the intended workspace or inbox and read scopes first.

Use distinct connector names and authorizations for each environment. Never
copy access tokens or secrets into a plugin file.

## Plugin package and marketplace

Each environment contains `.claude-plugin/plugin.json`, shared `.mcp.json`, and
`SETUP.md`. The repository catalog is `.claude-plugin/marketplace.json`.
To inspect a package with Claude Code before installing it:

```sh
claude plugin validate --strict plugins/waveline
claude plugin validate --strict .claude-plugin/marketplace.json
```

After native OAuth support is implemented and verified, from the repository root
you can register this local marketplace and install an environment:

```sh
claude plugin marketplace add .
claude plugin install waveline@waveline-plugins
```

Use `waveline-alpha`, `waveline-staging`, or `waveline-local` for private testing.
In a Claude Code session, `/mcp` manages the server's authentication. Cowork uses
its own plugin/connector setup UI; verify the actual OAuth flow on that surface.

## Native authentication prerequisite

The inspected backend only pre-registers hosted ChatGPT and Claude callbacks.
It has no dynamic client registration or Client ID Metadata Document support;
its client ID validation also excludes URL-form client IDs. Its production
redirect policy does not currently accept native loopback callbacks.

Consequently, installing this package is not enough to complete native Claude
Code login. The main backend implementation must support the chosen native
registration mechanism and exact callback flow with PKCE and resource binding.
For pre-registered native clients, Claude supports an `oauth.clientId` and
`oauth.callbackPort` configuration, but these must correspond to an actual
approved backend registration. No fabricated native client is included here.
Do not reuse `waveline-claude` with a native callback or bypass OAuth using a
hard-coded bearer token. These backend changes are outside this packaging repo.

## Public distribution

The Claude plugin directory and MCP Connectors Directory are separate submission
paths. Submit production to each desired directory after live testing. Claude's
plugin directory requires a public GitHub source link. Keep the source private
during development; before making it public, review all environment files and
choose the source-license terms. No license grant or public repository URL has
been invented in these manifests.

Reuse `plugins/waveline/submission/listing.md` and `reviewer-cases.json` for the
connector submission. For plugin submission, include the production plugin's
GitHub path, manifest, MCP reference, and setup instructions. After acceptance,
Anthropic may mirror source updates as described in its submission process;
increase plugin versions for releases and keep review on the source branch.

## References

- [Claude plugin format](https://code.claude.com/docs/en/plugins-reference)
- [Claude marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [Claude Code MCP and OAuth](https://code.claude.com/docs/en/mcp)
- [Hosted connector authentication](https://claude.com/docs/connectors/building/authentication)
- [Claude plugin submission](https://claude.com/docs/plugins/submit)
- [Claude connector submission](https://claude.com/docs/connectors/building/submission)
