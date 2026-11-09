"""Unified category catalog for Government, Public Services & Social Impact API Ecosystem."""
from __future__ import annotations

CATEGORIES = (
    {"id": "government_departments", "name": "Government Departments", "subcategories": ["central_government", "state_government", "local_government", "public_administration"]},
    {"id": "citizen_services", "name": "Citizen & Municipal Services", "subcategories": ["identity_documents", "licenses_permits", "certificates", "grievance_redressal", "municipal_services"]},
    {"id": "public_safety", "name": "Public Safety & Emergency Services", "subcategories": ["fire_services", "disaster_response", "emergency_management", "public_safety"]},
    {"id": "urban_rural_development", "name": "Urban, Rural & Community Development", "subcategories": ["urban_planning", "rural_development", "housing_programs", "community_infrastructure", "community_development"]},
    {"id": "public_health_programs", "name": "Public Health Programs", "subcategories": ["health_awareness", "vaccination_programs", "community_health", "sanitation"]},
    {"id": "social_welfare", "name": "Social Welfare, Skills & Protection", "subcategories": ["child_welfare", "senior_citizen_support", "disability_services", "social_assistance"] },
    {"id": "ngo_nonprofit", "name": "NGOs, Nonprofits, Charities & Foundations", "subcategories": ["charitable_trusts", "foundations", "nonprofit_management", "nonprofit_organizations", "charities", "volunteer_networks", "volunteering"]},
    {"id": "csr_social_enterprise", "name": "CSR & Social Enterprise", "subcategories": ["csr_programs", "impact_enterprises", "inclusive_business", "community_investment", "social_enterprise"]},
    {"id": "environmental_governance", "name": "Environmental Governance & Initiatives", "subcategories": ["pollution_regulation", "conservation_programs", "climate_policy", "environmental_authorities", "environmental_initiatives"]},
    {"id": "public_transport_services", "name": "Public Transport Services", "subcategories": ["municipal_transport", "public_transit", "road_services", "transport_authorities"]},
    {"id": "public_procurement", "name": "Public Procurement & Tenders", "subcategories": ["government_tenders", "public_contracts", "vendor_registration", "procurement_notices"]},
    {"id": "research_policy", "name": "Public Policy, Information & Research", "subcategories": ["policy_research", "think_tanks", "program_evaluation", "development_research"]},
    {"id": "public_information_services", "name": "Public Information Services", "subcategories": ["public_information", "open_data", "public_notices", "right_to_information"]},
    {"id": "skill_development_programs", "name": "Skill Development Programs", "subcategories": ["vocational_training", "employment_skills", "entrepreneurship_training", "digital_skills"]},
)

# Stable identifiers from the retired parallel package resolve to the canonical category.
LEGACY_CATEGORY_CROSSWALK = {
    "government_departments": "government_departments",
    "public_procurement": "public_procurement",
    "public_services": "citizen_services",
    "municipal_services": "citizen_services",
    "public_information_services": "public_information_services",
    "nonprofit_organizations": "ngo_nonprofit",
    "charities": "ngo_nonprofit",
    "foundations": "ngo_nonprofit",
    "community_development": "urban_rural_development",
    "rural_development": "urban_rural_development",
    "social_enterprise": "csr_social_enterprise",
    "volunteering": "ngo_nonprofit",
    "environmental_initiatives": "environmental_governance",
    "skill_development_programs": "skill_development_programs",
}

def list_categories():
    return [dict(item) for item in CATEGORIES]

def get_category(category_id: str):
    canonical_id = LEGACY_CATEGORY_CROSSWALK.get(category_id, category_id)
    for item in CATEGORIES:
        if item["id"] == canonical_id:
            return dict(item)
    return None
