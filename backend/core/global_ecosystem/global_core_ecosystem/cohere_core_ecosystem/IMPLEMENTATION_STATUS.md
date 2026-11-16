# Cohere CORE Implementation Status

Provider status: interface_only  
Live provider calls: disabled  
Registered capabilities: 5  
Verified live connections: 0

## Implemented provider-level foundation

- Canonical provider catalog with defensive-copy accessors.
- Canonical five-capability inventory and package routing metadata.
- Cohere-specific domain taxonomy and coverage summary.
- Provider request/result, tenant context, opaque secret-reference and readiness contracts.
- Provider policy boundaries, operation guardrails and recursive secret-field rejection.
- Provider module service, discovery orchestrator, dependency map and stable manager facade.
- Provider PHP contract.
- Shared compatibility, configuration, contracts, documentation, events, exceptions, orchestration, security, testing, utilities and validation modules.
- Legacy duplicate root-level generic package directories removed; reusable responsibilities migrated into canonical cohere_shared_* modules.

## Capability package standard

All five packages retain the ten Google product-Core subfolders:
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

Each package owns typed contracts, a validator service, non-secret configuration, manifest, README, public exports and a PHP caller-context contract under authentication/contract.php.

## Provider routing

The provider facade dispatches:
- classify -> ClassifyCoreService
- command -> CommandCoreService
- embed -> EmbedCoreService
- rerank -> RerankCoreService
- tokenize -> TokenizeCoreService

It rejects unknown capabilities, malformed mappings, wrong field types, unsupported fields, unsupported execution options and nested secret-like metadata.

## Test coverage added

Provider-wide tests cover all five successful dispatch paths, capability-specific invalid payloads, unknown capability and non-mapping input rejection, wrong field types, nested secret-field rejection, unsupported fields and execution options, tenant-context policy, no-live-call status, catalog defensive copies and operation guardrails.

Capability-specific unit tests remain in each package's tests/ directory.

Test execution: not yet confirmed in CI or a configured local runtime. Committed tests must pass before claiming verified test readiness.

## Not implemented or not enabled

- Live Cohere API/SDK transport.
- Production authentication and secure credential injection.
- ENGINE execution, retries, timeouts, queues or scheduling.
- DATABASE persistence and STORAGE artifacts.
- Verified account entitlement, model availability and provider smoke tests.

## Release gate

Do not change readiness to live/ready until API and ENGINE adapters, credentials, tenant authorization, capability/model configuration, integration tests, smoke tests and deployment checks are implemented and verified. Never commit provider secrets.
