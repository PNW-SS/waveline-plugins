# Connect Waveline Local in Claude

Server: `https://maksim-workers.pnw-devs.com/mcp`. Use only this environment's account and authorization.

1. Confirm the intended server is enabled and reachable. Package installation
   does not start or deploy the server.
2. For hosted Claude, add this URL as a custom connector. The current registered
   hosted client is `waveline-claude`, without a client secret, with callback
   `https://claude.ai/api/mcp/auth_callback`. Confirm deployed configuration first.
3. For Claude Code, this local package supplies client `waveline-local-desktop`
   and callback port 43821. The local Worker registers the exact callback
   `http://localhost:43821/callback`. Use `/mcp` to authenticate. Keep the local
   Worker and its tunnel running with an HTTPS origin at `https://127.0.0.1:3003`.
   Verify a completed login and tool call before claiming client compatibility;
   Cowork's actual OAuth flow also needs independent verification.
4. Sign in to Waveline and select Workspace or one permitted inbox, starting with
   read permissions. Read connection details and a known synthetic record.
5. Add write permission only when needed. Obtain explicit approval before sending
   the exact text to the specified external recipient from the selected inbox.
   Each accepted recipient send costs US$0.01 before tax plus any applicable
   existing messaging charges, accumulated on workspace billing.

If login fails, verify the environment's issuer/resource and client registration.
Never request a production secret in chat, hard-code a bearer token, disable
OAuth, or change permissions as a workaround. Setup instructions do not authorize
sending messages, accessing unrelated inboxes, or making backend configuration changes.
