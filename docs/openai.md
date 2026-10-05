# OpenAI setup

This repository includes an OpenAI-compatible plugin manifest, shared production
MCP configuration, branding, and a repository marketplace. It does not itself
create a public directory listing.

The Waveline endpoint requires a host that supports MCP `2026-07-28` (MCP 2.0).

## Hosted ChatGPT

If Waveline appears in your plugin directory, install it and use the listing's
connection flow. Directory availability depends on your account and organization.
Keep that installed connection selected when verifying tools or monitoring.

For separately registered development connections, where your account and
organization allow custom MCP connections:

1. Add `https://api.waveline.tel/mcp` with OAuth in ChatGPT's plugin settings.
2. If prompted for a predefined client ID, use `waveline-chatgpt` and leave the
   client secret empty.
3. Follow the sign-in link to Waveline and sign in as yourself. The assistant
   uses your current Waveline permissions; role and inbox membership changes
   change its access. Read-only access is selected by default.
4. If you want to send messages, enable the optional write access on Waveline's
   consent screen and accept the displayed integration pricing during connection
   setup. The OAuth request must include `messages.write` for that option to appear; see below
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
requires consent to write access and integration pricing during connection setup,
and checks the signed-in user's permissions when sending. Each accepted external
recipient send costs US$0.01 before tax; existing messaging charges may also apply.
This pricing acceptance is not repeated as a warning or separate approval for
each send. Sending still requires authorization for the exact inbox, recipient,
and text; an existing explicit send instruction is sufficient. OAuth consent
alone does not authorize messages, and a draft request stays a draft.

For [internal Waveline messages](../plugins/waveline/README.md#send-an-internal-message),
the connection needs `inboxes.read`, `messages.read`, and `messages.write`, and
you must be an active member of the sending inbox. Recipient discovery does not
grant access to colleagues' histories. Internal messages incur no external SMS
integration fee and are distinct from phone-number texts.

The hosted connector's OAuth request configuration is managed outside this
repository. Its owner must update the requested scopes through the configuration
used to register that connector. Changing the desktop `waveline-codex` client
in `plugins/waveline/.mcp.codex.json` does not change requests from hosted ChatGPT's
`waveline-chatgpt` client.

After the requested scopes are corrected, reauthorize the connection and approve
the optional write access. Reconnecting with the same read-only request will not
add sending. Existing grants must not be silently expanded. Verify that the new
consent screen offers sending and that the resulting connection includes
`messages.write` before attempting a user-approved message.

### Monitor with ChatGPT or your dot

When your connected ChatGPT host and Waveline service support MCP Events, ask
the assistant to watch an inbox or contact and explain what it should do when
an update arrives. In a dot conversation, use the connected Waveline plugin
and name the intended account and inbox. The same Waveline permissions apply.
See [OpenAI's MCP Events guide](https://developers.openai.com/plugins/build/mcp-events)
and [dots and connected plugins](https://learn.chatgpt.com/docs/dots).

Use ordinary requests such as “Let me know when this customer replies” or
“Watch new call summaries in Sales for promised callbacks.” The packaged
monitoring skill recognizes requests about future updates and chooses the
matching event. It uses existing context for the account, inbox or customer,
response, and notification destination, asking only for missing details.
Historical questions and one-time lookups do not start monitoring. There is
no install-time subscription setup or onboarding hook.

For automatic saved replies, use the starter prompt or ask "Automatically save
reply suggestions in Waveline when customer texts arrive in Sales." The bundled
`auto-replies` skill checks `messages.read`, `inboxes.read`,
`messages.drafts.write`, and `events.subscribe`, then registers or reuses the
native incoming-text monitor with its durable draft-saving action. It saves
private suggestions for review without sending. An Events-capable host and
the current backend tools are required; missing capabilities are reported.

The assistant checks saved monitors before creating subscriptions, reuses a
compatible one, and preserves unrelated triggers. It reports **Enabled** only
after native subscription success. Partial failures and uncertain results remain
explicit, and saved state is checked before retries. Permission grants alone do
not confirm that any monitor is active.

Background monitoring is a separate permission, off by default. The connector's
OAuth request must include `events.subscribe` alongside the read permissions
for what you want to watch. To discover all nine call, message, and contact event
types, request:

```text
calls.read contacts.read inboxes.read messages.read events.subscribe
```

Reconnect and select **Allow background monitoring** on Waveline's consent
screen. If that option is missing, the connector owner needs to add the requested
scope. Existing grants are not expanded automatically. Optional sending and
inbox management permissions remain separate. Allowing monitoring does not
start a subscription; tell the assistant what to watch afterward.

For example:

- “Watch incoming texts in Dispatch and prepare replies for my review.”
- “Watch completed calls in Sales and tell me when a caller needs a callback.”
- “Watch new call summaries in my inbox and flag promised follow-up.”

Call and message subscriptions target one inbox at a time. A conversation filter
can narrow message events further. Contact events can target one contact.
Completed calls, recording readiness, transcript readiness and summary readiness
are separate events; a completed call may not have its summary yet.

Waveline sends updates for resources you can currently read. Changes to your
role or inbox access and disconnecting the connection stop future delivery
where access is lost. The assistant should confirm subscription success before
claiming it is watching. If events are unavailable on your connection, contact
support; installing this package alone cannot enable them.

Delivery can be delayed, duplicated or interrupted. Subscriptions require
refresh and do not replay missed events; ask the assistant to check Waveline
history if you need to catch up. To stop, ask it to unsubscribe from the named
monitor and confirm the result. Simply closing or pausing a chat does not stop
monitoring. Any message send still needs authorization for the exact inbox,
recipient, and text. Use an existing explicit send instruction without repeating
fee warnings or fee approval. Monitoring is suitable for notifications and
drafts; it does not grant automatic reply permission.

To [save reply suggestions in Waveline](../plugins/waveline/README.md#save-a-suggested-reply-for-review)
as customer texts arrive, explicitly name that destination in your request.
The OAuth request needs `messages.drafts.write` alongside `messages.read`,
`inboxes.read`, and `events.subscribe`; saving drafts does not need
`messages.write`. Approve the separate draft permission during connection setup.
The first version supports direct external text conversations whose latest
message is inbound. Saved suggestions are reviewed in Waveline; neither saving
nor choosing **Use reply** sends them or incurs an external SMS send fee.

### Verify an installed hosted plugin

After connecting through the directory listing, check that its plugin page shows
the expected tools and events. In a ChatGPT Work chat on the web, a desktop Work
chat with Cloud selected, or a dot, select that installed plugin and ask for one
specific monitor. Have the assistant confirm the selected account, event, and
target before relying on notifications. If tools, events, or the monitoring
consent option are missing, contact Waveline support with the plugin name.

Before replacing a connection, review existing monitors for the same event and
target. Reconnecting can create another monitor, so avoid overlapping tests.
After the replacement works, ask the original chat to stop only the superseded
monitor and confirm it has stopped.

## Repository marketplace

For clients supporting the repository's OpenAI-compatible format, register the
marketplace from a local checkout:

```sh
codex plugin marketplace add .
```

This registers the repository as a separate marketplace source. Existing
personal copies and installed packages do not synchronize with the checkout
automatically. Before applying an update, confirm the installed plugin's source,
update that source, then refresh or reinstall the plugin and start a new chat.

Select Waveline and complete authentication. The package supplies its public
desktop client settings; do not add tokens or shared secrets to its files.
Live desktop compatibility must be verified before relying on it.

For help, contact [Waveline support](mailto:support@pnwsoftwaresolutions.com).

[OpenAI plugin documentation](https://developers.openai.com/plugins/build/plugins)
