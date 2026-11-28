# GLOBAL TRANSPORT ROAD RAIL AIR MOBILITY CORE ECOSYSTEM

**Parent:** `GLOBAL CORE ECOSYSTEM`  
**Canonical path:** `backend/core/global_ecosystem/global_core_ecosystem/global_transport_road_rail_air_mobility_core_ecosystem/`

## Mission
Own the canonical CORE taxonomy, domain identity, capability metadata, policy boundaries and discovery contracts for Road Transport, Rail Transport, Air Transport and Mobility.

## Domain coverage
- **Road:** road networks, highways, streets, bridges, tunnels, passenger and freight transport, safety and accessibility metadata.
- **Rail:** passenger and freight rail, high-speed rail, metro/suburban rail, stations, terminals and infrastructure metadata.
- **Air:** passenger aviation, air cargo, airports, airline/operator identity and aviation safety metadata.
- **Mobility:** public transit, shared mobility, micromobility, fleets, multimodal journeys, route/network and accessibility metadata.

## Layer boundaries
- CORE owns taxonomy, stable IDs, capability classification, policy and readiness metadata.
- API owns provider APIs, authentication, transport clients and response normalization.
- Database/Storage own persistence and durable records.
- Engine owns dispatch, scheduling, retries and operational execution.
- CORE does not claim live bookings, dispatch, tracking, traffic control or transport operations.

The Bada Business transport package is a separate business-capability adapter. It references this canonical transport taxonomy instead of duplicating it.
