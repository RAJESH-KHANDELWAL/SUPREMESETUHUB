# GLOBAL SOCIAL MEDIA API ECOSYSTEM

India + worldwide social-media provider directory, organized into a dedicated
folder for every catalogued platform.

## Folder architecture

Each provider has its own folder named
`<provider_id>_social_media_api_ecosystem/` with a `provider.py` metadata module.
The parent `social_media_api_ecosystem.py` catalog links each provider to its folder.

The catalog currently contains 112 provider entries, spanning:

- Global mainstream networks, microblogging and messaging
- Photo/video, short-video, live streaming and creator communities
- Professional networks, publishing, blogs, Q&A and forums
- Federated and decentralized social networks
- India-first and regional-language social platforms
- Creator memberships, social commerce and age-restricted adult platforms

## Core files

- `social_media_api_ecosystem.py` — master catalog, category metadata and filters
- `service.py` — provider directory and detail lookup services
- `routes.py` — FastAPI overview, list and provider-detail routes
- `schemas.py` — reserved for shared request/response schemas
- `integrations/` — integration adapters and provider connection workflows
- `services/` — shared service implementations
- `tools/` — shared tools
- `meta_social_media_api_ecosystem/` — Meta provider family
- `x_social_media_api_ecosystem/` — X provider family
- `<provider_id>_social_media_api_ecosystem/` — dedicated provider folder

## API access and connection status

The `api_access` field is a discovery hint, not a guarantee of current availability,
free access, approval or API scope. Verify official documentation, product status,
developer approval, regional access and platform terms before implementation.

All provider modules are metadata scaffolds. No credentials are included and no
provider-wide live connection is claimed. Each connector must be implemented and
tested independently before marking it connected.

## Adult and age-restricted platforms

Adult-oriented entries are directory metadata only. Any future account integration
must be lawful, consensual, age-restricted, privacy-preserving and compliant with
applicable jurisdictional law and platform terms. This ecosystem does not provide
explicit media generation, hosting, scraping or distribution.
