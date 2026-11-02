"""Category catalog for Government, Public Services & Social Impact."""
from __future__ import annotations

CATEGORIES = (
    {"id": "government_departments", "name": "Government Departments", "subcategories": ["central_government","state_government","local_government","public_administration"]},
    {"id": "citizen_services", "name": "Citizen Services", "subcategories": ["identity_documents","licenses_permits","certificates","grievance_redressal"]},
    {"id": "public_safety", "name": "Public Safety & Emergency Services", "subcategories": ["fire_services","disaster_response","emergency_management","public_safety"]},
    {"id": "urban_rural_development", "name": "Urban & Rural Development", "subcategories": ["urban_planning","rural_development","housing_programs","community_infrastructure"]},
    {"id": "public_health_programs", "name": "Public Health Programs", "subcategories": ["health_awareness","vaccination_programs","community_health","sanitation"]},
    {"id": "social_welfare", "name": "Social Welfare & Protection", "subcategories": ["child_welfare","senior_citizen_support","disability_services","social_assistance"]},
    {"id": "ngo_nonprofit", "name": "NGOs & Nonprofit Organizations", "subcategories": ["charitable_trusts","foundations","nonprofit_management","volunteer_networks"]},
    {"id": "csr_social_enterprise", "name": "CSR & Social Enterprise", "subcategories": ["csr_programs","impact_enterprises","inclusive_business","community_investment"]},
    {"id": "environmental_governance", "name": "Environmental Governance", "subcategories": ["pollution_regulation","conservation_programs","climate_policy","environmental_authorities"]},
    {"id": "public_transport_services", "name": "Public Transport Services", "subcategories": ["municipal_transport","public_transit","road_services","transport_authorities"]},
    {"id": "public_procurement", "name": "Public Procurement & Tenders", "subcategories": ["government_tenders","public_contracts","vendor_registration","procurement_notices"]},
    {"id": "research_policy", "name": "Public Policy & Research", "subcategories": ["policy_research","think_tanks","program_evaluation","development_research"]},
)

def list_categories():
    return [dict(item) for item in CATEGORIES]

def get_category(category_id: str):
    for item in CATEGORIES:
        if item["id"] == category_id:
            return dict(item)
    return None
