# Claude directory OAuth registration

The built-in `waveline-claude` public client supports a manually configured
hosted custom connection. That is not evidence of automatic directory setup.
Waveline currently provides neither dynamic registration nor client-ID metadata
documents. The chosen preparation path uses Anthropic-held client credentials,
which is a documented directory option requiring coordination with Anthropic.
[Authentication options](https://claude.com/docs/connectors/building/authentication).

## Prepared registration

| Field | Value |
| --- | --- |
| Client ID | `waveline-claude-directory` |
| Name | Claude directory |
| Redirect URI | `https://claude.ai/api/mcp/auth_callback` |
| Resource | `https://api.waveline.tel/mcp` |
| Token endpoint authentication | `client_secret_basic` |
| Scopes | `contacts.read contacts.write calls.read messages.read messages.write inboxes.read` |
| Secret | Private generated draft; never include it here |

The helper `waveline-cloudflare/scripts/prepare-mcp-directory-client.cjs`
generates a private file outside the workspace. It refuses overwriting an existing
file, prints no credentials, and does not change remote settings. A production
draft was generated during readiness preparation. The operator has its private
location in this task; the path is intentionally omitted from public documents.

Before deployment, merge the file's `worker_registration` object into the existing
production `INTEGRATIONS_OAUTH_CLIENTS` secret array. Preserve other registrations.
Only the secret hash belongs in this Worker configuration. Do not set
`platform: "claude"`, since that would replace the public custom-connection client
shown in Waveline's setup UI.

Coordinate the actual directory OAuth mode, callback, and authentication method
with Anthropic before entering `provider_credentials` into their private setup.
The documentation identifies `mcp-review@anthropic.com` for this flow. No message
has been sent and no credential has been shared with Anthropic by this task.

After registering both sides, test new-user consent, token exchange, refresh,
revocation, and the full tool scan. The credential draft has no user access until
registered and an individual user consents. This remains an external registration
gate, not something a plugin ZIP or application code push completes automatically.

Native Claude Code uses the separate [desktop client](native-desktop-oauth.md),
not Anthropic's hosted confidential credential.
