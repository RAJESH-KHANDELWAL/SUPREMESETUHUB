# Global Transport, Road, Rail, Air, Mobility, Logistics & Supply Chain Service / Work / Business Core Ecosystem

This is the separate Bada Business Core package for commercial activity around
transport and mobility. It classifies service providers, operators, work domains,
business models and supply-chain capabilities.

## Business domains

- `road_transport_mobility/` — **Road Transport & Mobility:** Road passenger and goods transport, commercial road networks and road-based mobility services.
- `rail_metro_transport/` — **Rail & Metro Transport:** Passenger rail, metro, suburban rail, rail freight, stations and rail infrastructure services.
- `aviation_airport_transport/` — **Aviation, Airports & Air Cargo:** Airlines, airports, ground handling, air cargo and aviation logistics services.
- `maritime_shipping_ports/` — **Maritime, Shipping & Ports:** Container and bulk shipping, ports, coastal shipping, waterways and marine logistics.
- `freight_logistics_supply_chain/` — **Freight, Logistics & Supply Chain:** Freight forwarding, brokerage, procurement logistics, planning and supply-chain services.
- `courier_parcel_last_mile/` — **Courier, Parcel & Last-Mile Delivery:** Domestic and international courier, express parcels, e-commerce fulfilment and last-mile delivery.
- `warehousing_distribution_cold_chain/` — **Warehousing, Distribution & Cold Chain:** Warehouses, distribution centres, inventory handling, cold storage and temperature-controlled logistics.
- `fleet_vehicle_services/` — **Fleet & Vehicle Services:** Fleet operations, leasing, maintenance, telematics, driver management and fleet optimisation.
- `passenger_transport_public_transit/` — **Passenger Transport & Public Transit:** Public and private passenger operators, buses, taxis, shuttles, school and employee transport.
- `global_aviation_aerospace_space_technology_core_ecosystem/` — **Aviation, Aerospace & Space Technology Business:** Commercial aviation, aerospace supply chain, space technology services and related enterprises.

## Layer boundary

Core owns business-domain identity, taxonomy, capability metadata and discovery.
It does not book transport, dispatch vehicles, track shipments, onboard carriers,
perform customs clearance, execute payments, or claim provider availability.
API, engine, database, storage and deployment layers own those operations.
