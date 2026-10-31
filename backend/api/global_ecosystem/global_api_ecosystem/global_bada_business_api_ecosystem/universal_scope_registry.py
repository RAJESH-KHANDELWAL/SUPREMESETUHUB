"""Universal India + Global work, business and people taxonomy.

This module defines a curated, extensible classification registry. It is NOT a
live directory of employers, companies, vacancies, users, providers or services.
All records remain catalog-only until sourced, verified and connected to a
permitted data provider. Adult-industry classifications are restricted to lawful
18+ contexts and must be protected by application-level age, consent, privacy
and jurisdiction controls.
"""
from __future__ import annotations

from typing import Any

REGISTRY_VERSION = "1.0.0"
REGISTRY_STATUS = "taxonomy_catalog_only"
GEOGRAPHIC_COVERAGE = ("india", "global")
DELIVERY_MODES = ("online", "offline", "hybrid", "remote", "on_site")
WORK_ARRANGEMENTS = (
    "full_time", "part_time", "contract", "temporary", "freelance", "gig",
    "internship", "apprenticeship", "volunteer", "self_employed",
    "business_owner", "seasonal", "project_based", "remote", "on_site",
)
AUDIENCE_GROUPS = (
    "school_students", "college_students", "university_students", "freshers",
    "job_seekers", "employees", "workers", "professionals", "freelancers",
    "gig_workers", "self_employed", "homemakers", "caregivers", "parents",
    "entrepreneurs", "founders", "business_owners", "investors", "retired_people",
    "individuals", "couples", "families", "relatives", "friends", "communities",
    "institutions", "companies", "nonprofits", "public_sector",
)
BUSINESS_SIZES = (
    "individual", "home_based", "micro", "small", "medium", "large",
    "enterprise", "multinational",
)
BUSINESS_STAGES = (
    "idea", "pre_launch", "startup", "early_revenue", "growth",
    "established", "mature", "restructuring", "closed",
)

