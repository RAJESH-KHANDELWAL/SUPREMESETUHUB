# Cohere CORE Implementation Status

**Provider status:** `interface_only`  
**Live provider calls:** disabled

## Provider-level foundation

- Five capability identifiers are registered in the canonical capability catalog.
- Provider-level catalog, capability routing inventory, domain taxonomy and discovery/orchestration summary are present.
- Shared provider areas follow the `cohere_shared_*` naming convention.
- Shared request/result contracts, policy boundary, manager and PHP interoperability contract are present.
- The provider facade dispatches requests to the five capability-specific CORE validators and returns normalized validation results.

## Capability package structure

Each capability package follows the Google product-Core folder convention:
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

Provider-level routing tests cover successful dispatch, capability-specific invalid input, unknown capabilities, non-mapping inputs and invalid field types. These tests are committed but must still be executed in the repository CI/runtime before being marked verified.

## Not implemented or not enabled

- Live Cohere API/SDK transport.
- Production authentication and secure credential injection.
- ENGINE execution, retries, timeouts, queues or scheduling.
- DATABASE persistence and STORAGE artifacts.
- Verified account entitlement, model availability or provider smoke tests.

## Remaining integration work

1. Run provider and capability unit tests in CI and resolve any failures.
2. Implement API and ENGINE adapters in their own layer folders.
3. Add secure runtime credential injection and tenant authorization.
4. Add integration tests, provider smoke tests, observability and deployment validation.
5. Change manifest readiness only when those checks pass.

Never commit provider secrets. Catalog registration is not proof of API access, model availability, entitlement or authorization.
