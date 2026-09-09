# Waveline tool review and coverage

Inspected against `waveline-cloudflare/src/integrations/mcp/tools.ts` on
September 9, 2026. This is a review worksheet, not hosted test evidence.

All 20 tools have titles, bounded purpose-specific input schemas, all three
OpenAI annotations, and OAuth scopes in `_meta.securitySchemes`. They call
Waveline's own fixed endpoints. There is no arbitrary HTTP/SQL execution tool,
embedded UI, AI media generation, or money-transfer tool.

The scanner must authorize all six MCP scopes and approve write permissions to
discover all 20 tools. Read-only consent intentionally hides four write tools.
Do not publish a read-only snapshot with listing copy advertising sends/edits.

## Annotation justification

All tools are idempotent under the defined arguments. Write tools require a stable
operation key; changed arguments with the same key conflict instead of creating
a new operation.

| Tool | Read only | Destructive | Open world | Why / successful review evidence needed |
| --- | --- | --- | --- | --- |
| `get_connection` | true | false | false | Reads current grant and audience; verify Workspace and inbox cases. |
| `list_inboxes` | true | false | false | Lists permitted inboxes and sending numbers. |
| `find_contacts` | true | false | false | Searches visible records with literal filters; check ambiguity and pagination. |
| `get_contact` | true | false | false | Retrieves a selected visible contact. |
| `create_contact` | false | false | false | Adds a scoped contact without overwriting an existing record; replay creates one record. |
| `update_contact` | false | true | false | Replaces or clears selected existing fields; omitted fields stay unchanged. |
| `list_contact_notes` | true | false | false | Lists existing permitted notes. |
| `add_contact_note` | false | false | false | Appends a note without replacing existing notes; replay adds one note. |
| `list_calls` | true | false | false | Lists external call history within scope and time filters. |
| `get_call` | true | false | false | Retrieves permitted external interactions for one call. |
| `list_call_recordings` | true | false | false | Lists permitted existing recordings; excludes cross-inbox recordings when restricted. |
| `get_recording` | true | false | false | Reads recording metadata. |
| `get_recording_transcript` | true | false | false | Reads saved text without generating a transcript. |
| `get_recording_summary` | true | false | false | Reads a saved summary without new AI processing. |
| `get_recording_download` | true | false | false | Returns a temporary URL for an authorized existing recording. |
| `list_messages` | true | false | false | Lists permitted external messages; tests must cover mixed-inbox conversations. |
| `get_message` | true | false | false | Reads one permitted message and participants. |
| `list_message_attachments` | true | false | false | Lists existing attachments without uploading files. |
| `get_attachment_download` | true | false | false | Returns a temporary URL for an authorized existing attachment. |
| `send_message` | false | true | true | Enqueues an irreversible external send and one-cent recipient usage; requires explicit confirmation. |

The creation/append tools use `destructiveHint: false` because they do not
overwrite or delete data; they still advertise `readOnlyHint: false` and require
write scopes. Claude's checklist phrases write hints more broadly. Have the
reviewer assess these justifications against the actual behavior; do not claim
that annotations alone prove directory acceptance.

The current server returns `structuredContent` but does not declare tool
`outputSchema`. This is a metadata improvement opportunity, not an established
blanket submission rejection. Preserve the existing contract and validate the
actual scan before adding schemas that could reject legitimate result variants.

## Reviewer fixtures and execution

The owner supplied synthetic reviewer credentials for production, alpha, and
staging. Production application login succeeded with the supplied code and showed
populated call history. This does not establish OAuth consent, owner/admin access,
all required fixtures, or MCP behavior. Keep credentials and actual fixture IDs
in private reviewer fields.

Before running `reviewer-cases.json`, prepare or identify:

- A uniquely named visible contact and an out-of-scope contact; creation/update
  targets that can be changed without affecting other tests.
- An external call with a saved recording, transcript, and summary, plus an
  internal call and a recording involving another inbox.
- An external conversation with a message attachment, a mixed-inbox conversation,
  and message content containing an instruction-injection test string.
- A reviewer grant for one inbox and an owner/admin reviewer grant for Workspace
  tests. These must be independent of normal employee/customer data.
- One explicitly approved controlled send destination and test billing/delivery
  conditions. Reviewer login credentials are not authorization for a send.

Use fixed dates/timezones matching the fixtures for time-dependent prompts.
Map every tool above to at least one successful hosted invocation. For each
scenario, record surface, deployed revision, actual result, and pass/fail evidence
privately. Also test denied scopes, cross-inbox IDs, token expiry/revocation,
unchanged retries, changed-argument retry conflicts, and injected instructions.

[OpenAI MCP review](https://developers.openai.com/plugins/deploy/app-review),
[Claude review checklist](https://claude.com/docs/connectors/building/review-criteria).
