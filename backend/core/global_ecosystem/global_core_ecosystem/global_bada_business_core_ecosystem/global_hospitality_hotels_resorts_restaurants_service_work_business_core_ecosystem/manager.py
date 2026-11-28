"""Manager for hospitality service, work and business capabilities."""
from __future__ import annotations

from pathlib import Path
from typing import Any

BUSINESS_ROOT = Path(__file__).resolve().parent
CORE_ECOSYSTEM_NAME = "global_hospitality_hotels_resorts_restaurants_core_ecosystem"

SERVICE_DOMAINS = (
    "accommodation_operations", "restaurant_food_beverage_operations",
    "reservations_guest_relations", "housekeeping_laundry",
    "front_office_concierge", "catering_events_banquets",
    "facility_maintenance_security", "procurement_inventory_supply",
    "sales_marketing_distribution", "revenue_finance_accounting",
    "human_resources_training_careers", "technology_digital_operations",
    "consulting_quality_compliance", "transport_wellness_recreation",
)


def ecosystem_manifest() -> dict[str, Any]:
    """Expose the business-layer scope and its canonical CORE dependency."""
    return {
        "name": "global_hospitality_hotels_resorts_restaurants_service_work_business_core_ecosystem",
        "layer": "global_bada_business_core_ecosystem",
        "depends_on": CORE_ECOSYSTEM_NAME,
        "service_domains": list(SERVICE_DOMAINS),
        "geography_source": "paired_hospitality_core_ecosystem",
        "record_policy": "verified_sources_only",
    }


def validate_business_record(record: dict[str, Any]) -> list[str]:
    required = ("id", "name", "business_type", "geography_id", "source", "verification_status")
    return [f"missing required field: {field}" for field in required if not record.get(field)]
