# BADA BUSINESS ECOSYSTEM

Canonical Bada Business platform/product ecosystem inside SUPREMESETUHUB.

## Canonical root

backend/bada_business_ecosystem/

This is the one canonical owner for Bada Business platform-specific data and modules. New Bada Business platform links, referral URLs, programs, courses, products, events, registration definitions and provider metadata belong here—not in the old backend/bada_business path or API resource facade.

## Package structure

- platform/ — provider identity and platform profile
- links/ — public platform links and destination registry
- programs/ — program-specific records
- courses/ — learning and course resources
- products/ — products and digital-store resources
- events/ — event and webinar records
- registration/ — registration and enquiry definitions
- referrals/ — referral codes and destinations
- platform_resources/ — implemented provider resource catalog and program snapshots
- api_ecosystem/ — adapter exposing the Bada Business API router

## Existing canonical platform resources

The platform_resources catalog now physically contains the link catalog and program data files:
- LFP Digital
- Cash Growth Profit
- Idea to IPO
- Digital Dukan
- BB Impact program snapshot

The old platform resource folder delegates imports to this canonical root. API-side Bada Business resource modules also import these canonical files rather than carrying duplicate program data.

## API implementation boundary

The broad Global Bada Business API source tree, its routes, schemas, industry taxonomy, capabilities and integration modules remain at:

backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/

The top-level api_ecosystem package exposes that router. This preserves existing app route registration and import contracts. It does not mean the large API source tree has already been physically moved into this product/domain package. Keep API transport code in the API layer unless a separately tested full-tree migration is performed.

## Legacy compatibility

backend/bada_business/global_ecosystem/global_bada_business_ecosystem/ is now a compatibility facade. Do not add new Bada Business domain modules there.

backend/api/global_ecosystem/global_api_ecosystem/bada_business_api_ecosystem/ is a compatibility facade for old API resource imports. It must not maintain a second copy of links or program records.

## Verification

The existing links and program snapshots are sourced from repository records and owner-supplied captures. They do not establish current availability, official developer API access, a partnership or a live integration. Check commercial terms and event schedules with Bada Business before relying on them.
