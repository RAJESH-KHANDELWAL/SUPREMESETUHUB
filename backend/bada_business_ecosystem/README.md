# BADA BUSINESS ECOSYSTEM

This is the top-level Bada Business product ecosystem under SUPREMESETUHUB.

## Canonical hierarchy

backend/bada_business_ecosystem/
└── global_bada_business_ecosystem/

The child global_bada_business_ecosystem/ is the canonical owner of Bada Business platform resources, referral links, program data and provider metadata.

## Top-level components
- global_bada_business_ecosystem/ — canonical Bada Business provider/platform ecosystem
- api_ecosystem/ — API router entry point
- platform/, links/, programs/, courses/, products/, events/, registration/, referrals/ — additional product-domain namespaces

## API implementation boundary

The broad API route tree, schemas, industry taxonomy, business capability contracts and integrations remain implemented in:

backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/

Its router reads the canonical resource catalog from global_bada_business_ecosystem/platform_resources/. The API tree remains in the API layer to preserve app registration and existing import paths; it has not been physically moved in this change.

## Legacy folders

backend/bada_business/global_ecosystem/global_bada_business_ecosystem/ and the API-side bada_business_api_ecosystem resource package are compatibility facades. New platform resource content must be created in the canonical child ecosystem.

## Verification

Provider URLs and program snapshots are metadata from existing repository records and owner-supplied page captures. They do not prove official API access, partnership, current availability or a live connection.
