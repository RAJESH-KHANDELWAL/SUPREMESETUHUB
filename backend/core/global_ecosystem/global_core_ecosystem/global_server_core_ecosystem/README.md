# GLOBAL SERVER CORE ECOSYSTEM

Provider-neutral CORE contracts and metadata registry for server resources across seven provider namespaces.

## Owns
- Stable server identity and resource metadata models.
- Provider-neutral lifecycle and deployment policy contracts.
- Typed provider, inventory and lifecycle protocols.
- Local validation and process-local identity registry.
- Seven-provider metadata catalog, readiness discovery and dependency mapping.
- CORE capability taxonomy and Normal → Basic → Standard → Premium → Professional → Enterprise → Supreme service-tier metadata.

## Does not own
- HTTP routes, authentication transport or request/response handling (API).
- Cloud SDK execution, provisioning, deployment or adapter orchestration (ENGINE).
- Durable SQL/NoSQL persistence, schemas or migrations (DATABASE).
- Object, file, backup or artifact storage (STORAGE).

## Providers
Abelohost, AWS, Cloudflare, DigitalOcean, Google Cloud, Microsoft Azure and ViceTemple are represented as provider metadata packages. Catalog presence does not imply an account, credentials, subscription, API entitlement, reachability or a live connection.

## Operational boundary
The registry is process-local metadata only. It does not prove that a server is reachable, that a provider operation succeeded, or that a remote lifecycle state is current. Remote operations remain disabled in CORE. Credentials must be held by an external secret manager and used only by separately authorized API/ENGINE components.
