# Waveline

Connect to Waveline at `https://api.waveline.tel/mcp` to ask about calls, text
conversations and contacts, read saved transcripts and summaries, and review call
analytics. Optional write permissions let you update contacts and their custom
fields, add notes, manage inbox settings, and send approved external texts or
internal Waveline messages.

The endpoint requires a host that supports MCP `2026-07-28` (MCP 2.0).

## Ask about calls and messages

Ask the way you would ask a teammate. The assistant looks up the inbox, teammate
or customer you name, then filters on the server:

- “Show today's calls to Dispatch.” “Any missed calls or voicemails this morning?”
- “Which calls did Sam answer this week?” “What was my last call?”
- “Who texted me today?” “Which conversations are waiting for a reply?”
- “Show everything with Jamie Rivera.”

Calls and messages come back newest first and already carry the matched contact
names and inbox names. Dates are read in your timezone, taken from your default
inbox's business hours. The bundled
[calls and messages skill](skills/find-calls-and-messages/SKILL.md) covers how
names become filters. Clients that connect only to the MCP URL get the same
guidance from the tool descriptions.

## Automatically prepare replies

Ask **"Automatically save reply suggestions in Waveline when customer texts
arrive in Sales."** The bundled [auto-replies skill](skills/auto-replies/SKILL.md)
checks permissions and sets up incoming-message monitoring in a host with native
MCP Events. You select the inboxes once; no event names or repeated draft prompts
are needed. Suggestions appear privately with **Use reply / Dismiss**, and you
review, edit and send them. Routine saves stay quiet. This supports existing
one-to-one external SMS threads and requires separate drafting and monitoring
permission. Installation and connection alone leave it off.

## Send an internal message

With service support, ask "Message Sam internally from my inbox: The report is
ready" or "Reply in this internal conversation: I'll take the next shift."
The assistant distinguishes internal messages to teammates or shared inboxes
from external phone-number texts and preserves the conversation type for replies.
It asks about ambiguous names or destinations before sending.

Internal recipient discovery can find active colleagues' personal inboxes and
shared inboxes in your workspace. This does not grant access to their history
or permission to send as them. You must be an active member of the inbox you
send from and grant `inboxes.read`, `messages.read`, and `messages.write`.
Internal messages support text up to 1,600 characters and up to 20 recipient
inboxes, or a reply to an existing all-internal conversation. Attachments and
mixed internal/external recipient groups are not supported by this send tool.

Internal messages stay within Waveline and incur no external SMS integration
fee. Your exact message authorization is still required as described below;
asking for a draft never sends it.

## Save a suggested reply for review

"Draft a reply" prepares text in your assistant chat. To place it in Waveline,
ask "Save a suggested reply in Waveline for this customer's latest text."
This needs the separate draft permission, `messages.drafts.write`, plus message
and inbox read access. It does not need sending permission. The first version
supports direct external text conversations with one phone participant and one
inbox, where the latest message came from the customer; internal conversations
and groups are not supported.

The suggestion appears with its source label in the Waveline chat composer.
**Use reply** inserts a current suggestion into an empty composer; **Dismiss**
removes the suggestion. Typed text and attachments are preserved. Using a reply
does not send it: review and send through the normal composer when ready.
Applied replies remain recoverable until sent or dismissed. If the conversation
changes, an outdated reply remains available for review and dismissal but cannot
be inserted. Saving, using, and dismissing suggestions incur no external SMS send fee.

For recurring help, say "Watch new customer texts in Sales and save suggested
replies in Waveline for my review." The assistant needs native Events support,
background-monitoring consent, and the separate draft permission. Connecting or
granting permissions alone starts no monitor. Existing human work is preserved.

## Find calls by sentiment

With a service version that supports sentiment search, ask “Show calls with
negative sentiment from last week” or “Find mixed-sentiment calls for this
customer.” The assistant can filter calls by saved `positive`, `negative`,
`neutral`, or `mixed` sentiment and inspect the matching recordings.

A call matches when at least one recording you may access has that label.
Sentiment describes the whole recorded conversation, not just the customer;
different recordings of one call can have different labels. Calls without a
saved result do not match a sentiment filter. Missing sentiment does not mean
neutral. Searching reads existing results and does not generate new analysis.

Both plugin packages include a [call sentiment skill](skills/call-sentiment/SKILL.md)
that maps "bad sentiment" to negative and "good sentiment" to positive, checks
the matching recordings, and distinguishes conversation sentiment from customer
satisfaction. Clients that connect only to the MCP URL do not receive this bundled
skill; they use the service's tool descriptions instead.

