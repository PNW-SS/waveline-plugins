# Grok setup

The same plugin folder serves two catalogs. Grok Bot installs plugins from the
Cursor Marketplace (`plugins/waveline/.cursor-plugin/plugin.json`, `mcp.json`);
Grok Build installs from the xAI plugin marketplace
(`plugins/waveline/.grok-plugin/plugin.json`, `.mcp.json`). Both configurations
contain only the production URL. This repository alone does not establish a
listing in either catalog.

## Grok Bot plugin

Once Waveline is listed:

1. Open **Plugins** in Grok Bot's sidebar, search for **Waveline** and click **Add**.
2. Follow the sign-in link to Waveline and sign in as yourself. The assistant uses
   your current Waveline permissions; role and inbox membership changes change its
   access. Read-only access is selected by default.
3. To send messages, enable the optional write access on Waveline's consent screen
   and acknowledge the displayed messaging charge.
4. Confirm **Waveline** shows under **Installed**. Every bot on the account can use it.

## Grok Build plugin

From the xAI marketplace, open `/marketplace` (or run `grok plugin install waveline --trust`),
or install straight from this repository at a released commit. The first Waveline tool
call opens the browser for sign-in.

## Custom connector (no plugin)

Grok Bot (**Settings → Plugins**, add a custom connector) and grok.com, the Grok mobile
apps and Grok-enabled Teslas (**Connectors → New Connector → Custom**) can add the
server directly:

1. Enter `https://api.waveline.tel/mcp` as the server URL. If asked for a client ID,
   use `waveline-grok` and leave the client secret empty.
2. Sign in to Waveline and review the requested access as above.

A custom connector provides Waveline's tools but not the plugin's skills.

## Network endpoints and credentials

The plugin connects only to `https://api.waveline.tel/mcp`. Authentication is
Waveline's OAuth flow in your browser: the client registers automatically, Waveline
answers with its public client and PKCE, and no client secret or API key is issued.
The plugin runs no local code and does not read local credentials, `.env` files or
unrelated files. Each accepted external recipient send costs US$0.01 before tax;
existing messaging charges may also apply.
