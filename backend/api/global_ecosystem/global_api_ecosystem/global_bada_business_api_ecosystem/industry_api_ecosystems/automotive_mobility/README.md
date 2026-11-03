# Automotive, Vehicles, Mobility & Transport Services API Ecosystem

Stable package ID: `automotive_mobility`

A discovery taxonomy for automotive products, vehicle services, EV infrastructure and passenger mobility across **Bharat (India) and global markets**. It supports online, offline and hybrid business models.

## Coverage

This ecosystem contains 18 independently organized categories. Each category has its own directory under `categories/<category_id>/`, with a category README and Python package initializer. The central `catalog.py` remains the canonical machine-readable taxonomy.

## Category scope

1. Passenger Cars & SUVs
2. Commercial Vehicles
3. Two-Wheelers & Three-Wheelers
4. Electric Vehicles & EV Mobility
5. Auto Parts & Components
6. Automotive Manufacturing
7. Vehicle Dealerships & Showrooms
8. Vehicle Rental & Leasing
9. Vehicle Repair & Maintenance
10. Vehicle Inspection & Testing
11. Automotive Accessories & Customisation
12. Vehicle Fleet Management
13. Vehicle Finance & Insurance
14. EV Charging & Battery Services
15. Vehicle Scrapping & Recycling
16. Automotive Technology & Software
17. Public & Private Passenger Mobility
18. Roadside Assistance & Breakdown Services

## Domain boundaries

- This ecosystem owns vehicle products, vehicle-specific services, automotive supply and passenger-mobility discovery.
- Freight forwarding, cargo movement, courier networks, warehousing, customs and general logistics remain in the Transport, Logistics & Supply Chain ecosystem.
- Fleet management here covers vehicle assets, maintenance, telematics and safety. Freight dispatch, shipment planning and logistics control towers remain outside this package.
- General banking, lending and insurance remain in Finance; this package covers only vehicle-specific finance and motor insurance discovery.
- General public transit infrastructure and transport authorities remain in Government/Public Services or Transport as applicable. This package covers vehicle operators and passenger mobility providers.
- EV charging hardware and battery services are vehicle-energy services; general electricity generation and grid utilities remain in Energy & Environment.

## API endpoints

- `GET /industries/automotive-mobility/status`
- `GET /industries/automotive-mobility/categories`
- `GET /industries/automotive-mobility/categories?q=...`
- `GET /industries/automotive-mobility/categories/{category_id}`

## Implementation status

`taxonomy_scaffold` — category structure and discovery endpoints only. This does not imply live listings, provider verification, vehicle-condition checks, licensing, government endorsement, regulatory approval, insurance underwriting or quality certification.
