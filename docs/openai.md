# OpenAI setup

This repository includes an OpenAI-compatible plugin manifest, shared production
MCP configuration, branding, and a repository marketplace. It does not itself
create a public directory listing.

## Hosted ChatGPT

Where your account and organization allow custom MCP connections:

1. Add `https://api.waveline.tel/mcp` with OAuth in ChatGPT's plugin settings.
2. If prompted for a predefined client ID, use `waveline-chatgpt` and leave the
   client secret empty.
3. Follow the sign-in link to Waveline and sign in as yourself. The assistant
   uses your current Waveline permissions; role and inbox membership changes
   change its access. Read-only access is selected by default.
4. If you want to send messages, enable the optional write access on Waveline's
   consent screen and acknowledge the displayed messaging charge. The OAuth
   request must include `messages.write` for that option to appear; see below
   if the screen only lists read permissions.
5. Enable Waveline in a conversation and ask which connection and inboxes it
   can access. Sending also requires your normal Waveline permission to send
   from the chosen inbox. Messages sent through the assistant appear under
   your name.

### Connect multiple Waveline accounts

In Waveline's ChatGPT plugin settings, add another account and repeat the OAuth
sign-in for each Waveline account you want to use. If the consent page shows an
account you already connected, choose **Switch Waveline account**, sign in to
the other account, and then review its permissions. The pending connection
request returns to the consent page after sign-in.

ChatGPT identifies each connection using the signed-in Waveline account's
stable profile ID and displays its name, email, and workspace label when
available. Each tool call uses the selected connection's own permissions.
Specify the intended account or workspace when asking the assistant to read
or change Waveline data, especially before sending a message.

### Sending permission missing from consent

A request containing only `calls.read`, `contacts.read`, `inboxes.read`, and
`messages.read` authorizes read-only access. It does not offer message sending.
For those reads plus optional sending, the connector's OAuth authorization
request must include this space-separated `scope` value:

```text
calls.read contacts.read inboxes.read messages.read messages.write
```

This is a requested permission list, not an automatic grant. Waveline still
requires consent to write access and the messaging charge, and checks the signed-in
user's permissions when sending. Each accepted external recipient send costs
US$0.01 before tax; existing messaging charges may also apply.

The hosted connector's OAuth request configuration is managed outside this
repository. Its owner must update the requested scopes through the configuration
used to register that connector. Changing the desktop `waveline-codex` client
in `plugins/waveline/.mcp.json` does not change requests from hosted ChatGPT's
`waveline-chatgpt` client.

After the requested scopes are corrected, reauthorize the connection and approve
the optional write access. Reconnecting with the same read-only request will not
add sending. Existing grants must not be silently expanded. Verify that the new
consent screen offers sending and that the resulting connection includes
`messages.write` before attempting a user-approved message.

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
