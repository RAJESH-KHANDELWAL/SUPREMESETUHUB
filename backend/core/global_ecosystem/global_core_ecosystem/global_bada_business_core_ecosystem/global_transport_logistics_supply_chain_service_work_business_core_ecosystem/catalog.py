"""Bada Business capability taxonomy reusing the canonical Transport CORE."""
from __future__ import annotations

from copy import deepcopy
from typing import Any

ECOSYSTEM_ID = "GLOBAL-BADA-BUSINESS-TRANSPORT-LOGISTICS-SUPPLY-CHAIN-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL BADA BUSINESS TRANSPORT LOGISTICS SUPPLY CHAIN SERVICE WORK BUSINESS CORE ECOSYSTEM"
PARENT_ECOSYSTEM_ID = "GLOBAL-BADA-BUSINESS-CORE-ECOSYSTEM"
TRANSPORT_CORE_ID = "GLOBAL-TRANSPORT-ROAD-RAIL-AIR-MOBILITY-CORE-ECOSYSTEM"
TRANSPORT_CORE_PATH = (
    "backend/core/global_ecosystem/global_core_ecosystem/"
    "global_transport_road_rail_air_mobility_core_ecosystem"
)
PACKAGE_PATH = (
    "backend/core/global_ecosystem/global_core_ecosystem/"
    "global_bada_business_core_ecosystem/"
    "global_transport_logistics_supply_chain_service_work_business_core_ecosystem"
)

BUSINESS_CAPABILITY_GROUPS: tuple[dict[str, Any], ...] = (
    {
        "group_id": "LOGISTICS",
        "name": "Global Logistics",
        "capabilities": [
            "FREIGHT_FORWARDING", "ROAD_RAIL_AIR_FREIGHT_SERVICES",
            "WAREHOUSING_AND_DISTRIBUTION", "FULFILMENT_AND_LAST_MILE",
            "COLD_CHAIN_LOGISTICS", "CUSTOMS_AND_CROSS_BORDER_LOGISTICS",
            "REVERSE_LOGISTICS", "FREIGHT_VISIBILITY_METADATA",
        ],
        "transport_domains": ["ROAD_TRANSPORT", "RAIL_TRANSPORT", "AIR_TRANSPORT"],
    },
    {
        "group_id": "SUPPLY_CHAIN",
        "name": "Global Supply Chain",
        "capabilities": [
            "SOURCING_AND_PROCUREMENT", "SUPPLIER_CLASSIFICATION",
            "DEMAND_AND_CAPACITY_PLANNING", "INVENTORY_AND_ORDER_FULFILMENT",
            "PRODUCTION_AND_DISTRIBUTION_COORDINATION",
            "TRACEABILITY_AND_SUPPLY_CHAIN_VISIBILITY", "SUPPLY_CHAIN_RISK_METADATA",
        ],
        "transport_domains": ["ROAD_TRANSPORT", "RAIL_TRANSPORT", "AIR_TRANSPORT"],
    },
    {
        "group_id": "SERVICES",
        "name": "Transport Services",
        "capabilities": [
            "PASSENGER_TRANSPORT_SERVICES", "FREIGHT_TRANSPORT_SERVICES",
            "FLEET_MANAGEMENT_SERVICES", "TERMINAL_AND_STATION_SERVICES",
            "AIRPORT_GROUND_SERVICES", "VEHICLE_MAINTENANCE_SERVICES",
            "TICKETING_AND_RESERVATION_SERVICE_CLASSIFICATION",
            "ROUTE_PLANNING_SERVICE_CLASSIFICATION",
        ],
        "transport_domains": ["ROAD_TRANSPORT", "RAIL_TRANSPORT", "AIR_TRANSPORT", "MOBILITY"],
    },
    {
        "group_id": "WORK",
        "name": "Transport and Logistics Work",
        "capabilities": [
            "DRIVER_AND_OPERATOR_ROLE_CLASSIFICATION",
            "PILOT_AND_CREW_ROLE_CLASSIFICATION",
            "RAIL_OPERATIONS_ROLE_CLASSIFICATION",
            "WAREHOUSE_AND_FULFILMENT_ROLE_CLASSIFICATION",
            "DISPATCH_AND_LOGISTICS_COORDINATION_ROLES",
            "FLEET_AND_MAINTENANCE_WORKFORCE",
            "SKILLS_TRAINING_AND_WORKFORCE_PLANNING",
        ],
        "transport_domains": ["ROAD_TRANSPORT", "RAIL_TRANSPORT", "AIR_TRANSPORT", "MOBILITY"],
    },
    {
        "group_id": "BUSINESS",
        "name": "Transport and Logistics Business",
        "capabilities": [
            "CARRIER_AND_FLEET_OPERATOR_MODELS", "FREIGHT_FORWARDER_AND_3PL_4PL_MODELS",
            "WAREHOUSE_AND_FULFILMENT_OPERATOR_MODELS",
            "PUBLIC_AND_SHARED_MOBILITY_OPERATOR_MODELS",
            "TRANSPORT_MARKETPLACE_AND_PLATFORM_MODELS",
            "INFRASTRUCTURE_CONCESSION_AND_OPERATOR_MODELS",
            "BUSINESS_COMPLIANCE_AND_REVENUE_MODEL_METADATA",
        ],
        "transport_domains": ["ROAD_TRANSPORT", "RAIL_TRANSPORT", "AIR_TRANSPORT", "MOBILITY"],
    },
)

def list_business_capability_groups() -> list[dict[str, Any]]:
    """Return independent copies of the business taxonomy."""
    return deepcopy(list(BUSINESS_CAPABILITY_GROUPS))

def get_business_capability_group(group_id: str) -> dict[str, Any] | None:
    key = group_id.strip().upper()
    for group in BUSINESS_CAPABILITY_GROUPS:
        if group["group_id"] == key:
            return deepcopy(group)
    return None

def get_business_catalog() -> dict[str, Any]:
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "name": ECOSYSTEM_NAME,
        "parent_id": PARENT_ECOSYSTEM_ID,
        "transport_core_id": TRANSPORT_CORE_ID,
        "transport_core_path": TRANSPORT_CORE_PATH,
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "capability_groups": list_business_capability_groups(),
        "capability_group_count": len(BUSINESS_CAPABILITY_GROUPS),
        "live_jobs_verified": False,
        "live_service_providers_verified": False,
        "live_transactions_verified": False,
    }
