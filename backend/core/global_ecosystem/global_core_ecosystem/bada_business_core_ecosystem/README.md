# BADA BUSINESS CORE ECOSYSTEM

This package owns Bada Business domain rules and orchestration contracts.

## Canonical ecosystem connection

The canonical source of provider-owned facts and destinations is:

- Ecosystem root: `backend/global_ecosystem/global_bada_business_ecosystem/`
- Resource catalog: `backend/global_ecosystem/global_bada_business_ecosystem/platform_resources/catalog.py`
- Platform/referral destinations: `backend/global_ecosystem/global_bada_business_ecosystem/links/platform_links.py`
- Community course directory: `backend/global_ecosystem/global_bada_business_ecosystem/course_resources/BADA_BUSINESS_COMMUNITY_COURSE_LINKS.md`
- Program snapshots: `backend/global_ecosystem/global_bada_business_ecosystem/platform_resources/programs/`

CORE consumes these records through its read-only programs resource adapter. Do not copy or independently maintain provider URLs, prices, course records, program descriptions, or event snapshots in CORE. Keep provider facts in the canonical Global Bada Business Ecosystem and keep CORE focused on domain rules and orchestration contracts.

## Programs domain

The `programs/` package provides program discovery, lookup, search and enrollment-request validation. It reads program facts from the canonical resource catalog at `backend/global_ecosystem/global_bada_business_ecosystem/platform_resources/`.

Provider facts are not copied into CORE. Registration submission, payment processing, API transport, AI recommendations and live provider connectivity are outside this package's current implementation.

## Public interface

```python
from backend.core.global_ecosystem.global_core_ecosystem.bada_business_core_ecosystem import (
    BadaBusinessProgramsManager,
)

manager = BadaBusinessProgramsManager()
print(manager.list_programs())
```

Current status: CORE programs domain scaffold implemented; live provider registration and payment processing are disabled.
