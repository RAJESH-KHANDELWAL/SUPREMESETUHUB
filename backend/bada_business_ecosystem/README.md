# BADA BUSINESS ECOSYSTEM

Canonical top-level home for the complete Bada Business product ecosystem in SUPREMESETUHUB.

## Hierarchy

backend/bada_business_ecosystem/ is the product/domain root. It owns Bada Business platform resources: links, programs, courses, products, events, registration and referral destinations.

## Components

- platform_resources/: canonical catalog of platform links and program snapshots.
- platform/, links/, programs/, courses/, products/, events/, registration/, referrals/: domain boundaries for structured modules. Do not invent live data where no source exists.
- api_ecosystem/: stable entry point to the separately implemented API transport layer.

## API boundary

The API implementation and its existing route tree remain under backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/ so existing imports, route registration and integrations are not broken by a mass move. The api_ecosystem package exposes that implementation from this top-level ecosystem. The API consumes the canonical resource catalog; it does not own duplicate platform links.

## Legacy compatibility

The earlier backend/bada_business/global_ecosystem/global_bada_business_ecosystem/ path remains as a compatibility package during migration. New Bada Business product resources should be added here.

## Verification

Catalog entries are resource references, not proof of official API access, partnership or live integration. Provider terms, prices, event dates and availability must be independently checked.
