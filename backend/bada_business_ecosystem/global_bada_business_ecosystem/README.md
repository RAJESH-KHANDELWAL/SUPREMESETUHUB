# GLOBAL BADA BUSINESS ECOSYSTEM

This is the canonical Bada Business provider/product ecosystem under:

backend/bada_business_ecosystem/global_bada_business_ecosystem/

It owns the Bada Business platform profile, provider links, referral destinations, and program snapshots.

## Structure
- platform_resources/catalog.py — provider identity and the canonical resource catalog
- platform_resources/programs/ — LFP Digital, BB Impact and Idea to IPO records
- __init__.py — package identity and catalog exports

The parent backend/bada_business_ecosystem/ package owns the broader Bada Business product ecosystem and exposes this child package.

## API layer
The broader HTTP API implementation remains in backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/. Its existing router is exposed through backend/bada_business_ecosystem/api_ecosystem/ to preserve route registration and compatibility. It has not been physically moved in this step.

## Verification
The current provider links and program snapshots are resource metadata from existing repository links and owner-supplied page captures. They do not establish official API access, partnership, current availability, or live integration.
