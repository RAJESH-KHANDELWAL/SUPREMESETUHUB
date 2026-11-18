# BILIBILI CORE ECOSYSTEM

**Ecosystem ID:** `SOCIAL-BILIBILI-CORE-ECOSYSTEM`  
**Parent:** GLOBAL SOCIAL MEDIA CORE ECOSYSTEM  
**Package:** `backend/core/global_ecosystem/global_core_ecosystem/global_social_media_core_ecosystem/bilibili_social_media_core_ecosystem/`

## Responsibility

This package owns Bilibili platform identity, capability metadata, tenant-scoped policy boundaries, lifecycle and readiness metadata. Provider transport and authentication remain in the Global Social Media API layer.

## Provider reference

`backend/api/global_ecosystem/global_api_ecosystem/global_social_media_api_ecosystem/bilibili_social_media_api_ecosystem/`

API access hint: `official_api_region_scoped`. This is discovery metadata only and does not guarantee access, entitlement, approval or live connectivity.

## Security boundary

No credentials or tokens are stored here. No provider API calls, scraping, publishing or media operations are performed by this Core package.

