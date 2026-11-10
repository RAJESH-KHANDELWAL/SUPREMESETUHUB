"""Shared profiles for the 29 expanded Bharat-to-global domain packages."""
from __future__ import annotations

from copy import deepcopy

GEOGRAPHIC_SCOPES = (
    "bharat_india", "south_asia", "asia_pacific", "middle_east", "africa",
    "europe", "north_america", "latin_america_caribbean", "oceania", "global_cross_border",
)
MATURITY_LEVELS = (
    "basic_normal", "standard", "professional", "advanced", "expert",
    "enterprise_industrial", "research", "frontier", "supreme_long_horizon",
)
DOMAIN_PROFILES = {
    "global_developer_ecosystem": {
        "id": "global_developer_ecosystem",
        "name": "Global Developer & Software Ecosystem",
        "description": "Bharat-to-global software and digital product development: websites, apps, AI, APIs, platforms, cloud-native systems, open source, enterprise engineering and lawful adult-only products.",
        "categories": [
            "web_development", "mobile_and_desktop_apps", "backend_and_api_engineering",
            "frontend_and_design_systems", "ai_and_machine_learning", "data_and_analytics",
            "cloud_and_devops", "cybersecurity_and_privacy", "open_source_and_developer_tools",
            "enterprise_and_industry_software", "game_and_interactive_development",
            "adult_only_content_platforms", "age_assurance_and_consent", "creator_and_subscription_platforms",
            "content_moderation_and_safety", "accessibility_and_localisation",
            "testing_and_quality_engineering", "systems_and_embedded_development",
            "blockchain_and_distributed_apps", "research_and_frontier_computing"
        ]
    },
    "global_education_ecosystem": {
        "id": "global_education_ecosystem",
        "name": "Education & Knowledge",
        "description": "Schools, universities, vocational training, tutoring, research libraries, learning platforms, assessment, credentials and lifelong learning.",
        "categories": [
            "schools",
            "universities",
            "vocational_training",
            "tutoring",
            "research_libraries",
            "learning_platforms",
            "assessment",
            "credentials",
            "lifelong_learning"
        ]
    },
    "global_finance_ecosystem": {
        "id": "global_finance_ecosystem",
        "name": "Finance & Fintech",
        "description": "Personal and business finance, accounting, lending, investment information, insurance, risk and financial technology.",
        "categories": [
            "personal_finance",
            "business_finance",
            "accounting",
            "lending",
            "investment_information",
            "insurance",
            "risk",
            "fintech"
        ]
    },
    "global_health_ecosystem": {
        "id": "global_health_ecosystem",
        "name": "Health & Healthcare",
        "description": "Healthcare delivery, hospitals, clinical information systems, public health, diagnostics, medical devices, wellness and health research.",
        "categories": [
            "healthcare_delivery",
            "hospitals",
            "clinical_information_systems",
            "public_health",
            "diagnostics",
            "medical_devices",
            "wellness",
            "health_research"
        ]
    },
    "global_relationship_ecosystem": {
        "id": "global_relationship_ecosystem",
        "name": "Relationships & Family",
        "description": "Dating, marriage, family support, communication, relationship education, counselling directories and consent-centred intimacy information.",
        "categories": [
            "dating",
            "marriage",
            "family_support",
            "communication",
            "relationship_education",
            "counselling_directories",
            "consent_centred_intimacy"
        ]
    },
    "global_science_research_ecosystem": {
        "id": "global_science_research_ecosystem",
        "name": "Science & Research",
        "description": "Scientific disciplines, research institutions, laboratories, datasets, reproducibility, scholarly publishing and research infrastructure.",
        "categories": [
            "scientific_disciplines",
            "research_institutions",
            "laboratories",
            "datasets",
            "reproducibility",
            "scholarly_publishing",
            "research_infrastructure"
        ]
    },
    "global_agriculture_ecosystem": {
        "id": "global_agriculture_ecosystem",
        "name": "Agriculture & Farming",
        "description": "Crop production, soil, seeds, irrigation, farm machinery, livestock, fisheries, agri-fintech and agricultural supply chains.",
        "categories": [
            "crop_production",
            "soil",
            "seeds",
            "irrigation",
            "farm_machinery",
            "livestock",
            "fisheries",
            "agri_fintech",
            "agricultural_supply_chains"
        ]
    },
    "global_food_ecosystem": {
        "id": "global_food_ecosystem",
        "name": "Food & Beverage",
        "description": "Food production, processing, safety, nutrition, restaurants, grocery, distribution, traceability and food-service technology.",
        "categories": [
            "food_production",
            "food_processing",
            "food_safety",
            "nutrition",
            "restaurants",
            "grocery",
            "distribution",
            "traceability",
            "food_service_technology"
        ]
    },
    "global_transport_ecosystem": {
        "id": "global_transport_ecosystem",
        "name": "Transport & Mobility",
        "description": "Road, rail, aviation, maritime, public transit, vehicles, mobility services, traffic systems and transport technology.",
        "categories": [
            "road",
            "rail",
            "aviation",
            "maritime",
            "public_transit",
            "vehicles",
            "mobility_services",
            "traffic_systems",
            "transport_technology"
        ]
    },
    "global_logistics_ecosystem": {
        "id": "global_logistics_ecosystem",
        "name": "Logistics & Supply Chain",
        "description": "Warehousing, freight, courier, fulfilment, inventory, procurement, customs, cross-border trade and supply-chain visibility.",
        "categories": [
            "warehousing",
            "freight",
            "courier",
            "fulfilment",
            "inventory",
            "procurement",
            "customs",
            "cross_border_trade",
            "supply_chain_visibility"
        ]
    },
    "global_government_ecosystem": {
        "id": "global_government_ecosystem",
        "name": "Government & Public Services",
        "description": "Public administration, civic technology, digital public infrastructure, citizen services, public records and service delivery.",
        "categories": [
            "public_administration",
            "civic_technology",
            "digital_public_infrastructure",
            "citizen_services",
            "public_records",
            "service_delivery"
        ]
    },
    "global_legal_ecosystem": {
        "id": "global_legal_ecosystem",
        "name": "Law & Legal Services",
        "description": "Legal research, law firms, courts, contracts, dispute resolution, regulatory compliance, legal operations and justice technology.",
        "categories": [
            "legal_research",
            "law_firms",
            "courts",
            "contracts",
            "dispute_resolution",
            "regulatory_compliance",
            "legal_operations",
            "justice_technology"
        ]
    },
    "global_entertainment_ecosystem": {
        "id": "global_entertainment_ecosystem",
        "name": "Entertainment",
        "description": "Film, television, OTT, live events, talent, ticketing, creator businesses and entertainment distribution.",
        "categories": [
            "film",
            "television",
            "ott",
            "live_events",
            "talent",
            "ticketing",
            "creator_businesses",
            "entertainment_distribution"
        ]
    },
    "global_media_ecosystem": {
        "id": "global_media_ecosystem",
        "name": "Media & Publishing",
        "description": "News, journalism, books, magazines, digital publishing, broadcasting, creator media and content distribution.",
        "categories": [
            "news",
            "journalism",
            "books",
            "magazines",
            "digital_publishing",
            "broadcasting",
            "creator_media",
            "content_distribution"
        ]
    },
    "global_sports_ecosystem": {
        "id": "global_sports_ecosystem",
        "name": "Sports & Fitness",
        "description": "Professional and community sports, leagues, coaching, facilities, sports science, fitness services and sports technology.",
        "categories": [
            "professional_sports",
            "community_sports",
            "leagues",
            "coaching",
            "facilities",
            "sports_science",
            "fitness_services",
            "sports_technology"
        ]
    },
    "global_fashion_lifestyle_ecosystem": {
        "id": "global_fashion_lifestyle_ecosystem",
        "name": "Fashion & Lifestyle",
        "description": "Apparel, textiles, footwear, beauty, cosmetics, personal care, accessories, luxury and lifestyle commerce.",
        "categories": [
            "apparel",
            "textiles",
            "footwear",
            "beauty",
            "cosmetics",
            "personal_care",
            "accessories",
            "luxury",
            "lifestyle_commerce"
        ]
    },
    "global_tourism_ecosystem": {
        "id": "global_tourism_ecosystem",
        "name": "Tourism & Travel",
        "description": "Destinations, travel planning, tours, attractions, travel services, visitor information and responsible tourism.",
        "categories": [
            "destinations",
            "travel_planning",
            "tours",
            "attractions",
            "travel_services",
            "visitor_information",
            "responsible_tourism"
        ]
    },
    "global_hospitality_ecosystem": {
        "id": "global_hospitality_ecosystem",
        "name": "Hospitality",
        "description": "Hotels, accommodation, restaurants, catering, guest services, reservations and hospitality operations.",
        "categories": [
            "hotels",
            "accommodation",
            "restaurants",
            "catering",
            "guest_services",
            "reservations",
            "hospitality_operations"
        ]
    },
    "global_energy_ecosystem": {
        "id": "global_energy_ecosystem",
        "name": "Energy & Power",
        "description": "Electricity, grids, generation, renewables, storage, energy markets and efficiency.",
        "categories": [
            "electricity",
            "grids",
            "generation",
            "renewables",
            "energy_storage",
            "energy_markets",
            "efficiency"
        ]
    },
    "global_environment_ecosystem": {
        "id": "global_environment_ecosystem",
        "name": "Environment & Climate",
        "description": "Climate, conservation, biodiversity, pollution, environmental monitoring, sustainability and circular economy.",
        "categories": [
            "climate",
            "conservation",
            "biodiversity",
            "pollution",
            "environmental_monitoring",
            "sustainability",
            "circular_economy"
        ]
    },
    "global_robotics_ecosystem": {
        "id": "global_robotics_ecosystem",
        "name": "Robotics & Automation",
        "description": "Industrial, service and research robotics, automation, control systems, sensors, actuation and human-robot interaction.",
        "categories": [
            "industrial_robotics",
            "service_robotics",
            "research_robotics",
            "automation",
            "control_systems",
            "sensors",
            "actuation",
            "human_robot_interaction"
        ]
    },
    "global_quantum_computing_ecosystem": {
        "id": "global_quantum_computing_ecosystem",
        "name": "Quantum Computing",
        "description": "Quantum hardware, algorithms, simulation, software tooling, networking research and post-quantum technology references.",
        "categories": [
            "quantum_hardware",
            "quantum_algorithms",
            "simulation",
            "software_tooling",
            "networking_research",
            "post_quantum_technology"
        ]
    },
    "global_accessibility_ecosystem": {
        "id": "global_accessibility_ecosystem",
        "name": "Accessibility & Assistive Technology",
        "description": "Digital accessibility, assistive devices, inclusive design, captions, screen readers, language access and adaptive technologies.",
        "categories": [
            "digital_accessibility",
            "assistive_devices",
            "inclusive_design",
            "captions",
            "screen_readers",
            "language_access",
            "adaptive_technologies"
        ]
    },
    "global_identity_ecosystem": {
        "id": "global_identity_ecosystem",
        "name": "Identity & Trust",
        "description": "Digital identity, verification, credentials, consent records, trust frameworks, fraud prevention and privacy-preserving identity.",
        "categories": [
            "digital_identity",
            "verification",
            "credentials",
            "consent_records",
            "trust_frameworks",
            "fraud_prevention",
            "privacy_preserving_identity"
        ]
    },
    "global_defence_ecosystem": {
        "id": "global_defence_ecosystem",
        "name": "Defence & Emergency Resilience",
        "description": "Defence-related public information, civil protection, disaster response, emergency communications, resilience and lawful safety research.",
        "categories": [
            "defence_public_information",
            "civil_protection",
            "disaster_response",
            "emergency_communications",
            "resilience",
            "lawful_safety_research"
        ]
    },
    "global_manufacturing_industry_ecosystem": {
        "id": "global_manufacturing_industry_ecosystem",
        "name": "Manufacturing & Industry",
        "description": "Industrial production, factories, materials, quality systems, industrial IoT, maintenance, engineering and Industry 4.0.",
        "categories": [
            "industrial_production",
            "factories",
            "materials",
            "quality_systems",
            "industrial_iot",
            "maintenance",
            "engineering",
            "industry_4_0"
        ]
    },
    "global_gaming_esports_ecosystem": {
        "id": "global_gaming_esports_ecosystem",
        "name": "Gaming & Esports",
        "description": "Video games, game development, publishing, esports, streaming, player communities and interactive entertainment.",
        "categories": [
            "video_games",
            "game_development",
            "publishing",
            "esports",
            "streaming",
            "player_communities",
            "interactive_entertainment"
        ]
    },
    "global_career_hr_ecosystem": {
        "id": "global_career_hr_ecosystem",
        "name": "Careers & Human Resources",
        "description": "Employment, recruitment, workforce planning, payroll references, professional development, skills and workplace technology.",
        "categories": [
            "employment",
            "recruitment",
            "workforce_planning",
            "payroll_references",
            "professional_development",
            "skills",
            "workplace_technology"
        ]
    },
    "global_space_ecosystem": {
        "id": "global_space_ecosystem",
        "name": "Space & Aerospace",
        "description": "Space science, satellites, launch systems, Earth observation, aerospace engineering and space applications.",
        "categories": [
            "space_science",
            "satellites",
            "launch_systems",
            "earth_observation",
            "aerospace_engineering",
            "space_applications"
        ]
    },
    "global_water_ecosystem": {
        "id": "global_water_ecosystem",
        "name": "Water & Sanitation",
        "description": "Water supply, treatment, wastewater, sanitation, irrigation infrastructure, hydrology and water-quality monitoring.",
        "categories": [
            "water_supply",
            "water_treatment",
            "wastewater",
            "sanitation",
            "irrigation_infrastructure",
            "hydrology",
            "water_quality_monitoring"
        ]
    }
}


def get_domain_profile(domain_id: str) -> dict | None:
    """Return domain metadata without implying that runtime capabilities exist."""
    profile = DOMAIN_PROFILES.get(str(domain_id or "").strip().casefold())
    if profile is None:
        return None
    result = deepcopy(profile)
    result["geographic_scopes"] = list(GEOGRAPHIC_SCOPES)
    result["maturity_levels"] = list(MATURITY_LEVELS)
    result["implementation_status"] = "SCOPE_DEFINED"
    result["runtime_owner"] = "CORE/API/ENGINE/DATABASE/SECURITY"
    return result


__all__ = ["DOMAIN_PROFILES", "GEOGRAPHIC_SCOPES", "MATURITY_LEVELS", "get_domain_profile"]
