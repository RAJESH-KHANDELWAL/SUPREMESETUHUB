# INTEGRATIONS BOUNDARY

This package is reserved for provider adapters owned by the API/integration layer. Individual Core may register adapter identifiers and capability metadata only.

- No credentials, tokens or secret values belong here.
- No network calls or SDK clients are implemented by this Core catalog foundation.
- Each future adapter must have explicit provider authorization, tenant scoping, consent checks, timeout/retry policy, safe error handling and integration tests.
- Mark a provider live only after an authenticated deployment smoke test; catalog presence is not connectivity evidence.

**Current status:** placeholder boundary; no live adapters verified.