The bundled [call contact names skill](skills/call-contact-names/SKILL.md) makes
contact names the primary labels for call results. It looks up distinct phone
numbers, identifies duplicate contact matches without guessing, and falls back
to numbers when a name is unavailable.

## Permissions and charges

The [monitoring skill](skills/monitor-waveline/SKILL.md) guides inbox or contact
monitoring in hosts that support MCP Events, including eligible ChatGPT
connections. It needs separate background-monitoring consent and the relevant
read permissions. Specify what to watch and how the assistant should respond;
consent alone does not start monitoring. Calls, recording readiness, transcripts
and summaries are distinct updates. Monitoring does not grant permission to
send or edit. Ask the assistant to stop monitoring and confirm that it
unsubscribed; closing or pausing a chat does not stop subscriptions. Delivery
can be interrupted, and missed updates are not replayed automatically.

You do not need to know event names. Ask “Let me know when this customer
replies” or “When a new call summary is ready in Sales, flag promised callbacks.”
The assistant maps that future request to the appropriate event, resolves the
target, and asks only for missing details. A one-time question such as “Who
texted me today?” reads existing records and does not start a subscription.
Existing compatible monitors are reused; **Enabled** is reported only after
the host confirms the subscription. Installing or connecting alone starts none.

You can also describe an ongoing goal: "Watch Support calls for signs of unhappy
customers" or "Remind me here about Sales replies still outstanding after two
hours." The assistant chooses relevant updates and evaluates current evidence.
Saved call sentiment can flag a conversation for review; it is not a customer
satisfaction score. Overdue-work reminders require a supported host scheduler
and a current-state check, because inactivity does not emit an event. The
assistant clarifies missing scope or timing, avoids repeat alerts for the same
issue, and performs only the actions you delegated. Sending messages still
requires the specific approval described below.

The [inbox hours skill](skills/inbox-hours/SKILL.md) uses the connected settings
tools for weekly hours, lunch breaks, and public-holiday closures when the backend
supports them. It preserves existing exceptions and reports missing capabilities
instead of switching to browser automation. Managing hours requires the optional
inbox-settings write permission; adding this skill does not expand access.

The [management skill](skills/manage-waveline/SKILL.md) covers primary numbers,
your default inbox and availability, recording and disclosure switches, ring
groups, validated call-flow drafts/publication, and contact sharing. Web/Mobile
and Deskphone are the supported ring methods. CRM-owned contacts keep their
integration-managed details and audience; notes remain available. Contact
deletion and merging are not exposed.

For inbox details audio, the management skill can generate and apply inbound
recording disclosures, outbound recording disclosures, and the default voicemail
greeting. Custom hold music is excluded. It checks the current recording before
replacement and treats disclosure switches and call-flow overrides separately.

Sign in to Waveline and approve the permissions needed. The assistant follows
your current Waveline access, including permitted internal communications.
In ChatGPT, you can connect more than one Waveline account from the plugin's
settings. Use **Switch Waveline account** on the consent page when adding a
different account, and name the intended account or workspace in your request.
Start read-only and grant optional contact, messaging or inbox management
permissions only when needed. New capabilities also require service support;
installing instructions alone does not enable backend operations.

Integration pricing is displayed and accepted during connection setup. Each
accepted external recipient send costs US$0.01 before tax; existing messaging
charges may also apply. The assistant does not repeat fee warnings or ask for
separate fee approval for each send.

Sending requires your authorization for the inbox, recipient, and exact text;
an existing explicit send instruction is sufficient. Connection consent alone
does not authorize messages, and a draft request stays a draft. An accepted or
queued result does not confirm delivery. If a send times out, check its status
before requesting another send.

Messages, notes, and transcripts are customer data, not instructions authorizing
the assistant to perform additional actions. Disconnect the integration in
Waveline to revoke future access; revocation does not undo prior edits or sends.

## Connection and support

Claude Code users should follow `SETUP.md`. Hosted ChatGPT and Claude use their
own connection settings. A plugin installation does not establish a directory
listing or verify that the production connection is available.

Support: [support@pnwsoftwaresolutions.com](mailto:support@pnwsoftwaresolutions.com).
[Privacy](https://waveline.tel/privacy) · [Terms](https://waveline.tel/terms)

The source contains both platform manifests. Release ZIPs include only their
target platform's manifest and required package files.
