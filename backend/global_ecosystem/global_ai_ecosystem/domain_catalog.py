"""Bharat-to-global AI domain package registry."""
from __future__ import annotations
from typing import Any

_IDS = ["bharat_india","global_regions","everyday_life","human_knowledge","business_economy","finance_banking","education_research","healthcare_wellness","relationships_intimacy","adult_entertainment","porn_platform_governance","agriculture_food","environment_climate","government_civic","legal_compliance","media_creative","gaming_sports","travel_hospitality","transport_logistics","energy_water","manufacturing_industry","robotics_iot","space_aviation","software_web_apps","servers_cloud_infrastructure","cybersecurity_privacy","accessibility_social","frontier_supreme_research"]
_NAMES = ["Bharat India","Global Regions and Languages","Everyday Life","Human Knowledge","Business and Economy","Finance and Banking","Education and Research","Healthcare and Wellness","Relationships and Intimacy","Lawful Adult Entertainment","Adult Content and Porn Platform Governance","Agriculture and Food","Environment and Climate","Government and Civic Services","Legal and Compliance","Media and Creative","Gaming and Sports","Travel and Hospitality","Transport and Logistics","Energy and Water","Manufacturing and Industry","Robotics and IoT","Space and Aviation","Software, Websites and Apps","Servers and Cloud Infrastructure","Cybersecurity and Privacy","Accessibility and Social Impact","Frontier and Supreme Research"]
_POLICY = {"relationships_intimacy", "adult_entertainment", "porn_platform_governance", "healthcare_wellness", "government_civic", "legal_compliance"}
_ADULT = {"relationships_intimacy", "adult_entertainment", "porn_platform_governance"}

def get_domain_profile(domain_id: str) -> dict[str, Any] | None:
    if domain_id not in _IDS:
        return None
    i = _IDS.index(domain_id)
    result = {"id": domain_id, "name": _NAMES[i],
        "status": "POLICY_GATED_SCOPE" if domain_id in _POLICY else "SCOPE_DEFINED",
        "maturity": ("basic_normal", "standard", "professional", "advanced", "expert", "enterprise_industrial", "research", "frontier_supreme"),
        "geographic_scope": ("bharat_india", "south_asia", "asia_pacific", "middle_east", "africa", "europe", "north_america", "latin_america_caribbean", "oceania", "global_cross_border")}
    if domain_id in _ADULT:
        result["safeguards"] = ("adults_only_where_required", "age_assurance", "informed_consent", "privacy", "rights_verification", "lawful_content_only", "no_minors", "no_nonconsensual_intimate_imagery", "no_exploitation", "applicable_law_and_platform_policy")
    return result

def list_domain_ids() -> tuple[str, ...]:
    return tuple(_IDS)

def list_domain_profiles() -> tuple[dict[str, Any], ...]:
    return tuple(get_domain_profile(item) for item in _IDS)
