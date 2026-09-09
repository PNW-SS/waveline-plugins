# Waveline directory submission draft

Status: prepared locally; not submitted. Confirm all information against the
released service before making publisher attestations.

## Listing copy

**Name:** Waveline

**Tagline:** Review customer calls, contacts, and messages.

**Description:** Connect Waveline to find contacts, review customer calls and text
messages, and read saved call transcripts and summaries. Select Workspace or one
permitted inbox and choose the permissions you want to grant. Optional actions
let you update contacts, add notes and send explicitly approved text messages.
Each accepted external recipient send costs US$0.01 before tax, added to your
workspace invoice; existing messaging charges may also apply.

**Primary category:** Productivity / business communications (use the nearest
available category in each submission portal).

**Starter prompts:**

- Review yesterday's missed customer calls.
- Find a contact and summarize their recent calls and messages.
- Draft a follow-up text for a customer. Ask before sending.

## Connection details

| Field | Value |
| --- | --- |
| Remote server | `https://api.waveline.tel/mcp` |
| Transport | Stateless Streamable HTTP, JSON responses |
| Authentication | Waveline OAuth authorization code with S256 PKCE |
| Authorization server | `https://api.waveline.tel` |
| Protected resource metadata | `https://api.waveline.tel/.well-known/oauth-protected-resource/mcp` |
| Permissions | `contacts.read`, `contacts.write`, `calls.read`, `messages.read`, `messages.write`, `inboxes.read` |
| Default user choice | Read-only; additional writes require opt-in |
| Current hosted ChatGPT client | `waveline-chatgpt`, public client, no secret |
| Current hosted Claude client | `waveline-claude`, public client, no secret |
| Embedded UI | None; tool-only connector |

The currently configured public clients serve custom hosted connections. Confirm
the chosen client registration with each directory. Anthropic-held credentials
are a supported directory option and require an operator-created client secret;
such a secret must be provisioned privately and never placed in this package.
Codex/Claude Code native client support must be independently verified before
listing those surfaces. The public OpenAI directory is shared with Codex, so
discuss or satisfy the intended surface compatibility during review.

## Data and actions

The server exposes 20 purpose-specific tools for connection/inbox information,
contact search and updates, notes, external calls and messages, saved recording
content, and authorized attachment/recording links. Each request uses the
connection's live permissions. Messages are attributed to the integration.

No automatic message campaign, internal-only activity export, group send, file
upload, arbitrary SQL/HTTP execution, call initiation, or transcript generation
is exposed by this MCP package. Returned data may include personal customer
information within the approved scope; users should connect only the intended
workspace or inbox. The published privacy policy must describe actual data
handling and retention. This draft does not invent retention or compliance claims.

## Required inputs before submission

- Production release with MCP/OAuth enabled and reachable over public HTTPS.
- A verified publisher identity consistent with Waveline's legal entity.
- Confirmed public website, support contact, privacy policy, terms and setup guide.
  These values were not provided and have intentionally not been fabricated.
- Final OAuth registration for each target platform and callback verification.
- A reviewer account containing synthetic data and safe reproducible fixtures.
  Never share production credentials or local development bypass codes.
- A review environment that can exercise paid-send behavior without contacting
  real customers. Coordinate any requested hosted reviewer sign-in flow with the
  product's authentication implementation; do not weaken production login.
- Execute the included scenarios on the intended hosted surfaces and record results.
- Approved branding and allowed regions; the supplied SVGs reuse the app's existing
  wave path, with system font fallback for the wordmark.

## Submission paths

**OpenAI:** Submit the server URL directly through the plugin submission portal,
along with publisher, policy, tool, prompt and test details. A local marketplace
entry or `plugin_asdk_app` ID does not constitute a public submission. Approval
and the subsequent publish action remain separate steps.

**Claude connector:** Submit the same remote MCP server through the Connectors
Directory process. Reuse the copy, assets and scenarios in Anthropic's form.

**Claude plugin:** The production folder also contains a Claude manifest and
setup guide. The plugin directory requires a public GitHub source link and a
separate submission. See the repository's `docs/claude.md` for native OAuth
prerequisites and the distinction between the two directories.

- [OpenAI submission](https://developers.openai.com/plugins/deploy/submission)
- [Claude connector submission](https://claude.com/docs/connectors/building/submission)
- [Claude plugin submission](https://claude.com/docs/plugins/submit)

No submission or legal attestation has been made by creating this draft.
