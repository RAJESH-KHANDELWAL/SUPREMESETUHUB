# BADA BUSINESS CORE PROGRAMS

**Location:** `backend/core/global_ecosystem/global_core_ecosystem/bada_business_core_ecosystem/programs/`

This package implements the CORE domain for Bada Business program discovery and enrollment-request preparation.

## Canonical resource references

CORE reads provider-owned records from the canonical Global Bada Business Ecosystem. The following locations are references only; CORE must not maintain duplicate provider catalogs:

| Resource | Canonical path |
|---|---|
| Ecosystem root | `backend/global_ecosystem/global_bada_business_ecosystem/` |
| Platform resource catalog | `backend/global_ecosystem/global_bada_business_ecosystem/platform_resources/catalog.py` |
| Platform/referral URLs | `backend/global_ecosystem/global_bada_business_ecosystem/links/platform_links.py` |
| Community course URLs | `backend/global_ecosystem/global_bada_business_ecosystem/course_resources/BADA_BUSINESS_COMMUNITY_COURSE_LINKS.md` |
| Program snapshots | `backend/global_ecosystem/global_bada_business_ecosystem/platform_resources/programs/` |

The three currently declared program IDs are `lfp_digital`, `bb_impact`, and `idea_to_ipo`. Program metadata and any associated source URL remain owned by the canonical resource records. A program ID is not itself a separate URL.

## Responsibilities

- Discover, list, search and retrieve canonical program records.
- Normalize program identifiers.
- Validate the minimum applicant fields for a draft enrollment request.
- Define workflow contracts for discovery, comparison and request preparation.

## Architecture boundary

- Program facts, descriptions, links, prices and event snapshots remain owned by the canonical Global Bada Business Ecosystem paths listed above.
- This package imports the canonical resource catalog through `resource_adapter.py`; it does not duplicate provider data.
- API routes and HTTP schemas belong in API.
- AI recommendations and agent behavior belong in AI.
- Actual workflow execution and external provider calls belong in ENGINE or injected integration adapters.
- This package does not submit registrations, process payments, or claim a live Bada Business connection.

## Public interface

```python
from backend.core.global_ecosystem.global_core_ecosystem.bada_business_core_ecosystem.programs import (
    BadaBusinessProgramsManager,
)

manager = BadaBusinessProgramsManager()
manager.list_programs()
manager.get_program("lfp_digital")
manager.search_programs("leadership")
```

## Verification status

CORE domain scaffold is implemented. Live registration, provider API access and payment processing are not enabled. Current program terms and availability must be confirmed with Bada Business.
