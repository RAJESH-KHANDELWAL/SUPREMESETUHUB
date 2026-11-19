# COHERE SHARED CONTRACTS

Canonical provider-wide Cohere CORE contracts:

- `CapabilityRequest` and `CoreResult` for the Python provider facade
- `TenantContext` for authenticated application-supplied identity
- `SecretReference` for opaque secret-manager pointers
- `Readiness` and `EcosystemState` for lifecycle/readiness vocabulary
- `CapabilityDescriptor` for normalized capability metadata

Capability-specific request payloads remain in each capability package. Contracts do not perform API calls or resolve secrets.
