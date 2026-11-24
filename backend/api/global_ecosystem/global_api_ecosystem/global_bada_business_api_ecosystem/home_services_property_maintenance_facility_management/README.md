# Home Services, Property Maintenance & Facility Management API Ecosystem

Stable ID: `home_services_property_maintenance_facility_management`  
Coverage target: India + Global  
Channels: online, offline and hybrid  
Status: `taxonomy_scaffold`  
Top-level categories: 18

## Scope

Home and residential services, repair and maintenance, property upkeep, housing-society operations, commercial facility management, workplace/retail facilities and service-vendor coordination.

## API endpoints

- `GET /industries/home-services-facility-management/status`
- `GET /industries/home-services-facility-management/categories`
- `GET /industries/home-services-facility-management/categories?q=...`
- `GET /industries/home-services-facility-management/categories/{category_id}`
- `GET /industries/home-services-facility-management/cross-ecosystem-links`

## Gym, Spa, Massage & Wellness boundary

Gym and fitness centres, personal training, yoga and meditation, spa and massage services already have canonical taxonomy in `healthcare_wellness_fitness`. This package deliberately avoids duplicate categories and exposes canonical category IDs through its cross-ecosystem endpoint. Future home-visit wellness booking may reference those IDs while storing only home-service fulfilment relationships here.

## Adjacent boundaries

- Property development, real-estate transactions and major construction remain in `real_estate_construction`.
- Clinical care, diagnosis and medical treatment remain in healthcare ecosystems.
- Licensed security and specialist safety providers remain in `security_defence_safety_services`.
- Facility work-order coordination does not certify providers or licences.

## Operational safeguards

Before live launch, add provider identity verification, service-area coverage, credential/licence checks where required, transparent quotes, customer consent, appointment status, cancellation/refund rules, complaint handling, worker safety, audit logs and privacy controls. Never present an unverified listing as vetted.

This is a taxonomy/API scaffold, not a live provider directory, booking marketplace, dispatch network, payment gateway or verified service guarantee.
