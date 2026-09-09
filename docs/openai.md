# OpenAI setup

This repository includes an OpenAI-compatible plugin manifest, shared production
MCP configuration, branding, and a repository marketplace. It does not itself
create a public directory listing.

## Hosted ChatGPT

Where your account and organization allow custom MCP connections:

1. Add `https://api.waveline.tel/mcp` with OAuth in ChatGPT's plugin settings.
2. If prompted for a predefined client ID, use `waveline-chatgpt` and leave the
   client secret empty.
3. Follow the sign-in link to Waveline. Select the workspace or inbox you intend
   to share and start with read permissions.
4. Enable Waveline in a conversation and ask which connection and inboxes it
   can access.

If Waveline appears in your provider's directory, use its listing's connection
flow instead. Availability depends on your provider's plan and organization settings.

## Repository marketplace

For clients supporting the repository's OpenAI-compatible format, register the
marketplace from a local checkout:

```sh
codex plugin marketplace add .
```

Select Waveline and complete authentication. The package supplies its public
desktop client settings; do not add tokens or shared secrets to its files.
Live desktop compatibility must be verified before relying on it.

For help, contact [Waveline support](mailto:support@pnwsoftwaresolutions.com).

[OpenAI plugin documentation](https://developers.openai.com/plugins/build/plugins)
