# Automotive, Vehicles, Mobility & Transport Services API Ecosystem

Stable package ID: `automotive_mobility`

A discovery taxonomy for automotive products, vehicle services, EV infrastructure and passenger mobility across **Bharat (India) and global markets**. It supports online, offline and hybrid business models.

## Business-domain coverage

The ecosystem exposes **20 business domains** through the `/domains` API. These domains are intentionally mapped to **18 maintained API categories** so closely related areas share canonical implementations rather than creating duplicate packages.

1. Automobile Manufacturing
2. Cars & Commercial Vehicles
3. Two-Wheelers & Three-Wheelers
4. Electric Vehicles (EV)
5. EV Charging Infrastructure
6. Batteries & Energy Storage
7. Auto Parts & Components
8. Automobile Dealerships
9. Vehicle Sales & Resale
10. Vehicle Rental & Leasing
11. Vehicle Repair & Maintenance
12. Vehicle Insurance & Claims
13. Vehicle Registration & RTO Services
14. Road Transport & Mobility
15. Public Transport
16. Fleet Management
17. Taxi & Ride-Hailing
18. Logistics & Last-Mile Mobility (vehicle/passenger-mobility scope only)
19. Autonomous & Connected Vehicles
20. Global Automotive Technology

## API categories

Each category has a directory under `categories/<category_id>/`, with its own README and Python package initializer. The central `catalog.py` is the canonical machine-readable taxonomy.

## Domain boundaries

- This ecosystem owns vehicle products, vehicle-specific services, automotive supply, EV charging/battery services and passenger-mobility discovery.
- Freight forwarding, cargo movement, courier networks, warehousing, customs and general logistics remain in the Transport, Logistics & Supply Chain ecosystem. The last-mile domain here is limited to vehicle and passenger-mobility services.
- Fleet management here covers vehicle assets, maintenance, telematics and safety. Freight dispatch, shipment planning and logistics control towers remain outside this package.
- General banking, lending and insurance remain in Finance; this package covers only vehicle-specific finance and motor insurance discovery.
- Vehicle registration/RTO entries are informational discovery and document-support categories. They do not represent government affiliation, official RTO access or authority to perform regulated services.
- Vehicle operators and passenger-mobility providers are covered here; public transport authorities and infrastructure remain in Government/Public Services or Transport as applicable.

## API endpoints

- `GET /industries/automotive-mobility/status`
- `GET /industries/automotive-mobility/categories`
- `GET /industries/automotive-mobility/categories?q=...`
- `GET /industries/automotive-mobility/categories/{category_id}`
- `GET /industries/automotive-mobility/domains`
- `GET /industries/automotive-mobility/domains?q=...`
- `GET /industries/automotive-mobility/domains/{domain_id}`

## Implementation status

`taxonomy_scaffold` — category/domain discovery endpoints only. This does not imply live listings, provider verification, vehicle-condition checks, licensing, government endorsement, regulatory approval, insurance underwriting or quality certification. Router registration and integration tests must be completed by the parent application before production use.
