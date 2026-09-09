# Environments

| Environment | Plugin | MCP URL |
| --- | --- | --- |
| Production | waveline | https://api.waveline.tel/mcp |
| Alpha | waveline-alpha | https://alpha-api.pnwsoftwaresolutions.com/mcp |
| Staging | waveline-staging | https://staging-api.pnwsoftwaresolutions.com/mcp |
| Local | waveline-local | https://maksim-workers.pnw-devs.com/mcp |

These URLs were read from the existing Worker configuration and local override.
No server was deployed, enabled, or probed during package setup. The checked-in
public environment configurations had integrations disabled when inspected;
actual deployed readiness must be confirmed separately.

Each package uses a fixed URL and distinct identity. To change an environment's
endpoint, update `environments.json` and its plugin's `.mcp.json`, then validate.
The local URL belongs to the existing developer tunnel; other developers must
configure their own reachable HTTPS endpoint. This repository starts no tunnel.

Register and authorize each environment separately. The backend issuer and OAuth
resource must match the selected origin and `/mcp` URL. Plugin names do not select
databases, billing mode, carrier credentials, or provider sandboxes.

Production is the public listing candidate. Alpha, Staging, and Local are private
testing packages. A public Git repository exposes every committed configuration,
even when only production archives are attached to a release. Review repository
visibility separately before publishing source.

No environment variables are needed for packaging. If future tests introduce
local-only settings, prefix them with `LOCAL_ONLY_`, keep them optional in required
variable validation, and exclude them from deployed environment files and secrets.
