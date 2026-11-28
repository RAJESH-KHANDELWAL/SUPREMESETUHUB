# Global Transport, Mobility, Logistics & Supply Chain Business API Ecosystem

Canonical Global entry point for the Transport, Mobility & Logistics industry identity
(transport_mobility_logistics) and the broader transport-business classification.

The former root-level transport_mobility_logistics/ folder contained only the
industry identity metadata. That metadata is now defined in this package and the
industry registry resolves the ID here.

The separate transport_logistics_supply_chain/ package remains in place because
it owns a distinct 12-category API implementation, service, routes, schemas and
tests currently wired through the industry router. Its exports remain exposed
through this consolidated package for compatibility; it is not deleted or
duplicated by this change.

This package also contains the transport-business classification domains and
nested Aviation/Aerospace entry point. Taxonomy scaffold only; not live vehicle
tracking, carrier onboarding, booking, customs clearance or proof of provider
availability.
