# Hosted ChatGPT local testing

This connects ChatGPT's hosted MCP client to the local Waveline Worker through
the existing HTTPS tunnel. The installed personal desktop plugin has a separate
OAuth client and credential store; its successful authentication does not verify
this flow. Keep the local Worker, web app, Supabase, and tunnel running.

## Connection values

| Field | Local development value |
| --- | --- |
| Name | Waveline Local Hosted |
| Description | Connect ChatGPT to the local Waveline workspace and inboxes. |
| MCP server URL / resource | `https://maksim-workers.pnw-devs.com/mcp` |
| Authentication | OAuth, predefined / manually supplied client |
| Client ID | `waveline-chatgpt` |
| Client secret | Leave empty; this is a PKCE public client |
| Authorization URL | `https://maksim-workers.pnw-devs.com/oauth/authorize` |
| Token URL | `https://maksim-workers.pnw-devs.com/oauth/token` |
| Exact registered callback | `https://chatgpt.com/connector_platform_oauth_redirect` |

The authorization and token URLs are normally discovered automatically. Never
enter the desktop client ID or localhost desktop callback in this connection.
The Waveline sign-in page for this development environment is served at
`http://localhost:5173`; it must be accessible from the browser completing consent.
Production uses its own public Waveline web app and MCP origin.

## Connect and verify

1. Sign into the intended ChatGPT account/workspace. If needed and available,
   enable Developer mode under Settings > Security and login.
2. Open [ChatGPT Plugins](https://chatgpt.com/plugins), select the plus button,
   and create a remote MCP connection using the values above. Choose a predefined
   OAuth client if the form offers registration methods. The server does not
   advertise dynamic client registration or client metadata document support.
3. If ChatGPT displays a different callback, record its exact value before
   changing the operator-owned registration. Do not use wildcard callbacks.
4. Complete Waveline sign-in, select the intended workspace or one inbox, and
   keep the default read-only consent. Verify the account and access before
   approving. This initial test does not require contact writes or paid sends.
5. Confirm ChatGPT discovers Waveline's tools. Start a fresh conversation, select
   only this hosted connection, and ask: "Show my connected Waveline workspace
   and the inboxes this connection can access. Do not change anything."
6. Check that `get_connection` and `list_inboxes` succeed and match the authorized
   audience. Check that the grant also appears in Waveline's integrations list.
7. Record the real hosted connection ID and test outcome. Only then add a hosted
   package binding if needed; no placeholder app ID belongs in a manifest.

If a scopes field is available, the initial read-only test can request
`contacts.read calls.read messages.read inboxes.read`. MCP discovery supports
these plus `contacts.write` and `messages.write`; Waveline consent determines
the granted subset. Webhook permissions are for the REST integration API and
must not be requested by this MCP client. A fresh MCP challenge explicitly lists
MCP permissions to avoid falling back to the broader authorization-server list.

## Verification recorded on September 9, 2026

- Public resource and authorization-server metadata returned HTTP 200.
- Unauthenticated MCP returned HTTP 401 with the correct metadata URL and six
  MCP scopes, excluding webhook scopes.
- The issuer matches the protected resource's authorization server, and metadata
  advertises S256 PKCE and authorization-response issuer identification.
- An authorization request using `waveline-chatgpt`, ChatGPT's exact callback,
  and the discovered scopes returned HTTP 302 to local Waveline sign-in. This
  created only an expiring authorization intent, not a grant or token.
- Created the hosted ChatGPT registration named `Waveline Local Hosted`. Its
  account-specific identifier is retained in the operator's private verification
  record. The form discovered
  the correct endpoints, resource, and stable callback. Its registration method
  is User-Defined OAuth Client, client ID `waveline-chatgpt`, token authentication
  `none`, with only the four read scopes selected.
- The user completed Waveline sign-in and consent from a regular browser.
  ChatGPT shows the connection as connected and lists 16 read-only actions.
- A fresh hosted ChatGPT conversation successfully called `get_connection` and
  `list_inboxes`. The tool outputs show an active Workspace connection named
  `ChatGPT (OAuth)`, the four read scopes, and the authorized inboxes. Local SQL
  independently confirmed the active OAuth grant.
- No contact, call, or message contents were requested by this smoke test, and
  neither tool performs a write or sends a message. The connection response does
  not provide the workspace display name. Hosted writes and the remaining read
  tools have not been exercised in this account.
- The operator's private smoke-test record contains both actual hosted tool calls
  and their results. Account-specific conversation links are not public setup
  instructions.

## Sign-in troubleshooting

The embedded browser stalled before opening Waveline OAuth. Completing sign-in
in the user's regular browser worked. That request initially failed because
ChatGPT included `ui_locales=en-US`; the authorization endpoint now accepts this
optional display-language hint without persisting it or changing consent, scopes,
PKCE, client or resource validation. All 29 MCP/OAuth tests and the Worker type
check passed after the fix.

Use the saved hosted connection in the operator's ChatGPT account
and select Waveline Local Hosted in a new ChatGPT conversation. It is a
separate hosted developer connection; the existing desktop package still uses
its direct MCP configuration and has not been rebound to this hosted app.

This verifies local hosted sign-in and the two named tools. It does not establish
other environments, all tool behavior, or public directory approval.

## Official references

- [Connect and test an MCP server in ChatGPT](https://developers.openai.com/plugins/deploy/connect-chatgpt)
- [OAuth discovery, predefined clients, and callbacks](https://developers.openai.com/plugins/build/auth)
- [Plugin packaging and shared directory](https://developers.openai.com/plugins/build/plugins)
