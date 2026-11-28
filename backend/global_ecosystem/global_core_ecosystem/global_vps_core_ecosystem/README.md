# Global VPS Core Ecosystem

Provider-neutral Core catalogue and policy boundary for VPS/cloud virtual-machine services.

## Architecture
- Canonical provider registry: `catalog.py`
- Provider-specific metadata packages: one package per provider
- Capability taxonomy: `domain_catalog.py`
- Shared domain runtime: `domain_runtime.py`
- Request contracts and secret rejection: `contracts.py`
- Authorization classification: `policy.py`
- Discovery and health orchestration: `orchestrator.py`
- Public service facade: `service.py`
- Python manager: `manager.py`
- PHP metadata facade: `manager.php`
- Read-only master taxonomy mapping: `master_catalog.py`
- Offline structural tests: `test_vps_core.py`

## Provider inventory
The canonical catalogue contains 20 provider records. Each provider package contains exactly four purposeful files: `README.md`, `__init__.py`, `provider.py`, and `contracts.py`.

## Security and execution boundary
This Core validates metadata and request shape only. It does not create, start, stop, resize, rebuild or delete instances; execute SSH; modify firewalls or networks; call provider APIs; or persist credentials. Provider API transport and authenticated mutations belong in the independent API layer. Secrets must remain in an external secret manager or OS credential vault.

## Master catalogue
The module maps to existing taxonomy IDs only. It does not add artificial entries to reach the 2,468 target.
