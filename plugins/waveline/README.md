# Waveline

Connect to Waveline at `https://api.waveline.tel/mcp` to ask about calls, text
conversations and contacts, read saved transcripts and summaries, and review call
analytics. Optional write permissions let you update contacts and their custom
fields, add notes, manage inbox settings, and send approved text messages.

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

Before sending, approve the sending inbox, recipient, exact text, and charge.
Each accepted external recipient send costs US$0.01 before tax; existing
messaging charges may also apply. An accepted or queued result does not confirm
delivery. If a send times out, check its status before requesting another send.

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
