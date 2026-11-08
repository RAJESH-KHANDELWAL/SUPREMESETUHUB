# BADA BUSINESS ECOSYSTEM

Canonical home for the Bada Business platform's own resources and ecosystem identity.

## Hierarchy

`GLOBAL ECOSYSTEM → BADA BUSINESS ECOSYSTEM`

This ecosystem owns:
- Bada Business platform links and referral destinations
- Programs, courses, events and registration resources
- Products, services and digital-store links
- Platform profile, source notes and verification metadata

## Platform resources

The canonical catalog is in `platform_resources/`.

It currently contains the repository's existing Bada Business links:
- LFP Digital
- Cash Growth Profit
- Idea to IPO
- Digital Dukan

Program snapshots include LFP Digital, BB Impact and Idea to IPO. Details and commercial terms were supplied in page captures and are not independently verified. Recheck availability, prices, dates, contact details and terms with Bada Business before relying on them.

## API boundary

The API implementation remains separate at:
`backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/`

That API ecosystem owns route transport, business taxonomy, industry registries, capability contracts and integrations. It should not own duplicate copies of Bada Business platform referral/course links. It may expose the canonical resource catalog through a read-only API endpoint.

## Verification

This resource catalog is not an official developer API, partnership confirmation, authentication credential store or live connection. `official_public_api_verified` and `live_connection_verified` remain false until independently established.
