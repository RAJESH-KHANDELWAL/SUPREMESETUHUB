# Adobe Core Implementation Status

- Canonical catalog product families: derived from `catalog.py`.
- Root manager: `manager.py` and `get_manager()`.
- PHP interoperability: `manager.php` with `php/AdobeCoreContract.php`.
- Domain inventory: provider governance plus all canonical product-family domains, derived from the catalog.
- Shared domain runtime: `domain_runtime.py`.
- Shared control plane: catalog, contracts, module service, orchestrator, policy and service.
- Tests: `test_adobe_core_domains.py`; run in repository CI/environment before marking passed.
- Live Adobe connections verified: 0.
- Credentials or secrets configured: none claimed.
- Product-specific entitlements, scopes and production API integrations remain unverified.

## Validation boundaries
Repository structure and code presence are not runtime validation. Test execution must be reported separately. A catalog mapping is not proof of endpoint, entitlement or live connectivity.
