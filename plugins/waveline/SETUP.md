# Connect Waveline in Claude

Server: `https://api.waveline.tel/mcp`. Use only this environment's account and authorization.

1. Confirm the intended server is enabled and reachable. Package installation
   does not start or deploy the server.
2. For hosted Claude, add this URL as a custom connector. The current registered
   hosted client is `waveline-claude`, without a client secret, with callback
   `https://claude.ai/api/mcp/auth_callback`. Confirm deployed configuration first.
3. For Claude Code, native OAuth support is currently pending in the backend.
   Do not substitute the hosted client ID with a native callback. Once the backend
   supports the actual native client and redirect flow, use `/mcp` to authenticate.
   Verify Cowork's actual OAuth flow independently before claiming compatibility.
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
