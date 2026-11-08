# LEGACY BADA BUSINESS ECOSYSTEM PATH

This package path is retained for backward-compatible imports during the transition to the canonical top-level package:

backend/bada_business_ecosystem/

New Bada Business product resources should be added to the top-level package. This legacy package continues to provide the original platform resource implementation until the remaining imports and downstream consumers have been migrated and verified.

The API transport, route registration, business taxonomy, industry registries and integrations remain in backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/. The top-level Bada Business Ecosystem exposes that API package through its api_ecosystem entry point.

Existing resource records are user-supplied or repository-captured references; they do not prove current availability, official API access, partnership or live integration.
