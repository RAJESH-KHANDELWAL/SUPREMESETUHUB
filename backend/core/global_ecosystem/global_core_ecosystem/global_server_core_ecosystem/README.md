# GLOBAL SERVER CORE ECOSYSTEM

CORE-owned provider-neutral server domain contracts.

## Owns
- Server identity and resource metadata models.
- Provider-neutral lifecycle and deployment policy contracts.
- Typed provider, inventory and lifecycle protocols.
- Local validation and identity metadata registry.
- CORE capability taxonomy for the seven provider namespaces.

## Does not own
- HTTP routes or request/response handling (API).
- Cloud SDK execution, provisioning or adapter orchestration (ENGINE).
- Durable SQL/NoSQL persistence (DATABASE).
- Object, file, backup or artifact storage (STORAGE).

The registry is process-local metadata only. It does not prove that a provider account exists, that a server is reachable, or that a cloud operation succeeded.
