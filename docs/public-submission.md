# Public submission for Waveline

Readiness checked September 9, 2026. Status: prepared locally; not submitted,
deployed, or published. An unsent Claude form was populated on the previous
account; after the owner switched publisher accounts, the new form requires its
own terms acceptance. Do not treat browser form contents as a saved submission.
Submit the production `waveline` integration. Alpha, Staging, and Local are
separate development environments, not additional public listings.

## Submission routes

| Destination | Entry point | Waveline submission |
| --- | --- | --- |
| OpenAI, shared by ChatGPT and Codex | [Plugin portal](https://platform.openai.com/plugins) | With MCP; Universal URL; `https://api.waveline.tel/mcp` |
| Claude Connectors Directory | [Remote MCP submission](https://claude.ai/admin-settings/directory/submissions/new) | Remote server; Streamable HTTP; the same production URL for every customer |
| Claude plugin directory | [Console submission](https://platform.claude.com/plugins/submit) or [Claude organization submission](https://claude.ai/admin-settings/directory/submissions/plugins/new) | Public GitHub source for the production plugin folder |

OpenAI needs a verified publisher and Apps Management write permission. Complete
the listing, OAuth configuration, domain challenge, tool scan, prompts, regions,
and review cases. Supply at least five positive and three negative cases. Reviewer
login must work without SMS, email confirmation, or MFA. Approval is followed by
a separate publish action. The public directory is shared by ChatGPT and Codex;
the local hosted connection ID is not a public submission.
[OpenAI submission guide](https://developers.openai.com/plugins/deploy/submission),
[package and directory model](https://developers.openai.com/plugins/build/plugins).

Claude remote submissions require a Team/Enterprise organization and directory
management access. Prepare public documentation, privacy URL, icon, support
contact, company details, and test-account instructions. Test every exposed tool
before completing the portal's acknowledgments. The remote connector route is
separate from plugin submission.
[Claude connector guide](https://claude.com/docs/connectors/building/submission).

Claude's plugin route requires public GitHub source. Console accepts submitters
with Developer, Admin, or Owner roles; it is an option for authors without a
Claude Team/Enterprise organization. Published source updates are automatically
mirrored and screened, so choose the submitted branch deliberately.
[Claude plugin guide](https://claude.com/docs/plugins/submit).

## Readiness evidence

Checked against the current working tree on `develop` (HEAD
`a277dabc357d595679f8a0fdd5723531d666cae7`, with pre-existing uncommitted changes).

| Check | Observed result |
| --- | --- |
| Package validator | Passed for all four environments and both marketplaces |
| Packaging regression suite | All 7 tests passed |
| Claude strict validator | Production, Alpha, Staging plugins and repository marketplace passed |
| OpenAI canonical plugin validator | Production package passed |
| Archive build | Eight platform/environment ZIPs and checksums generated in `dist/` |
| Production MCP | Both unauthenticated GET and JSON-RPC `initialize` POST returned HTTP 404, `Route not found` |
| Production protected-resource discovery | GET `https://api.waveline.tel/.well-known/oauth-protected-resource/mcp` returned HTTP 404 |
| Production authorization-server discovery | GET `https://api.waveline.tel/.well-known/oauth-authorization-server` returned HTTP 404 |
| Public website, privacy, terms, support | All four URLs below returned HTTP 200 |
| Hosted behavior | Prior local ChatGPT evidence covers only `get_connection` and `list_inboxes`; production review cases remain unexecuted |
| Reviewer account | Production sign-in succeeded using the owner-supplied synthetic phone/OTP, without receiving SMS. A populated call list was visible. Admin rights, isolation, and full fixture coverage remain unverified. Alpha/staging credentials are supplied but not tested; local uses separate credentials. Credentials are omitted from repository files. |
| Public plugin source | GitHub independently confirmed `PNW-SS/waveline-plugins` is private. Owner chose to make this existing repository public after review. |
| Source review | Pattern scan of 57 working source files and 45 historical blobs in one reachable commit found no targeted credentials or private-key patterns. Account-specific hosted verification records were removed from public documentation and preserved privately. This is a limited scan, not a security certification. |
| Backend checks | 93 integration tests, Worker typecheck, and local database rollback suites passed (30 MCP assertions, 120 MCP RPC assertions, 95 OAuth RPC assertions). |
| Consent UI checks | 11 targeted OAuth/integration tests, frontend typecheck, and production build passed. Build reported bundle-size and mixed-import warnings. |
| Marketing checks | Production build passed; new support article rendered in browser; challenge route checks passed for absent, exact, and malformed tokens. |
| New publisher accounts | Both portals use the owner-selected company admin account. OpenAI's selected organization is unverified and requires a default payment method before business verification. Claude Console shows Admin access and permits opening plugin submission. |

The production result is a deployment/routing blocker. The local Worker source
already routes these paths, and its disabled-integrations path returns 503, not
this 404. Check the deployed revision and hostname routing before assuming that
changing `INTEGRATIONS_ENABLED` alone fixes production.

## Materials already available

- [Listing copy](../plugins/waveline/submission/listing.md), including starter
  prompts, scopes, optional writes, and the US$0.01 per accepted external recipient
  send disclosure.
- [Review cases](../plugins/waveline/submission/reviewer-cases.json): five positive
  and four negative scenarios; these are instructions, not passing test evidence.
- [All-tool review checklist](../plugins/waveline/submission/tool-review.md):
  fixtures and checks for all 20 tools, including the four optional write tools.
- [Native desktop OAuth](native-desktop-oauth.md): fixed public-client callbacks
  prepared in production/alpha/staging packages and Worker source; deployment and
  actual client testing are still required.
- [Claude directory registration](claude-directory-registration.md): a private
  confidential-client draft was generated outside the workspace. Neither side
  has been registered, and no credential has been shared with Anthropic.
- Branding in `plugins/waveline/assets/` and production archives
  `dist/waveline-openai-0.1.0.zip` and `dist/waveline-claude-0.1.0.zip`.
  The OpenAI remote submission uses the server URL; the Claude public plugin
  submission uses public source. Building a ZIP does not publish either listing.

| Listing field | Verified public value |
| --- | --- |
| Product | Waveline |
| Website | https://waveline.tel |
| Support URL | https://waveline.tel/support |
| Privacy URL | https://waveline.tel/privacy |
| Terms URL | https://waveline.tel/terms |
| Owner-confirmed legal entity | PNW Software Solutions LLC |
| Owner-confirmed support/review contact | support@pnwsoftwaresolutions.com |
| Owner-confirmed initial listing region | United States only |
| Setup documentation, prepared locally | https://waveline.tel/support/docs/ai-integrations |

The marketing working tree now reconciles the footer to the confirmed entity,
fixes support links, adds the setup article, and expands privacy/terms coverage
for the actual optional integration data and sending charge. These are local
edits for owner review and deployment, not claims about the current live policy
or legal compliance. Existing privacy-inquiry contacts remain unchanged.

## Work remaining, in execution order

1. Complete OpenAI business verification for the intended publisher organization.
   The new account's selected organization is labeled Personal; this is a UI
   label, not proof of its legal status. The portal requires a valid default
   payment method before verification starts. Payment entry and business evidence
   remain with the owner. Confirm Apps Management write permission and a project
   with global data residency when draft creation becomes available.
2. Release the MCP/OAuth backend and consent UI through the application repos'
   existing flow. Follow `waveline-cloudflare/docs/integrations/MCP.md` and the
   database release review. Database edits remain declarative; the human runs the
   schema diff. Confirm bindings, origins, and client registrations before enabling
   integrations. The committed feature flag is disabled; a code push alone is
   insufficient. Recheck both discovery URLs and the unauthenticated OAuth challenge.
   Also deploy the marketing changes described in
   `waveline-marketing/docs/plugin-publication.md`; integration-repo deployment
   alone does not publish the help and policy updates.
3. Use the owner-provided synthetic reviewer account in production, alpha, and
   staging; it does not apply to local. Verify that the supplied phone/OTP login
   works for an independent reviewer without access to an SMS inbox, and check
   account isolation and fixture coverage for contacts, calls, transcripts, and
   messages. Enter credentials only in the submission portal's private reviewer
   fields when preparing the submission; keep them out of repository files and
   public listing copy. Local retains its separate development login.
4. Verify production OAuth on the intended hosted surfaces and any advertised
   native clients. Confirm exact callbacks; the local desktop registration is
   not proof of production native support. Directory registration may differ
   from the current hosted custom-connection clients.
   The fixed native client and loopback consent warning are prepared and tested
   locally. Follow the separate Claude directory registration guide to merge its
   secret hash into existing Worker configuration and coordinate provider setup.
5. Execute the existing scenarios and exercise the remaining exposed tools.
   Record environment, date, fixture IDs, actual results, and evidence privately.
   Send testing needs a specifically approved test recipient and controlled
   billing/delivery. No send was performed during this readiness check.
6. Complete the OpenAI and Claude connector drafts using the confirmed company,
   support contact, and US-only region. Claude Console plugin-form access is
   verified; separate Claude Team/Enterprise remote-directory access is not.
   The new account's plugin introduction requires directory-terms acceptance.
   For OpenAI, provision only the actual domain challenge issued by the portal.
   The marketing challenge route is prepared, with no token configured. Once the
   portal issues the token, set `OPENAI_APPS_CHALLENGE_TOKEN` on the marketing
   deployment and verify the exact response using `https://waveline.tel` as the
   challenge base URL. Local OAuth metadata does not advertise UserInfo; review workspace-domain
   restriction support against [OpenAI's authentication guidance](https://developers.openai.com/plugins/build/auth)
   rather than claiming that capability. This is not a blanket requirement for
   the initial listing.
7. For Claude plugin distribution, finish the chosen existing repository's public
   release review and choose its license (still unanswered). Its development
   domains and all tracked environments will become visible. Publish a stable
   release branch, preferably `main`, and submit `plugins/waveline`; verify that
   the portal's source URL selects that branch rather than auto-mirroring develop.
   Do not change repository visibility before the reviewed release is ready.
8. Review accurate final drafts and submit. Record real submission IDs and review
   feedback. Publish approved listings through the applicable portal and verify
   installation from a fresh customer account.

Remaining owner/external gates are OpenAI payment setup and business verification,
Claude directory-terms acceptance and remote-directory access, the source license,
and an approved send-test destination. Production deployment, provider OAuth
registration, the issued domain token, full live review evidence, and actual
repository publication remain release gates. No messages, submissions, paid
sends, account conversions, repository visibility changes, or production
deployments were performed by this readiness task.
