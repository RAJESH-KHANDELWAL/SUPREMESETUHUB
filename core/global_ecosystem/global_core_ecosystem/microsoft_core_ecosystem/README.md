# Microsoft Core Ecosystem

Provider-level, read-only control plane for Microsoft product-family metadata. It catalogs the 16 existing product families, assigns domains, exposes stable manager/service interfaces, and declares policy boundaries. It does not claim a product is licensed, provisioned, authorized, deployed, or connected.

## Architecture
- `manager.py`: single canonical Python entry point, provider/product registry, detached inventory helpers, and `get_manager()`.
- `domain_catalog.py`: 19-domain taxonomy and deterministic classification.
- `domain_runtime.py`: read-only domain-scoped discovery.
- `policy.py`: tenant-context and capability metadata guardrails.
- `orchestrator.py`: product/domain discovery and dependency metadata.
- `service.py`: public read-only service.
- `manager.php`: PHP metadata interoperability facade only.
- `product_ecosystem_index.json`: machine-readable inventory contract.
- `backend/test/test_microsoft_core_ecosystem.py`: canonical regression test suite.

## Integration boundaries
Microsoft Entra OAuth and token lifecycle belong in the API/auth integration layer. Microsoft Graph and Azure SDK transport belong in dedicated API adapters. Secrets must be supplied by secure runtime configuration, never catalog metadata. Database and persistence remain shared-layer ownership. This Core package does not create or connect to databases.

## Import
```python
from backend.core.global_ecosystem.global_core_ecosystem.microsoft_core_ecosystem import get_manager
manager = get_manager()
print(manager.health())
```
