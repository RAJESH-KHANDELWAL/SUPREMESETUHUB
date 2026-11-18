# GLOBAL BADA BUSINESS Storage Ecosystem

Storage-owned business taxonomy for affiliate marketing, network marketing and direct selling. The root contains two canonical business domains with platform-specific namespaces kept separate.

## Categories
- `global_affiliate_marketing_business_storage_ecosystem/` — iDigitalPreneur, LeadsGuru and Millionaire Track metadata.
- `network_marketing_direct_selling_business_storage_ecosystem/` — YOUTAG business namespace and child affiliate taxonomy reference.

## Architecture
Python catalog and metadata models, API status handlers, PHP metadata readers, JSON manifests/schemas and offline tests. Provider API clients, authentication and external operations belong in integration layers. Production persistence belongs in the central database layer.

## Readiness
Catalog foundation only. No live business platform, referral, commission, payout or account connection is asserted. Preserve platform-level separation and never commit credentials or private customer data.