# Each domain has stable IDs and a shared record shape. Subcategories are
# intentionally broad so country-specific taxonomies can extend them.
GLOBAL_WORK_BUSINESS_DOMAINS: tuple[dict[str, Any], ...] = (
    {
        "id": "work_careers_employment", "name": "Work, Jobs & Careers",
        "audiences": ["job_seekers", "employees", "workers", "freshers", "professionals"],
        "subcategories": [
            "government_jobs", "private_sector_jobs", "public_sector_jobs",
            "international_jobs", "local_jobs", "remote_jobs", "hybrid_jobs",
            "full_time_jobs", "part_time_jobs", "contract_jobs", "temporary_jobs",
            "seasonal_jobs", "shift_work", "entry_level_jobs", "experienced_jobs",
            "executive_jobs", "career_changes", "return_to_work", "retirement_work",
            "career_guidance", "recruitment", "staffing", "placements",
        ],
        "modes": ["online", "offline", "hybrid", "remote", "on_site"],
        "adult_only": False,
    },
    {
        "id": "freelance_gig_independent_work", "name": "Freelancing, Gig & Independent Work",
        "audiences": ["freelancers", "gig_workers", "self_employed", "professionals", "students"],
        "subcategories": [
            "writing_editing", "translation_localization", "graphic_design",
            "web_development", "app_development", "software_engineering",
            "data_analysis", "ai_automation", "digital_marketing", "seo",
            "social_media_management", "video_audio_production", "photography",
            "virtual_assistance", "bookkeeping_accounting", "legal_consulting",
            "business_consulting", "tutoring", "coaching_training",
            "delivery_gig_work", "driving_transport_gigs", "home_service_gigs",
            "creative_commissions", "professional_contracting", "microtasks",
        ],
        "modes": ["online", "offline", "hybrid", "remote", "on_site"],
        "adult_only": False,
    },
    {
        "id": "students_education_skills", "name": "Students, Education & Skills",
        "audiences": ["school_students", "college_students", "university_students", "freshers"],
        "subcategories": [
            "school_education", "higher_education", "vocational_education",
            "online_learning", "coaching_tuition", "test_preparation",
            "certifications", "diplomas", "degrees", "research", "scholarships",
            "student_projects", "internships", "apprenticeships", "campus_placements",
            "career_counselling", "digital_skills", "technical_skills",
            "business_skills", "language_learning", "financial_literacy",
            "entrepreneurship_education", "special_needs_learning",
        ],
        "modes": ["online", "offline", "hybrid"],
        "adult_only": False,
    },
    {
        "id": "business_companies_trade", "name": "Businesses, Companies & Trade",
        "audiences": ["self_employed", "business_owners", "companies", "entrepreneurs"],
        "subcategories": [
            "sole_proprietorship", "partnership", "limited_liability_partnership",
            "private_limited_company", "public_company", "cooperative",
            "micro_business", "small_business", "medium_business", "large_enterprise",
            "multinational", "family_business", "home_based_business",
            "local_business", "franchise", "dealership", "distributorship",
            "wholesale", "retail", "manufacturing", "import_export", "trading",
            "ecommerce", "marketplace_seller", "subscription_business",
            "business_services", "business_transfer_acquisition",
        ],
        "modes": ["online", "offline", "hybrid"],
        "adult_only": False,
    },
    {
        "id": "entrepreneurship_startups", "name": "Entrepreneurship, Startups & Innovation",
        "audiences": ["entrepreneurs", "founders", "investors", "students", "business_owners"],
        "subcategories": [
            "business_ideas", "business_planning", "startup_formation",
            "validation_research", "incubators", "accelerators", "mentorship",
            "cofounder_matching", "fundraising", "angel_investment",
            "venture_capital", "bootstrapping", "crowdfunding",
            "intellectual_property", "product_development", "market_entry",
            "scaling_operations", "export_readiness", "social_enterprise",
            "rural_entrepreneurship", "women_entrepreneurship",
            "student_entrepreneurship", "franchise_entrepreneurship",
        ],
        "modes": ["online", "offline", "hybrid"],
        "adult_only": False,
    },
    {
        "id": "home_homemaker_care_economy", "name": "Home-Based Work, Homemakers & Care Economy",
        "audiences": ["homemakers", "caregivers", "parents", "self_employed"],
        "subcategories": [
            "home_based_enterprise", "home_food_business", "tailoring_handicrafts",
            "home_tuition", "online_freelancing", "remote_employment",
            "reselling", "crafts_and_artisan_work", "childcare_services",
            "eldercare_services", "caregiving_support", "domestic_services",
            "home_management_services", "community_support",
        ],
        "modes": ["online", "offline", "hybrid", "remote", "on_site"],
        "adult_only": False,
    },
    {
        "id": "industries_professional_services", "name": "Industries & Professional Services",
        "audiences": ["professionals", "business_owners", "companies", "individuals"],
        "subcategories": [
            "agriculture_forestry_fisheries", "mining_metals_minerals",
            "energy_utilities", "manufacturing_industrial", "construction_infrastructure",
            "real_estate_property", "retail_wholesale_distribution",
            "food_beverage_restaurants", "hospitality_tourism_travel",
            "transport_mobility_logistics", "automotive_ev_services",
            "technology_software_it", "ai_data_cloud_cybersecurity",
            "telecommunications", "finance_banking_insurance",
            "accounting_taxation", "legal_compliance", "consulting_advisory",
            "healthcare_life_sciences", "wellness_fitness", "beauty_personal_care",
            "fashion_textiles", "education_training", "media_entertainment",
            "arts_design_creative", "sports_recreation", "environment_sustainability",
            "water_marine", "aviation_aerospace", "security_safety",
            "government_public_services", "nonprofit_social_impact",
            "events_community_services", "repair_maintenance_home_services",
            "science_research_innovation", "supply_chain_warehousing",
        ],
        "modes": ["online", "offline", "hybrid"],
        "adult_only": False,
    },
    {
        "id": "family_relationships_community", "name": "Individuals, Couples, Family & Community",
        "audiences": ["individuals", "couples", "families", "relatives", "friends", "communities"],
        "subcategories": [
            "personal_development", "relationship_education", "couple_communication",
            "marriage_education", "parenting_education", "family_support",
            "caregiver_support", "elder_support", "community_groups",
            "friendship_communities", "life_skills", "conflict_resolution",
            "professional_counselling_directory", "wellbeing_education",
        ],
        "modes": ["online", "offline", "hybrid"],
        "adult_only": False,
    },
    {
        "id": "adult_18_plus_lawful_industry", "name": "Adult 18+ & Sexual Wellness Industry",
        "audiences": ["individuals", "couples", "business_owners", "companies"],
        "subcategories": [
            "sexual_wellness_education", "adult_health_information",
            "couples_intimacy_education", "lawful_adult_entertainment",
            "adult_content_creation", "adult_creator_platforms",
            "adult_studio_businesses", "adult_subscription_services",
            "adult_payment_compliance", "age_verification_services",
            "consent_and_safeguarding", "privacy_and_content_protection",
            "lawful_adult_retail", "adult_industry_professional_services",
        ],
        "modes": ["online", "offline", "hybrid"],
        "adult_only": True,
        "minimum_age": 18,
        "compliance_required": True,
    },
    {
        "id": "services_platforms_integrations", "name": "Services, Platforms & Technology Integrations",
        "audiences": ["individuals", "freelancers", "entrepreneurs", "business_owners", "companies"],
        "subcategories": [
            "cloud_hosting", "domains_dns", "website_platforms", "payments",
            "banking_fintech", "identity_verification", "communications",
            "crm_sales", "accounting_erp", "hr_payroll", "marketplaces",
            "booking_reservations", "delivery_logistics", "analytics_reporting",
            "automation_workflows", "developer_apis", "security_compliance",
            "customer_support", "document_signature", "ecommerce_integrations",
        ],
        "modes": ["online", "hybrid"],
        "adult_only": False,
    },
    {
        "id": "investment_finance_support", "name": "Finance, Investment & Business Support",
        "audiences": ["individuals", "entrepreneurs", "investors", "business_owners"],
        "subcategories": [
            "personal_finance_education", "business_finance", "loans_credit",
            "banking_services", "insurance", "tax_services", "accounting_audit",
            "investment_education", "capital_raising", "grants_subsidies",
            "government_schemes", "msme_support", "export_import_support",
            "business_valuation", "risk_management",
        ],
        "modes": ["online", "offline", "hybrid"],
        "adult_only": False,
    },
    {
        "id": "public_nonprofit_social_impact", "name": "Public Sector, Nonprofits & Social Impact",
        "audiences": ["individuals", "communities", "institutions", "nonprofits", "public_sector"],
        "subcategories": [
            "government_departments", "public_services", "municipal_services",
            "public_procurement", "nonprofit_organizations", "charities",
            "foundations", "community_development", "rural_development",
            "social_enterprise", "volunteering", "skill_development_programs",
            "environmental_initiatives", "public_information_services",
        ],
        "modes": ["online", "offline", "hybrid"],
        "adult_only": False,
    },
)

