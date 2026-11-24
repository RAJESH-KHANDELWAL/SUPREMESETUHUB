"""Bharat-to-global workload taxonomy supported by the infrastructure catalog.

Domains describe customer workloads, not DigitalOcean products or provider
endorsements. Availability and legal requirements must be verified per region.
"""
GEOGRAPHIC_SCOPES = (
    "bharat_india", "south_asia", "asia_pacific", "middle_east",
    "europe", "africa", "north_america", "south_america", "oceania", "global",
)

MATURITY_LEVELS = (
    "normal", "standard", "professional", "advanced", "expert",
    "enterprise", "industrial", "research", "frontier", "supreme",
)

WORKLOAD_DOMAINS = (
    {"id": "ai_data", "name": "AI, ML and Data", "groups": ("ai", "machine_learning", "data_science", "analytics", "model_serving")},
    {"id": "software_digital", "name": "Software and Digital Products", "groups": ("software", "saas", "websites", "mobile_apps", "developer_tools", "apis")},
    {"id": "business_commerce", "name": "Business and Commerce", "groups": ("business", "msme", "enterprise", "ecommerce", "marketplaces", "crm", "affiliate", "direct_selling")},
    {"id": "finance_payments", "name": "Finance and Payments", "groups": ("fintech", "accounting", "payments", "billing", "risk", "compliance")},
    {"id": "education_research", "name": "Education and Research", "groups": ("education", "learning", "universities", "research", "scientific_computing")},
    {"id": "healthcare_wellness", "name": "Healthcare and Wellness", "groups": ("healthcare", "telehealth", "wellness", "health_information")},
    {"id": "communication_social", "name": "Communication and Social", "groups": ("messaging", "social_networks", "community", "collaboration", "streaming")},
    {"id": "media_entertainment", "name": "Media and Entertainment", "groups": ("publishing", "video", "music", "gaming", "digital_entertainment")},
    {"id": "industry_infrastructure", "name": "Industry and Infrastructure", "groups": ("manufacturing", "iot", "logistics", "transport", "energy", "smart_city")},
    {"id": "agriculture_environment", "name": "Agriculture and Environment", "groups": ("agritech", "climate", "environment", "water", "sustainability")},
    {"id": "people_relationships", "name": "People, Relationships and Life", "groups": ("identity", "family_services", "relationships", "intimacy_education")},
    {"id": "adult_only_services", "name": "Lawful Adults-Only Services", "groups": ("adult_platforms", "adult_entertainment", "sexual_wellness", "adult_content_governance"), "adults_only": True},
    {"id": "public_sector", "name": "Public Sector and Governance", "groups": ("government_services", "civic_technology", "public_information", "digital_identity")},
)

_DOMAIN_BY_ID = {item["id"]: item for item in WORKLOAD_DOMAINS}
_GROUP_TO_DOMAIN = {
    group: item["id"] for item in WORKLOAD_DOMAINS for group in item["groups"]
}

def list_workload_domains():
    return [dict(item, groups=list(item["groups"])) for item in WORKLOAD_DOMAINS]

def get_workload_domain(domain_id):
    item = _DOMAIN_BY_ID.get(domain_id)
    return dict(item, groups=list(item["groups"])) if item else None

def find_domain_for_group(group):
    return _GROUP_TO_DOMAIN.get((group or "").strip().casefold())

def validate_scope(geography, maturity):
    errors = []
    if geography not in GEOGRAPHIC_SCOPES:
        errors.append("unsupported geographic scope")
    if maturity not in MATURITY_LEVELS:
        errors.append("unsupported maturity level")
    return errors
