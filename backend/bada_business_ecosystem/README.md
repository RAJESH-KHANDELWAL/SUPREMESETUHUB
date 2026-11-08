# BADA BUSINESS ECOSYSTEM

Canonical home for the complete Bada Business platform ecosystem inside SUPREMESETUHUB.

## Hierarchy
GLOBAL ECOSYSTEM -> BADA BUSINESS ECOSYSTEM

This package owns the Bada Business platform domain: platform identity, provider links, referral destinations, programs, courses, products, events, registration resources and provider-specific metadata.

## Package map
- platform/: platform identity and provider profile
- links/: public and referral destinations
- programs/: program-specific resources
- courses/: course catalog and learning resources
- products/: product and digital-store resources
- events/: event and webinar resources
- registration/: registration and enquiry resource definitions
- referrals/: referral codes and destination metadata
- platform_resources/: canonical link and program catalog
- api_ecosystem/: entry point to the Bada Business API router

## API implementation
The API transport, route handlers, schemas, business taxonomy, industry registries, capability contracts and integrations are currently implemented at:

backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/

That implementation is exposed from this package through api_ecosystem. The existing API route tree is deliberately retained for import and route-registration compatibility; the new package is the product/domain root. This is a safe integration, not a claim that every API source file has already been physically relocated.

The older backend/bada_business/global_ecosystem/global_bada_business_ecosystem/ package remains as a legacy compatibility provider for the resource catalog until a complete migration and downstream import audit can be performed.

## Resource and verification policy
Existing catalog links and page snapshots are references supplied by the repository owner or captured in the repository. They do not prove current availability, official developer API access, a commercial partnership or a live provider connection. Prices, program dates, event schedules and contact details must be verified with Bada Business before use.

The official public API and live connection flags remain false unless independently proven.
