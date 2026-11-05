# Global Transport, Mobility, Logistics & Supply Chain Business API Ecosystem

Consolidated entry point for the former `transport_mobility_logistics/` and
`transport_logistics_supply_chain/` root folders. Their package exports are
combined here; no nested folders named after those source folders are kept.

Existing API implementations remain under:
- `industry_api_ecosystems/transport_mobility_logistics/`
- `industry_api_ecosystems/transport_logistics_supply_chain/`

This package adds 9 transport-business classification domains and exposes the
existing industry packages without duplicating their API implementation.
Taxonomy scaffold only; not live vehicle tracking, carrier onboarding, booking,
customs clearance or proof of provider availability.
