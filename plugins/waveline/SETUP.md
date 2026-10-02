# Connect Waveline in Claude Code

Server: `https://api.waveline.tel/mcp`.

Use a Claude Code runtime that supports MCP `2026-07-28` (MCP 2.0).

1. Install the Waveline plugin and use `/mcp` to start authentication.
2. Sign in to Waveline using your own account.
3. Review the requested permissions and start with read-only access. The
   assistant follows your signed-in account's current Waveline access. If you
   enable sending, accept the displayed integration pricing during connection
   setup: US$0.01 per accepted external recipient send before tax; existing
   messaging charges may also apply. Internal Waveline messages incur no
   external SMS integration fee.
4. Ask which Waveline connection and inboxes are available, and confirm that
   they match the access you intended.
5. Grant write permissions only when needed. Sending requires your authorization
   for the sending inbox, recipient, and exact text. An explicit send instruction
   is sufficient; fee approval and warnings are not repeated for each send.
   Connection consent alone does not authorize messages, and asking for a draft
   does not authorize sending it.

For teammate and shared-inbox messages, see [internal messaging](README.md#send-an-internal-message).
Internal sending requires active membership in the sending inbox, separate from
the directory permission used to find a recipient.

If authentication cannot complete, contact
[support@pnwsoftwaresolutions.com](mailto:support@pnwsoftwaresolutions.com).
Do not supply passwords, verification codes, or access tokens in chat or plugin
files. The package includes the public client settings it needs.

Installation does not start the Waveline service. Connection availability depends
on the released service and your account's access. This setup guide does not
authorize sending messages or accessing additional inboxes.
