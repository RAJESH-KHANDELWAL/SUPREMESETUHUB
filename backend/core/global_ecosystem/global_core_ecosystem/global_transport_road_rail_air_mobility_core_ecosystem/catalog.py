"""Canonical non-commercial transport and mobility domain taxonomy.

This catalog classifies transport modes and mobility systems. Commercial services,
providers, logistics operations and business workflows belong to the separate
Global Bada Business Transport Core package.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

ECOSYSTEM_ID = "GLOBAL-TRANSPORT-ROAD-RAIL-AIR-MOBILITY-CORE-ECOSYSTEM"

TRANSPORT_MODES: tuple[dict[str, Any], ...] = (
    {"id": "road_transport", "name": "Road Transport", "scope": "Road networks, highways, streets and movement by road.", "capabilities": ["ROAD_NETWORK_CLASSIFICATION", "ROAD_TRANSPORT_MODE_METADATA"]},
    {"id": "rail_transport", "name": "Rail Transport", "scope": "Railways, metro, suburban rail and rail infrastructure.", "capabilities": ["RAIL_NETWORK_CLASSIFICATION", "RAIL_TRANSPORT_MODE_METADATA"]},
    {"id": "air_transport", "name": "Air Transport", "scope": "Air travel, aviation routes, airports and air transport infrastructure.", "capabilities": ["AVIATION_MODE_CLASSIFICATION", "AIRPORT_INFRASTRUCTURE_METADATA"]},
    {"id": "water_maritime_transport", "name": "Water & Maritime Transport", "scope": "Inland waterways, coastal movement, maritime routes and port infrastructure.", "capabilities": ["WATERWAY_CLASSIFICATION", "MARITIME_TRANSPORT_MODE_METADATA"]},
    {"id": "passenger_mobility", "name": "Passenger Mobility", "scope": "How people move within and between settlements using public and private modes.", "capabilities": ["PASSENGER_MOBILITY_CLASSIFICATION", "ACCESSIBILITY_METADATA", "INTERMODAL_PASSENGER_JOURNEY_METADATA"]},
)

def list_transport_modes() -> list[dict[str, Any]]:
    """Return a defensive copy of the canonical transport-mode catalog."""
    return deepcopy(list(TRANSPORT_MODES))

def get_transport_mode(mode_id: str) -> dict[str, Any] | None:
    """Return one transport mode by its stable ID."""
    needle = mode_id.strip().casefold()
    if not needle:
        return None
    item = next((item for item in TRANSPORT_MODES if item["id"].casefold() == needle), None)
    return deepcopy(item) if item else None

__all__ = ["ECOSYSTEM_ID", "TRANSPORT_MODES", "list_transport_modes", "get_transport_mode"]
