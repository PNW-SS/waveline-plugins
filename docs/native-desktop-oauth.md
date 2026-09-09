# Native desktop OAuth

The production, alpha, and staging packages now use the pre-registered public
client `waveline-desktop`. Its registration is implemented in
`waveline-cloudflare/src/integrations/oauth/protocol.ts` and becomes available
when that Worker revision is deployed. It is not a hosted directory registration.

| Setting | Value |
| --- | --- |
| Client ID | `waveline-desktop` |
| Client authentication | `none`; no secret |
| Callback port | `43821` |
| OpenAI desktop callback | `http://127.0.0.1:43821/callback` |
| Claude Code callback | `http://localhost:43821/callback` |
| Resource | The selected environment's exact HTTPS `/mcp` URL |

The bundled `.mcp.json` supplies the client ID, callback URL, and port. Both
callbacks are exact registrations; other ports, paths, query strings, hosts,
resources, and webhook scopes are rejected. Hosted ChatGPT and Claude retain
their separate callbacks and cannot use the desktop callback. Generic operator
registrations still reject production loopback URLs. Consent displays the local
destination and warns that the connection returns to an app on the user's computer.

Local retains `waveline-local-desktop` and its existing development-only operator
registration. Do not copy that development registration into production.

## Verify after deployment

1. Install the intended environment's updated package through its marketplace.
2. Start authentication in the native client. Claude Code uses `/mcp`.
3. Confirm the callback matches one of the two exact values above and the resource
   matches the chosen environment. Complete Waveline sign-in and read-only consent.
4. In a fresh conversation, call `get_connection` and `list_inboxes`; verify the
   authorized audience. Test revocation and reconnect before advertising the surface.

Automated protocol tests passed for all three deployed environment origins;
actual desktop sign-in is still a post-deployment check. The fixed port must be
available on the user's computer. Native clients that do not honor the bundled
pre-registered-client settings need separate compatibility work.

[Claude Code pre-configured OAuth](https://code.claude.com/docs/en/mcp),
[OpenAI native MCP settings](https://learn.chatgpt.com/docs/extend/mcp?surface=cli).
