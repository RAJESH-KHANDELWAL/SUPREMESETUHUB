# Cohere CORE Implementation Status

Provider status: interface_only  
Live provider calls: disabled  
Registered capability packages: 5  
Verified live connections: 0

## Provider-level foundation

- Canonical provider catalog, defensive-copy accessors and capability-to-package routing.
- Cohere capability domain taxonomy and coverage summary.
- Shared request/result, tenant context, opaque secret-reference, lifecycle and readiness contracts.
- Provider policy guardrails, recursive secret-field rejection and operation authorization boundary.
- Provider module service, discovery orchestrator, health summary, dependency map and stable manager facade.
- Python and PHP provider-level contracts.
- Eleven provider-wide cohere_shared_* modules.
- Legacy duplicate root-level generic package directories removed and their reusable code migrated into shared modules.

## Capability packages

Five dedicated capability packages follow the Google product-Core package convention. Each has ten subfolders: authentication, capabilities, docs, events, lifecycle, models, schemas, security, services and tests. Each package owns typed contracts, a capability service, non-secret configuration, manifest, README, public exports and an authentication/contract.php PHP caller-context contract.

## Provider routing

CohereCoreService dispatches classify, command, embed, rerank and tokenize requests to their own package validators. Unknown capabilities, malformed mappings, wrong field types, unsupported fields, unsupported execution options and nested secret-like metadata are rejected.

## Verification

Provider-wide tests cover successful dispatch, invalid payloads, unknown capabilities, wrong field types, secret-field rejection, unsupported fields/options, tenant-context policy, no-live-call status, defensive catalog copies and operation guardrails. Capability-level tests remain in each package.

GitHub Actions workflow: .github/workflows/cohere-core-ecosystem-tests.yml  
Test execution: pending GitHub Actions result; do not treat committed tests as passed until the workflow succeeds.

## Not implemented or enabled

- Live Cohere API/SDK transport.
- Production authentication and secure credential injection.
- ENGINE execution, retries, timeouts, queues or scheduling.
- DATABASE persistence and STORAGE artifacts.
- Verified account entitlement, model availability and provider smoke tests.

## Release gate

Do not enable live readiness until API/ENGINE adapters, credentials, tenant authorization, model configuration, integration tests, smoke tests and deployment checks are implemented and verified. Never commit provider secrets.
