"""Explicit coverage map for industry packages mounted as dedicated routers.

A registry entry is not considered routed merely because its taxonomy package exists.
Keep this list synchronized with the router imports in routes.py.
"""
from __future__ import annotations

from .registry import INDUSTRY_ECOSYSTEMS

ROUTED_INDUSTRY_IDS = frozenset({
    "agriculture_food_natural_resources",
    "education_learning_training",
    "jobs_careers_employment",
    "finance_banking_insurance",
    "real_estate_construction",
    "retail_ecommerce_consumer_goods",
    "technology_it_telecommunications",
    "manufacturing_industrial_services",
    "transport_logistics_supply_chain",
    "travel_tourism_hospitality",
    "marketing_media_entertainment",
    "arts_culture_heritage_creative_economy",
    "international_trade_import_export_customs_global_commerce",
    "energy_utilities_environment",
    "professional_legal_business_services",
    "government_public_services_social_impact",
    "automotive_mobility",
    "personal_lifestyle_wellness",
    "sports_recreation_community",
    "food_hospitality_restaurants",
    "security_defence_safety_services",
    "science_research_innovation",
    "mining_metals_minerals",
    "digital_infrastructure_telecommunications",
    "aviation_aerospace_space_technology",
    "water_resources_marine_industries",
    "fashion_textiles_apparel",
    "home_services_property_maintenance_facility_management",
    "healthcare_life_sciences",
})


def get_industry_router_coverage() -> dict[str, object]:
    """Report dedicated-router coverage without implying provider/live integrations."""
    registered_ids = {str(item["id"]) for item in INDUSTRY_ECOSYSTEMS}
    routed = sorted(registered_ids & ROUTED_INDUSTRY_IDS)
    missing = sorted(registered_ids - ROUTED_INDUSTRY_IDS)
    return {
        "success": True,
        "status": "partial",
        "registered_industry_count": len(registered_ids),
        "dedicated_router_count": len(routed),
        "missing_dedicated_router_count": len(missing),
        "coverage_percent": round((len(routed) / len(registered_ids)) * 100, 2) if registered_ids else 100.0,
        "routed_industry_ids": routed,
        "missing_industry_ids": missing,
        "note": "Dedicated taxonomy routes only; this does not verify live providers, business records, or external API connections.",
    }
