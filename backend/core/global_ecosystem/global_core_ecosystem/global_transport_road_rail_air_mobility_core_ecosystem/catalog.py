"""Canonical taxonomy for road, rail, air and mobility transport CORE metadata."""
from __future__ import annotations

from copy import deepcopy
from typing import Any

ECOSYSTEM_ID = "GLOBAL-TRANSPORT-ROAD-RAIL-AIR-MOBILITY-CORE-ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL TRANSPORT ROAD RAIL AIR MOBILITY CORE ECOSYSTEM"
PARENT_ECOSYSTEM_ID = "GLOBAL-CORE-ECOSYSTEM"
PACKAGE_PATH = (
    "backend/core/global_ecosystem/global_core_ecosystem/"
    "global_transport_road_rail_air_mobility_core_ecosystem"
)

TRANSPORT_DOMAINS: tuple[dict[str, Any], ...] = (
    {
        "domain_id": "ROAD_TRANSPORT",
        "name": "Road Transport",
        "capabilities": [
            "ROAD_NETWORK_CLASSIFICATION", "HIGHWAYS_AND_EXPRESSWAYS",
            "STREETS_AND_LOCAL_ROADS", "BRIDGES_TUNNELS_AND_ROAD_ASSETS",
            "ROAD_PASSENGER_TRANSPORT", "ROAD_FREIGHT_TRANSPORT",
            "ROAD_SAFETY_AND_ACCESSIBILITY", "ROAD_INFRASTRUCTURE_METADATA",
        ],
        "related_domains": ["MOBILITY", "LOGISTICS"],
    },
    {
        "domain_id": "RAIL_TRANSPORT",
        "name": "Rail Transport",
        "capabilities": [
            "RAIL_NETWORK_CLASSIFICATION", "PASSENGER_RAIL",
            "FREIGHT_RAIL", "HIGH_SPEED_RAIL", "METRO_AND_SUBURBAN_RAIL",
            "RAIL_STATIONS_AND_TERMINALS", "RAIL_SAFETY_AND_ACCESSIBILITY",
            "RAIL_INFRASTRUCTURE_METADATA",
        ],
        "related_domains": ["MOBILITY", "LOGISTICS"],
    },
    {
        "domain_id": "AIR_TRANSPORT",
        "name": "Air Transport",
        "capabilities": [
            "AVIATION_NETWORK_CLASSIFICATION", "AIR_PASSENGER_TRANSPORT",
            "AIR_CARGO_TRANSPORT", "AIRPORT_AND_TERMINAL_METADATA",
            "AIRLINE_AND_OPERATOR_METADATA", "AIR_TRAFFIC_SYSTEM_METADATA",
            "AVIATION_SAFETY_AND_ACCESSIBILITY",
        ],
        "related_domains": ["MOBILITY", "LOGISTICS"],
    },
    {
        "domain_id": "MOBILITY",
        "name": "Mobility",
        "capabilities": [
            "PUBLIC_TRANSIT", "SHARED_MOBILITY", "MICROMOBILITY",
            "PERSONAL_AND_FLEET_MOBILITY", "MULTIMODAL_JOURNEY_CLASSIFICATION",
            "ROUTE_AND_NETWORK_METADATA", "ACCESSIBILITY_AND_INCLUSIVE_MOBILITY",
            "TRAFFIC_AND_CONGESTION_METADATA",
        ],
        "related_domains": ["ROAD_TRANSPORT", "RAIL_TRANSPORT", "AIR_TRANSPORT"],
    },
)

def list_transport_domains() -> list[dict[str, Any]]:
    """Return independent copies of the canonical transport-domain catalogue."""
    return deepcopy(list(TRANSPORT_DOMAINS))

def get_transport_domain(domain_id: str) -> dict[str, Any] | None:
    """Look up a domain by its stable ID."""
    key = domain_id.strip().upper()
    for domain in TRANSPORT_DOMAINS:
        if domain["domain_id"] == key:
            return deepcopy(domain)
    return None

def get_transport_catalog() -> dict[str, Any]:
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "name": ECOSYSTEM_NAME,
        "parent_id": PARENT_ECOSYSTEM_ID,
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "domains": list_transport_domains(),
        "domain_count": len(TRANSPORT_DOMAINS),
        "live_connections_verified": False,
        "operational_dispatch_enabled": False,
        "api_transport_in_core": False,
    }
