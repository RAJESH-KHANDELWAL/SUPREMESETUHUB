"""Extensible Bharat-to-global domain taxonomy for the Global Ecosystem.

Entries are scope definitions and planned namespace identifiers. They do not
assert that a corresponding package, provider integration, or live service exists.
"""

DOMAIN_TAXONOMY = (
    {"id": "global_education_ecosystem", "name": "Education & Knowledge", "description": "Schools, universities, vocational training, tutoring, research libraries, learning platforms, assessment, credentials and lifelong learning."},
    {"id": "global_finance_ecosystem", "name": "Finance & Fintech", "description": "Personal and business finance, accounting, lending, investment information, insurance, risk and financial technology."},
    {"id": "global_health_ecosystem", "name": "Health & Healthcare", "description": "Healthcare delivery, hospitals, clinical information systems, public health, diagnostics, medical devices, wellness and health research."},
    {"id": "global_relationship_ecosystem", "name": "Relationships & Family", "description": "Dating, marriage, family support, communication, relationship education, counselling directories and consent-centred intimacy information."},
    {"id": "global_science_research_ecosystem", "name": "Science & Research", "description": "Scientific disciplines, research institutions, laboratories, datasets, reproducibility, scholarly publishing and research infrastructure."},
    {"id": "global_agriculture_ecosystem", "name": "Agriculture & Farming", "description": "Crop production, soil, seeds, irrigation, farm machinery, livestock, fisheries, agri-fintech and agricultural supply chains."},
    {"id": "global_food_ecosystem", "name": "Food & Beverage", "description": "Food production, processing, safety, nutrition, restaurants, grocery, distribution, traceability and food-service technology."},
    {"id": "global_transport_ecosystem", "name": "Transport & Mobility", "description": "Road, rail, aviation, maritime, public transit, vehicles, mobility services, traffic systems and transport technology."},
    {"id": "global_logistics_ecosystem", "name": "Logistics & Supply Chain", "description": "Warehousing, freight, courier, fulfilment, inventory, procurement, customs, cross-border trade and supply-chain visibility."},
    {"id": "global_government_ecosystem", "name": "Government & Public Services", "description": "Public administration, civic technology, digital public infrastructure, citizen services, public records and service delivery."},
    {"id": "global_legal_ecosystem", "name": "Law & Legal Services", "description": "Legal research, law firms, courts, contracts, dispute resolution, regulatory compliance, legal operations and justice technology."},
    {"id": "global_entertainment_ecosystem", "name": "Entertainment", "description": "Film, television, OTT, live events, talent, ticketing, creator businesses and entertainment distribution."},
    {"id": "global_media_ecosystem", "name": "Media & Publishing", "description": "News, journalism, books, magazines, digital publishing, broadcasting, creator media and content distribution."},
    {"id": "global_sports_ecosystem", "name": "Sports & Fitness", "description": "Professional and community sports, leagues, coaching, facilities, sports science, fitness services and sports technology."},
    {"id": "global_fashion_lifestyle_ecosystem", "name": "Fashion & Lifestyle", "description": "Apparel, textiles, footwear, beauty, cosmetics, personal care, accessories, luxury and lifestyle commerce."},
    {"id": "global_tourism_ecosystem", "name": "Tourism & Travel", "description": "Destinations, travel planning, tours, attractions, travel services, visitor information and responsible tourism."},
    {"id": "global_hospitality_ecosystem", "name": "Hospitality", "description": "Hotels, accommodation, restaurants, catering, guest services, reservations and hospitality operations."},
    {"id": "global_energy_ecosystem", "name": "Energy & Power", "description": "Electricity, grids, generation, renewables, storage, energy markets and efficiency."},
    {"id": "global_environment_ecosystem", "name": "Environment & Climate", "description": "Climate, conservation, biodiversity, pollution, environmental monitoring, sustainability and circular economy."},
    {"id": "global_robotics_ecosystem", "name": "Robotics & Automation", "description": "Industrial, service and research robotics, automation, control systems, sensors, actuation and human-robot interaction."},
    {"id": "global_quantum_computing_ecosystem", "name": "Quantum Computing", "description": "Quantum hardware, algorithms, simulation, software tooling, networking research and post-quantum technology references."},
    {"id": "global_accessibility_ecosystem", "name": "Accessibility & Assistive Technology", "description": "Digital accessibility, assistive devices, inclusive design, captions, screen readers, language access and adaptive technologies."},
    {"id": "global_identity_ecosystem", "name": "Identity & Trust", "description": "Digital identity, verification, credentials, consent records, trust frameworks, fraud prevention and privacy-preserving identity."},
    {"id": "global_defence_ecosystem", "name": "Defence & Emergency Resilience", "description": "Defence-related public information, civil protection, disaster response, emergency communications, resilience and lawful safety research."},
    {"id": "global_manufacturing_industry_ecosystem", "name": "Manufacturing & Industry", "description": "Industrial production, factories, materials, quality systems, industrial IoT, maintenance, engineering and Industry 4.0."},
    {"id": "global_gaming_esports_ecosystem", "name": "Gaming & Esports", "description": "Video games, game development, publishing, esports, streaming, player communities and interactive entertainment."},
    {"id": "global_career_hr_ecosystem", "name": "Careers & Human Resources", "description": "Employment, recruitment, workforce planning, payroll references, professional development, skills and workplace technology."},
    {"id": "global_space_ecosystem", "name": "Space & Aerospace", "description": "Space science, satellites, launch systems, Earth observation, aerospace engineering and space applications."},
    {"id": "global_water_ecosystem", "name": "Water & Sanitation", "description": "Water supply, treatment, wastewater, sanitation, irrigation infrastructure, hydrology and water-quality monitoring."},
)

GEOGRAPHIC_SCOPES = (
    "bharat_india",
    "south_asia",
    "asia_pacific",
    "middle_east",
    "africa",
    "europe",
    "north_america",
    "latin_america_caribbean",
    "oceania",
    "global_cross_border",
)

MATURITY_LEVELS = (
    "basic_normal",
    "standard",
    "professional",
    "advanced",
    "expert",
    "enterprise_industrial",
    "research",
    "frontier",
    "supreme_long_horizon",
)

IMPLEMENTATION_STATUSES = (
    "SCOPE_DEFINED",
    "CATALOGED",
    "ROADMAP",
    "RESEARCH",
    "POLICY_GATED_SCOPE",
    "IMPLEMENTED",
    "INTEGRATED",
    "PRODUCTION_READY",
)


def get_domain(domain_id: str):
    """Return a matching domain definition, or None when it is not in this expansion."""
    return next((item for item in DOMAIN_TAXONOMY if item["id"] == domain_id), None)


__all__ = [
    "DOMAIN_TAXONOMY",
    "GEOGRAPHIC_SCOPES",
    "MATURITY_LEVELS",
    "IMPLEMENTATION_STATUSES",
    "get_domain",
]
