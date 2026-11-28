"""Canonical service, work and business taxonomy for transport and mobility."""
from __future__ import annotations

from copy import deepcopy
from typing import Any

ECOSYSTEM_ID = "GLOBAL-TRANSPORT-ROAD-RAIL-AIR-MOBILITY-LOGISTICS-SUPPLY-CHAIN-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM"

BUSINESS_DOMAINS: tuple[dict[str, Any], ...] = (
    {"id": "road_transport_mobility", "name": "Road Transport & Mobility", "scope": "Road passenger and goods transport, commercial road networks and road-based mobility services.", "category_id": "road_transport_mobility"},
    {"id": "rail_metro_transport", "name": "Rail & Metro Transport", "scope": "Passenger rail, metro, suburban rail, rail freight, stations and rail infrastructure services.", "category_id": "rail_metro_transport"},
    {"id": "aviation_airport_transport", "name": "Aviation, Airports & Air Cargo", "scope": "Airlines, airports, ground handling, air cargo and aviation logistics services.", "category_id": "aviation_airport_transport"},
    {"id": "maritime_shipping_ports", "name": "Maritime, Shipping & Ports", "scope": "Container and bulk shipping, ports, coastal shipping, waterways and marine logistics.", "category_id": "maritime_shipping_ports"},
    {"id": "freight_logistics_supply_chain", "name": "Freight, Logistics & Supply Chain", "scope": "Freight forwarding, brokerage, procurement logistics, planning and supply-chain services.", "category_id": "freight_logistics_supply_chain"},
    {"id": "courier_parcel_last_mile", "name": "Courier, Parcel & Last-Mile Delivery", "scope": "Domestic and international courier, express parcels, e-commerce fulfilment and last-mile delivery.", "category_id": "courier_parcel_last_mile"},
    {"id": "warehousing_distribution_cold_chain", "name": "Warehousing, Distribution & Cold Chain", "scope": "Warehouses, distribution centres, inventory handling, cold storage and temperature-controlled logistics.", "category_id": "warehousing_distribution_cold_chain"},
    {"id": "fleet_vehicle_services", "name": "Fleet & Vehicle Services", "scope": "Fleet operations, leasing, maintenance, telematics, driver management and fleet optimisation.", "category_id": "fleet_vehicle_services"},
    {"id": "passenger_transport_public_transit", "name": "Passenger Transport & Public Transit", "scope": "Public and private passenger operators, buses, taxis, shuttles, school and employee transport.", "category_id": "passenger_transport_public_transit"},
    {"id": "global_aviation_aerospace_space_technology_core_ecosystem", "name": "Aviation, Aerospace & Space Technology Business", "scope": "Commercial aviation, aerospace supply chain, space technology services and related enterprises.", "category_id": "global_aviation_aerospace_space_technology_core_ecosystem"},
)

def list_business_domains() -> list[dict[str, Any]]:
    return deepcopy(list(BUSINESS_DOMAINS))

def get_business_domain(domain_id: str) -> dict[str, Any] | None:
    needle = domain_id.strip().casefold()
    if not needle:
        return None
    item = next((item for item in BUSINESS_DOMAINS if item["id"].casefold() == needle), None)
    return deepcopy(item) if item else None

def list_categories() -> list[dict[str, Any]]:
    """The category inventory is the same canonical business-domain inventory."""
    return list_business_domains()

def get_category(category_id: str) -> dict[str, Any] | None:
    return get_business_domain(category_id)

__all__ = ["ECOSYSTEM_ID", "BUSINESS_DOMAINS", "list_business_domains", "get_business_domain", "list_categories", "get_category"]
