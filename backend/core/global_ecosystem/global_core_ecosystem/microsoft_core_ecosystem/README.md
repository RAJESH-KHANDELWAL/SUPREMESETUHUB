# Microsoft Core Ecosystem

## Purpose
Provider-level, read-only control plane for Microsoft product-family metadata. This package catalogs products, assigns domains, exposes stable manager/service interfaces and declares policy boundaries. It does not claim that a product is licensed, provisioned, authorized, deployed or connected.

## Architecture
- `catalog.py`: canonical provider and product-family registry.
- `product_catalog.py`: stable offering inventory facade.
- `domain_catalog.py`: 19-domain taxonomy and deterministic classification.
- `domain_runtime.py`: read-only domain-scoped discovery.
- `policy.py`: tenant-context and capability metadata guardrails.
- `orchestrator.py`: product/domain discovery and dependency metadata.
- `service.py`: public read-only service.
- `manager.py`: canonical Python entry point (`get_manager()`).
- `manager.php`: PHP metadata interoperability facade; no provider API or DB access.
- `product_ecosystem_index.json`: machine-readable inventory contract.

## Existing product packages
The 16 existing product directories are retained and referenced by the canonical catalog. Their current placeholder state is not misrepresented as implemented adapters.

## Domain coverage
Provider Governance; Identity and Administration; Microsoft 365 and Collaboration; Azure Compute and Hosting; Azure Networking; Azure Data and Storage; AI/ML; Analytics and Observability; Developer and Application Platform; Windows and Endpoints; Security, Privacy and Compliance; Advertising and Commerce; Search and Browser Discovery; Gaming and Media; Business, Education and Enterprise; Payments, Billing and Subscriptions; Devices and Hardware; Language, Accessibility and Productivity; Specialty and Cross-Product.

## Integration boundaries
- Microsoft Entra OAuth and token lifecycle belong in the API/auth integration layer.
- Microsoft Graph and Azure SDK transport belong in dedicated API adapters.
- Secrets must be supplied by secure runtime configuration, never catalog metadata.
- This Core package does not create or connect to databases. The repository's existing central database configuration remains authoritative; no provider-specific database or port is introduced.
- Never infer live status from a catalog entry. Current catalog explicitly reports zero verified live connections.

## Import
```python
from backend.core.global_ecosystem.global_core_ecosystem.microsoft_core_ecosystem import get_manager
manager = get_manager()
print(manager.health())
```
