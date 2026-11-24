# GLOBAL SOCIAL MEDIA CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_social_media_core_ecosystem/`

## Mission
Multi-provider Core control plane for registered social, messaging, creator, publishing, video, community and related platforms. Owns platform identity, taxonomy, discovery metadata, capability declarations, tenant context, policy boundaries and lifecycle metadata.

## Architecture
- `catalog.py`: canonical ecosystem identity.
- `product_ecosystem_index.json` and `product_catalog.py`: validated platform inventory.
- `domain_catalog.py` and `domain_runtime.py`: 14-domain taxonomy and shared domain manager.
- `contracts.py`: tenant context, opaque secret references and result contract.
- `policy.py`: capability checks, age-classification boundaries and sensitive-field redaction.
- `module_service.py`: reusable platform manager runtime.
- `orchestrator.py`, `service.py`, `manager.py`: discovery and public entry points.
- `manager.php` and `php/GlobalSocialMediaCoreContract.php`: PHP interoperability only.
- `test_social_media_core_domains.py`: structural and behavior tests.
- `*_social_media_core_ecosystem/`: 113 platform packages.
- `social_media_*_core_ecosystem/`: 14 domain packages.

## Layer boundaries
Core does not perform OAuth, account authentication, API transport, scraping, posting, messaging, content downloads, durable persistence, billing, analytics ingestion or moderation enforcement. Those belong to dedicated API, application, storage, analytics and safety layers. Registration does not prove current availability, public API access, entitlement, account connection or permission.

## Safety and privacy
Credentials remain opaque references in an external secret manager. Tenant and actor identity come from the authenticated application layer. Publishing, messaging, account changes and destructive actions require provider authorization and audit. Adult platform packages are 18+ metadata classifications only and require age assurance, consent, privacy controls and jurisdiction-specific review in the responsible application/safety layers.

## Inventory
- Registered platform packages: **113**
- Domain taxonomy packages: **14**
- Live connections verified: **0**
- API calls performed by this Core: **0**
