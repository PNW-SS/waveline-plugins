# Waveline directory submission draft

Status: prepared locally; not submitted. Confirm all information against the
released service before making publisher attestations.

## Listing copy

**Name:** Waveline

**Publisher:** PNW Software Solutions LLC

**Support/review contact:** support@pnwsoftwaresolutions.com

**Initial availability:** United States only

**Setup documentation:** https://waveline.tel/support/docs/ai-integrations
(prepared locally; deploy and verify before submission).

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
The native `waveline-desktop` public registration and package settings are
prepared in source, using exact port 43821 loopback callbacks. A private Claude
directory credential draft also exists, but is not registered with either side.
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
- Public URLs checked September 9, 2026: [website](https://waveline.tel),
  [support](https://waveline.tel/support), [privacy](https://waveline.tel/privacy),
  and [terms](https://waveline.tel/terms), all HTTP 200. Confirm policy coverage
  for this integration and publish a plugin-specific setup guide.
- Marketing edits reconcile the footer to PNW Software Solutions LLC, add the
  setup guide and support address, and expand integration policy coverage.
  Review and deploy them with the integration release.
- Final OAuth registration for each target platform and callback verification.
- The owner supplied a synthetic reviewer account for production, alpha, and
  staging (not local). Production sign-in succeeded with the supplied OTP;
  verify tenant isolation, permissions, and reproducible fixture coverage before
  submission. Credentials belong only in private reviewer fields, not this
  listing, repository files, or public packages.
- A review environment that can exercise paid-send behavior without contacting
  real customers. Coordinate any requested hosted reviewer sign-in flow with the
  product's authentication implementation; do not weaken production login.
- Execute the included scenarios on the intended hosted surfaces and record results.
- Use the confirmed United States-only region. The supplied SVGs reuse the app's existing
  wave path, with system font fallback for the wordmark.
- New publisher-account readiness: OpenAI requires a default payment method and
  business verification before creating the draft. Claude Console Admin access
  is confirmed; its new-account form requires directory-terms acceptance.
- Publish the reviewed existing `PNW-SS/waveline-plugins` repository as requested;
  the license remains undecided. The repository is currently private.

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

See [public submission readiness](../../../docs/public-submission.md) for the
current portal links, verified checks, and remaining work. Production MCP and
OAuth discovery returned HTTP 404 on September 9, 2026, so this draft is not yet
ready to submit.
