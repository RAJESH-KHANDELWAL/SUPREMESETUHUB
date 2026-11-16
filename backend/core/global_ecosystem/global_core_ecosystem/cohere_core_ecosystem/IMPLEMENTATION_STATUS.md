# Cohere CORE Implementation Status

**Provider status:** `interface_only`  
**Live provider calls:** disabled

## Provider-level foundation

- Five capability identifiers are registered.
- Provider-level catalog, capability routing inventory, domain taxonomy and discovery/orchestration summary are present.
- Shared provider areas follow the `cohere_shared_*` naming convention.
- Shared request/result contracts, policy boundary, manager and PHP interoperability contract are present.

## Capability package structure

Each capability package now follows the Google product-Core folder convention:
- authentication
- capabilities
- docs
- events
- lifecycle
- models
- schemas
- security
- services
- tests

Each package also has a capability manifest, non-secret config, typed contracts and a service entry point.

## Implemented capability contracts

| Capability | Contract | Local validation |
|---|---|---|
| classify | `ClassifyRequest` | Non-empty text inputs |
| command | `CommandRequest` | Non-empty message |
| embed | `EmbedRequest` | Non-empty text inputs |
| rerank | `RerankRequest` | Non-empty query/documents and positive optional top-N |
| tokenize | `TokenizeRequest` | Non-empty text |

## Not implemented or not enabled

- Live Cohere API/SDK transport.
- Production authentication and secure credential injection.
- ENGINE execution, retries, timeouts, queues or scheduling.
- DATABASE persistence and STORAGE artifacts.
- Verified account entitlement, model availability or provider smoke tests.

## Known integration gap

The provider-level generic validation service has not yet been wired to dispatch each incoming request to its capability-specific service. Package-level validators and tests are present, but this routing must be implemented and verified before treating the provider facade as enforcing all capability-specific rules.

## Required next steps

1. Add provider-manager dispatch to the five capability service facades.
2. Run the capability unit tests and add provider-level routing tests.
3. Implement API and ENGINE adapters in their own layer folders.
4. Add secure runtime credential injection and tenant authorization.
5. Add integration tests, provider smoke tests, observability and deployment validation.
6. Change manifest readiness only when those checks pass.

Never commit provider secrets. Catalog registration is not proof of API access, model availability, entitlement or authorization.
