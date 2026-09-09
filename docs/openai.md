# OpenAI setup

The repository provides the `.codex-plugin/plugin.json` compatibility format,
remote MCP configuration, branding, and a repository marketplace. It does not
register a hosted ChatGPT connection or publish a public listing.

## Hosted ChatGPT

1. Release and enable the intended environment's MCP/OAuth server separately.
2. In ChatGPT developer mode, add the environment's MCP URL with OAuth. The
   current hosted public client is `waveline-chatgpt`, without a client secret;
   verify it against the deployed registration if the operator has overridden it.
3. Authorize the intended workspace or inbox, starting with read permissions.
4. Record the actual connection's technical `plugin_asdk_app...` identifier.
   Registration is pending, so no `.app.json` or invented IDs are included.
5. Once the real ID is available, add the platform's documented `.app.json`
   binding and update the OpenAI manifest and packaging validator/build allowlist
   together. Do not load the same tools twice through direct MCP and app wiring.
6. Execute the prepared hosted review scenarios with synthetic data.

Each environment needs its own connection and binding. Public submission uses
the production MCP URL and review materials; a developer connection ID alone is
not a public submission.

## Repository marketplace in Codex

This non-default marketplace needs explicit registration. From the repository
root, when you are ready to install:

```sh
codex plugin marketplace add .
```

Then select the desired Waveline environment in Codex. Do not infer successful
native OAuth from marketplace visibility. Native Codex registration/callback
compatibility must be verified independently of the hosted ChatGPT registration.

## References

- [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins)
- [OpenAI submission](https://developers.openai.com/plugins/deploy/submission)
- [OpenAI authentication](https://developers.openai.com/plugins/build/auth)