def list_domains(*, include_adult: bool = False) -> list[dict[str, Any]]:
    """Return a copy of the domain registry, excluding 18+ by default."""
    return [
        {**domain, "audiences": list(domain["audiences"]),
         "subcategories": list(domain["subcategories"]), "modes": list(domain["modes"])}
        for domain in GLOBAL_WORK_BUSINESS_DOMAINS
        if include_adult or not domain.get("adult_only", False)
    ]

def get_domain(domain_id: str, *, include_adult: bool = False) -> dict[str, Any] | None:
    """Return one domain by stable ID, respecting the adult exclusion default."""
    for domain in GLOBAL_WORK_BUSINESS_DOMAINS:
        if domain["id"] == domain_id and (include_adult or not domain.get("adult_only", False)):
            return {**domain, "audiences": list(domain["audiences"]),
                    "subcategories": list(domain["subcategories"]), "modes": list(domain["modes"])}
    return None

def search_subcategories(query: str, *, include_adult: bool = False) -> list[dict[str, str]]:
    """Case-insensitive search over domain names, IDs and subcategory IDs."""
    needle = query.strip().lower()
    if not needle:
        return []
    matches: list[dict[str, str]] = []
    for domain in GLOBAL_WORK_BUSINESS_DOMAINS:
        if domain.get("adult_only") and not include_adult:
            continue
        if needle in domain["id"] or needle in domain["name"].lower():
            matches.append({"domain_id": domain["id"], "domain_name": domain["name"],
                            "subcategory_id": "", "subcategory_name": ""})
        for subcategory in domain["subcategories"]:
            if needle in subcategory.replace("_", " ").lower():
                matches.append({"domain_id": domain["id"], "domain_name": domain["name"],
                                "subcategory_id": subcategory,
                                "subcategory_name": subcategory.replace("_", " ").title()})
    return matches

def validate_registry() -> dict[str, Any]:
    """Validate structural integrity; this does not verify real-world coverage."""
    ids = [domain["id"] for domain in GLOBAL_WORK_BUSINESS_DOMAINS]
    duplicate_ids = sorted({item for item in ids if ids.count(item) > 1})
    empty_domains = [domain["id"] for domain in GLOBAL_WORK_BUSINESS_DOMAINS
                     if not domain.get("subcategories")]
    duplicate_subcategories = {
        domain["id"]: sorted({item for item in domain["subcategories"]
                              if domain["subcategories"].count(item) > 1})
        for domain in GLOBAL_WORK_BUSINESS_DOMAINS
        if len(domain["subcategories"]) != len(set(domain["subcategories"]))
    }
    return {
        "registry_version": REGISTRY_VERSION,
        "registry_status": REGISTRY_STATUS,
        "domain_count": len(GLOBAL_WORK_BUSINESS_DOMAINS),
        "subcategory_count": sum(len(domain["subcategories"]) for domain in GLOBAL_WORK_BUSINESS_DOMAINS),
        "adult_domain_count": sum(bool(domain.get("adult_only")) for domain in GLOBAL_WORK_BUSINESS_DOMAINS),
        "duplicate_domain_ids": duplicate_ids,
        "empty_domains": empty_domains,
        "duplicate_subcategories": duplicate_subcategories,
        "structurally_valid": not (duplicate_ids or empty_domains or duplicate_subcategories),
        "live_data_verified": False,
        "worldwide_exhaustiveness_claimed": False,
    }
