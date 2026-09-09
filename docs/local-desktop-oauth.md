# Local desktop OAuth

The installed personal Waveline Local plugin uses the desktop MCP runtime even
when selected from ChatGPT's desktop UI. Its Authenticate button starts native
OAuth; it does not need a hosted `plugin_asdk_app` binding for that flow.

The local package now supplies a pre-registered public client:

- Client ID: `waveline-local-desktop`
- OpenAI callback URL: `http://127.0.0.1:43821/callback`
- Callback listener port: `43821`
- Resource: `https://maksim-workers.pnw-devs.com/mcp`
- No client secret.

The development Worker's `.dev.vars` contains the matching registration. It also
allows Claude Code's exact `http://localhost:43821/callback` form. Both callbacks
remain exact matches; different ports and paths are rejected. This registration
is local-only and must not be copied to deployed environment secrets. Hosted
ChatGPT/Claude connections continue to use their separate existing client IDs.

Wrangler's development proxy rewrites same-host URL headers to the incoming
protocol. Therefore the Worker tunnel must connect to Wrangler over HTTPS:
`https://127.0.0.1:3003`. The existing cloudflared origin's `noTLSVerify: true`
accepts Wrangler's development certificate on this loopback connection; the
public MCP endpoint still uses verified HTTPS. Wrangler `dev.local_protocol` is
now HTTPS, and the local scheduler supports its self-signed loopback certificate
through a scoped dispatcher, without changing global TLS verification.

After restarting the local Worker/tunnel and refreshing the personal plugin,
open MCP servers and click Authenticate beside `waveline-local`. Complete the
Waveline login and consent in the browser. Use a new task to pick up its tools.
Full sign-in and tool access are verified only after the user completes consent.

Production, Alpha, and Staging now have a separate `waveline-desktop` registration
prepared for deployment; see [native desktop OAuth](native-desktop-oauth.md).
Live native verification, hosted developer connections, and public directory
submission remain separate from this local flow.

[OpenAI native/plugin OAuth configuration](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
