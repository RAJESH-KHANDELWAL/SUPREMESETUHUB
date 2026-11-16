# BADA BUSINESS CORE ECOSYSTEM

This package owns Bada Business domain rules, read-only resource discovery, policy boundaries and orchestration contracts.

## Canonical ecosystem connection

The canonical source of provider-owned facts and destinations is:

- Ecosystem root: `backend/global_ecosystem/global_bada_business_ecosystem/`
- Resource catalog: `backend/global_ecosystem/global_bada_business_ecosystem/platform_resources/catalog.py`
- Platform/referral destinations: `backend/global_ecosystem/global_bada_business_ecosystem/links/platform_links.py`
- Community course directory: `backend/global_ecosystem/global_bada_business_ecosystem/course_resources/BADA_BUSINESS_COMMUNITY_COURSE_LINKS.md`
- Program snapshots: `backend/global_ecosystem/global_bada_business_ecosystem/platform_resources/programs/`

CORE consumes these records through `resource_adapter.py`. Do not copy or independently maintain provider URLs, prices, course records, program descriptions, or event snapshots in CORE. Keep provider facts in the canonical Global Bada Business Ecosystem.

## CORE package structure

- `programs/` — program discovery, lookup, search and enrollment-request validation.
- `courses/` — course discovery and lookup facade.
- `events/` — event snapshot discovery.
- `links/` — platform/referral destination discovery.
- `products/` — product discovery facade; currently empty because no canonical product records are published.
- `registration/` — registration input validation only.
- `referrals/` — referral-code extraction only.
- `contracts.py` — shared CORE result contract.
- `policies.py` — operation guardrails and registration readiness.
- `resource_adapter.py` — read-only adapter to the canonical Global Bada Business Ecosystem.
- `service.py` / `manager.py` — public CORE service and facade.
- `workflows.py` — side-effect-free workflow definitions.
- `php/` — PHP 8+ contract interoperability.
- `tests/` — CORE behavior and policy tests.
- `ARCHITECTURE.md` / `IMPLEMENTATION_STATUS.md` — architecture and implementation record.

## Public interface

```python
from backend.core.global_ecosystem.global_core_ecosystem.bada_business_core_ecosystem import (
    BadaBusinessCoreManager,
)

manager = BadaBusinessCoreManager()
print(manager.status())
print(manager.programs())
print(manager.courses())
print(manager.links())
```

The existing `BadaBusinessProgramsManager` remains available for compatibility.

## Layer boundaries

- CORE: domain policies, contracts, discovery and orchestration.
- API: HTTP routes, request/response schemas and transport.
- PHP: PHP-side adapter and contract interoperability.
- ENGINE: external workflow execution and retries.
- DATABASE/STORAGE: persistence and retention.

The separate PHP adapter remains under `backend/php/global_ecosystem/global_php_ecosystem/bada_business_php_ecosystem/`.

## Safety and implementation status

Provider registration submission, payment processing, order creation and live provider connectivity are disabled. The repository does not currently verify an official public Bada Business API or a live provider connection. Product discovery remains empty until product records are added to the canonical resource package.

No credentials, payment details, private account data or access tokens belong in this package. Verify current provider terms and availability directly with Bada Business.
