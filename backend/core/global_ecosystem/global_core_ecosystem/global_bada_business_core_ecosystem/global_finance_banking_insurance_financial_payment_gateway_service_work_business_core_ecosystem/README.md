# Global Finance, Banking, Insurance & Financial Payment Gateway — Service, Work & Business CORE

## Purpose and placement

This is the commercial classification layer under **Global Bada Business CORE**. It mirrors the control-plane architecture used by Google CORE while consuming the existing finance taxonomy as a read-only canonical dependency.

- **This module:** services, professional work, business lines, delivery models, package discovery, classification contracts, policy boundaries and health.
- **Canonical Global Finance CORE:** owns the finance domain definitions and canonical package inventory.
- **Global Supreme master catalogue:** remains the master topic taxonomy and implementation-registry reference.

The original Global Finance CORE folder remains at:

`backend/core/global_ecosystem/global_core_ecosystem/global_finance_banking_insurance_financial_payment_gateway_core_ecosystem`

The master file remains unchanged by this module:

`backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json`

## Architecture

| File | Responsibility |
|---|---|
| `catalog.py` | Ecosystem identity, parent, canonical dependency, master registry reference and package index |
| `domain_catalog.py` | 15 commercial domains, service/work/business types, delivery models and exhaustive mapping validation |
| `product_catalog.py` | Package inventory derived from canonical Global Finance CORE packages |
| `contracts.py` | Typed tenant, classification-request and result contracts |
| `policy.py` | Sensitive-data exclusions and financial-operation guardrails |
| `domain_runtime.py` | Read-only manager for an individual business domain |
| `module_service.py` | Package-scoped discovery service |
| `service.py` | Application-facing status, classification, search and validation |
| `orchestrator.py` | Catalogue, domain, package, search, health and dependency orchestration |
| `manager.py` | Stable public Python manager API |
| `manager.php` | PHP interoperability facade; Python remains canonical |
| `php/` | PHP value contracts for safe result/domain metadata |
| `test/` | Contract, catalogue, policy, package and mapping tests |

## Classification model

Each canonical finance domain is mapped to a corresponding commercial domain. The module classifies:

- **SERVICE:** a deliverable offered to a customer, organization or institution.
- **WORK:** a task, role, profession, project, operation or engagement performed by people or systems.
- **BUSINESS:** an enterprise, practice, platform, marketplace or commercial model.

It also exposes delivery-model labels such as B2B, B2C, B2G, D2C, marketplace, platform, agency, consultancy, freelance, subscription and cooperative. These are taxonomy labels, not proof that a provider or business is operational.

## Safety and regulatory boundary

This is a metadata and classification control plane only. It does not connect to a bank, payment gateway, insurer, broker or lender; store credentials; move funds; initiate refunds or payouts; approve credit; underwrite insurance; execute trades; or provide regulated financial advice.

Jurisdiction-specific legal review and required licenses/authorizations remain mandatory wherever applicable. Live execution belongs in separately secured, tested and authorized API/provider layers.

## Stable Python entry point

`from ...manager import get_manager`

Supported operations include `status()`, `health()`, `catalog()`, `list_domains()`, `list_domain_inventory()`, `get_domain_manager()`, `list_packages()`, `get_package()`, `list_offerings()`, `get_offering()`, `search()`, `classify()`, `validate()` and `dependency_map()`.

## Integrity guarantees

- Canonical domain and package definitions are imported; they are not copied or independently redefined.
- Every canonical package must map to exactly one commercial domain.
- Missing, unknown and duplicate domain/package mappings fail validation.
- Public summaries exclude credential-like and account-secret fields.
- The master catalogue is referenced, not silently rewritten.
