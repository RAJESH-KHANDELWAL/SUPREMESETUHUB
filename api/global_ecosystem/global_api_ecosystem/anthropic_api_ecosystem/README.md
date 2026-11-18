# Anthropic API Ecosystem

Canonical provider catalog for Anthropic Claude and developer APIs in SUPREMESETUHUB.

## Scope
- Direct Claude Platform API at https://api.anthropic.com
- Messages, Message Batches, Models, Token Counting and Files APIs
- Admin/workspace management where organization permissions allow
- Managed Agents sessions/environments, tool use and supported model capabilities
- API-key and Workload Identity Federation setup paths

## Backend integration
The shared provider adapter is backend/integrations/providers/anthropic.py, registered as ANTHROPIC in backend/integrations/registry.py. It reports configuration readiness only. A configured key is not proof of a successful API request.

## Setup
1. Create an API key in the Claude Console: https://platform.claude.com/settings/keys
2. Store it as server-side ANTHROPIC_API_KEY in the deployment secret manager.
3. Never put the key in frontend code, public config, Git commits, logs, or client responses.
4. Restart/redeploy the backend and inspect provider readiness.
5. Add a separately approved live health operation before describing the provider as connected.

For production workloads, evaluate Anthropic Workload Identity Federation to use short-lived credentials instead of long-lived static keys.

## Child catalogs
See the child folders for API-family scopes and implementation boundaries. Their README files are planning scaffolds, not claims that each API is implemented.

## Security and status
- Do not accept or persist provider secrets in browser storage.
- Redact credentials from logs and error messages.
- Use least-privilege service-account keys, workspace scoping and rotation.
- Keep readiness (CONFIGURED_NOT_VERIFIED) distinct from live connectivity (CONNECTED).
- Do not call Anthropic APIs from browser code with a server API key.
