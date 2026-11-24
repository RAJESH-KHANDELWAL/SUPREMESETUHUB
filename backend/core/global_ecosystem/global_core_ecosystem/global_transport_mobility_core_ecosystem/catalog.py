"""Canonical taxonomy for Global Transport and Mobility Core."""
from copy import deepcopy
ECOSYSTEM_ID = "GLOBAL-TRANSPORT-MOBILITY-CORE-ECOSYSTEM"
PARENT_ID = "GLOBAL-CORE-ECOSYSTEM"
STATUS = "CORE_CATALOG_ONLY"
TRANSPORT_MODES = (
    {"id": "ROAD_TRANSPORT", "name": "Road Transport", "description": "Roads, highways, bridges and road movement."},
    {"id": "RAIL_TRANSPORT", "name": "Rail Transport", "description": "Railways, metro systems and rail corridors."},
    {"id": "AIR_TRANSPORT", "name": "Air Transport", "description": "Air travel, airports and aircraft movement."},
    {"id": "WATER_TRANSPORT", "name": "Water Transport", "description": "Ferries and inland waterway movement."},
    {"id": "PUBLIC_TRANSIT", "name": "Public Transit", "description": "Bus, metro and tram passenger networks."},
    {"id": "PERSONAL_MOBILITY", "name": "Personal Mobility", "description": "Cars, motorcycles, bicycles and personal vehicles."},
    {"id": "SHARED_MOBILITY", "name": "Shared Mobility", "description": "Ride pooling, car sharing and bike sharing."},
    {"id": "ACTIVE_MOBILITY", "name": "Active Mobility", "description": "Walking, cycling and accessible non-motorized travel."},
    {"id": "INTERMODAL_TRANSPORT", "name": "Intermodal Transport", "description": "Journeys connecting road, rail, air and water."},
    {"id": "TRANSPORT_INFRASTRUCTURE", "name": "Transport Infrastructure", "description": "Stations, terminals, roads, tracks and supporting infrastructure."},
    {"id": "TRAFFIC_TRANSIT_SYSTEMS", "name": "Traffic and Transit Systems", "description": "Traffic management and public transit coordination."},
    {"id": "ACCESSIBLE_MOBILITY", "name": "Accessible Mobility", "description": "Inclusive and accessible passenger movement."},
)
def list_catalog():
    return deepcopy(list(TRANSPORT_MODES))
