# HUGGING FACE SPACES APIS

Parent: GLOBAL HUGGING FACE API ECOSYSTEM

## Scope
Space search, metadata, runtime state, hardware settings, secrets and variables subject to permissions.

## Integration boundary
This family is an API architecture and capability catalog. Implement endpoints only where Hugging Face publishes a supported API and the account has the required permissions. Do not assume that every operation is available through a public REST endpoint.

## Runtime configuration
Use the backend secret `HF_TOKEN`. Never store access tokens in this folder, repository files, client-side code, logs or examples.

## Implementation status
Catalog / family boundary established. Live operations must be implemented and individually verified before marking this family connected.
