"""Canonical domain taxonomy shared by global and business layers."""
from __future__ import annotations

DOMAINS = (
    {"domain_id": "agriculture_and_farming", "name": "Agriculture and Farming", "description": "Crops, horticulture, agroforestry, farm systems and primary production.", "layer": "GLOBAL_CORE"},
    {"domain_id": "food_systems", "name": "Food Systems", "description": "Food production, nutrition, processing, safety, distribution and resilience.", "layer": "GLOBAL_CORE"},
    {"domain_id": "natural_resources", "name": "Natural Resources", "description": "Land, soil, forests, biodiversity, minerals and responsible resource stewardship.", "layer": "GLOBAL_CORE"},
    {"domain_id": "water_and_irrigation", "name": "Water and Irrigation", "description": "Water resources, irrigation, watershed management and conservation.", "layer": "GLOBAL_CORE"},
    {"domain_id": "human_and_communities", "name": "Human and Communities", "description": "People, livelihoods, rural communities, skills, rights and inclusive development.", "layer": "GLOBAL_CORE"},
    {"domain_id": "animal_and_livestock", "name": "Animal and Livestock", "description": "Animal husbandry, livestock health, welfare, feed and responsible production.", "layer": "GLOBAL_CORE"},
    {"domain_id": "fisheries_and_aquaculture", "name": "Fisheries and Aquaculture", "description": "Inland and marine fisheries, aquaculture and aquatic ecosystem stewardship.", "layer": "GLOBAL_CORE"},
    {"domain_id": "climate_and_environment", "name": "Climate and Environment", "description": "Climate resilience, adaptation, emissions, ecosystem restoration and environmental safeguards.", "layer": "GLOBAL_CORE"},
    {"domain_id": "research_and_knowledge", "name": "Research and Knowledge", "description": "Agricultural science, extension, education, data and knowledge exchange.", "layer": "GLOBAL_CORE"},
    {"domain_id": "technology_and_innovation", "name": "Technology and Innovation", "description": "Agri-tech, machinery, sensors, AI, biotechnology and digital public infrastructure.", "layer": "GLOBAL_CORE"},
    {"domain_id": "trade_and_market_access", "name": "Trade and Market Access", "description": "Standards, traceability, market access and cross-border food and resource trade.", "layer": "GLOBAL_CORE"},
    {"domain_id": "governance_and_standards", "name": "Governance and Standards", "description": "Policy, public institutions, quality standards, compliance and ethical safeguards.", "layer": "GLOBAL_CORE"},
)

def list_domains() -> list[dict[str, str]]:
    return [dict(item) for item in DOMAINS]

def get_domain(domain_id: str) -> dict[str, str] | None:
    key = domain_id.strip().casefold()
    return next((dict(item) for item in DOMAINS if item["domain_id"].casefold() == key), None)

def domain_summary() -> dict[str, object]:
    return {"count": len(DOMAINS), "domains": list_domains()}
