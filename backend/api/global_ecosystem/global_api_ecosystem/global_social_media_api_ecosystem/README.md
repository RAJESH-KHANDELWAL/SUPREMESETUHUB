# Global Social Media API Ecosystem

India + worldwide provider directory spanning mainstream social networks, messaging,
short video, live streaming, professional networks, publishing, Q&A, federated
communities, creator memberships, social commerce and age-restricted adult platforms.

## Main catalog

- `social_media_api_ecosystem.py` — provider directory, categories, cautious API-access
  discovery labels, implementation rules and region/category filters.
- `integrations/` — integration metadata and service endpoints.
- `services/` — service-layer files.
- `tools/` — tool-layer files.
- `meta_social_media_api_ecosystem/` — Meta provider family.
- `x_social_media_api_ecosystem/` — X provider family.

## Important API status note

A directory entry does not mean that a public API exists, that access is free, or that
an integration is live. Some providers require partner approval, paid access, app
review or region-specific credentials. Others have no general public API or may be
discontinued. Verify each provider's current official documentation and product
status before implementation.

## Adult and age-restricted services

Adult creator and adult-video platforms are listed as provider metadata only. Any
future integration must be lawful, consensual, age-restricted, privacy-preserving and
compliant with the laws applicable in the user's jurisdiction and the provider's
terms. This catalog does not create, host, scrape, or distribute explicit media.

## India and regional availability

Platform availability, legality and access can vary by country, state, court order,
government direction and provider policy. Verify current Indian legal requirements,
geo-restrictions, age-assurance requirements and official terms before enabling a
provider.

## Connectivity status

This is a catalog, not a universal live connector. Individual providers must be
implemented and tested independently. `live_connections_verified` remains false
until actual authenticated integrations have been verified.
