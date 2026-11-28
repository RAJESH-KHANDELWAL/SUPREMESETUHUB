# AWS Core Implementation Status

## Canonical architecture

- Provider root: metadata-only AWS Core control plane.
- Canonical Python entry point: `AwsCoreManager` via `get_manager()`.
- PHP interoperability facade: `manager.php` backed by `php/AwsCoreContract.php`.
- Root services: provider catalog, contracts, policy, product catalog, domain catalog/runtime, module service, orchestrator and status facade.
- Service families: 16 registered from the repository's AWS API Ecosystem catalog; each family package delegates to its existing family service.
- Domain taxonomy: 13 AWS-specific domains with individual package managers and offering inventory.
- Shared support packages: 11 standardized `aws_shared_<capability>_core_ecosystem` packages.
- Product/domain index: `product_ecosystem_index.json`.
- Alignment and regression tests: `test_google_core_alignment.py` and `tests/test_catalog.py`.

## Security and policy boundaries

- Account context validates a 12-digit AWS account ID, AWS region shape, tenant and actor identifiers.
- Optional IAM/STS principal ARN must be well-formed and belong to the supplied AWS account.
- Credential references accept approved secret-manager or workload-identity reference types only; raw credential material is not a Core contract.
- Capability checks reject disabled modules and unregistered capabilities.
- Public module summaries use an explicit allow-list to prevent arbitrary metadata or credential-like fields from leaking.
- Core policy checks are metadata guardrails only; AWS IAM, resource policies, application authorization and audit enforcement remain mandatory in the API/application layers.

## Readiness

- All 16 families remain `CORE_CATALOG_ONLY`.
- API availability is unverified (`null`).
- Live AWS connections verified: 0.
- Credentials stored in Core: 0.
- AWS API calls performed by Core: 0.

These values describe catalog/control-plane state only. They do not establish AWS account authorization, regional service availability, deployed adapter readiness or production connectivity. Test files have been updated; CI execution and passing status must be verified separately.
