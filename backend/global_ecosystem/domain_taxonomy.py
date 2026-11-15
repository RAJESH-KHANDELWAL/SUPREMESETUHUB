"""Extensible Bharat-to-global domain taxonomy and query service.

This module owns domain metadata and read-only catalogue operations only.
It does not implement domain business logic or claim that a provider/service
is integrated. Runtime ownership remains in canonical CORE/API/ENGINE/
DATABASE/SECURITY layers.
"""
from __future__ import annotations

import re
from typing import Any

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
    "bharat_india", "south_asia", "asia_pacific", "middle_east", "africa",
    "europe", "north_america", "latin_america_caribbean", "oceania",
    "global_cross_border",
)
MATURITY_LEVELS = (
    "basic_normal", "standard", "professional", "advanced", "expert",
    "enterprise_industrial", "research", "frontier", "supreme_long_horizon",
)
IMPLEMENTATION_STATUSES = (
    "SCOPE_DEFINED", "CATALOGED", "ROADMAP", "RESEARCH",
    "POLICY_GATED_SCOPE", "IMPLEMENTED", "INTEGRATED", "PRODUCTION_READY",
)
_REQUIRED_FIELDS = ("id", "name", "description")
_ID_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")


def _copy_domain(item: dict[str, str]) -> dict[str, str]:
    """Return a detached record so callers cannot mutate the source catalogue."""
    return dict(item)


def list_domains() -> list[dict[str, str]]:
    """Return all 29 domain definitions in their stable catalogue order."""
    return [_copy_domain(item) for item in DOMAIN_TAXONOMY]


def get_domain(domain_id: str) -> dict[str, str] | None:
    """Look up a domain by stable ID; matching is whitespace/case insensitive."""
    key = str(domain_id or "").strip().casefold()
    if not key:
        return None
    for item in DOMAIN_TAXONOMY:
        if item["id"].casefold() == key:
            return _copy_domain(item)
    return None


def get_domain_by_name(name: str) -> dict[str, str] | None:
    """Look up a domain by its display name, ignoring case and outer whitespace."""
    key = str(name or "").strip().casefold()
    if not key:
        return None
    for item in DOMAIN_TAXONOMY:
        if item["name"].casefold() == key:
            return _copy_domain(item)
    return None


def search_domains(query: str) -> list[dict[str, str]]:
    """Search domain IDs, names and descriptions using case-insensitive matching."""
    needle = str(query or "").strip().casefold()
    if not needle:
        return []
    return [
        _copy_domain(item)
        for item in DOMAIN_TAXONOMY
        if needle in " ".join((item["id"], item["name"], item["description"])).casefold()
    ]


def get_domain_catalog() -> dict[str, Any]:
    """Return catalogue data and scope facets without implying runtime readiness."""
    return {
        "success": True,
        "catalogue": "bharat_to_global_domain_taxonomy",
        "registry_status": "taxonomy_only",
        "count": len(DOMAIN_TAXONOMY),
        "domains": list_domains(),
        "geographic_scopes": list(GEOGRAPHIC_SCOPES),
        "maturity_levels": list(MATURITY_LEVELS),
        "implementation_statuses": list(IMPLEMENTATION_STATUSES),
    }


def validate_domain_taxonomy() -> dict[str, Any]:
    """Run structural integrity checks on IDs and required domain metadata."""
    ids = [str(item.get("id", "")) for item in DOMAIN_TAXONOMY]
    duplicate_ids = sorted({value for value in ids if ids.count(value) > 1})
    missing_fields = [
        {"index": index, "fields": [field for field in _REQUIRED_FIELDS if not item.get(field)]}
        for index, item in enumerate(DOMAIN_TAXONOMY)
        if any(not item.get(field) for field in _REQUIRED_FIELDS)
    ]
    invalid_ids = sorted(value for value in ids if not _ID_PATTERN.fullmatch(value))
    checks = {
        "unique_domain_ids": not duplicate_ids,
        "required_fields_present": not missing_fields,
        "domain_ids_follow_slug_contract": not invalid_ids,
        "geographic_scopes_unique": len(GEOGRAPHIC_SCOPES) == len(set(GEOGRAPHIC_SCOPES)),
        "maturity_levels_unique": len(MATURITY_LEVELS) == len(set(MATURITY_LEVELS)),
        "implementation_statuses_unique": len(IMPLEMENTATION_STATUSES) == len(set(IMPLEMENTATION_STATUSES)),
    }
    return {
        "structurally_valid": all(checks.values()),
        "registry_status": "taxonomy_only",
        "domain_count": len(DOMAIN_TAXONOMY),
        "checks": checks,
        "issues": {
            "duplicate_ids": duplicate_ids,
            "missing_fields": missing_fields,
            "invalid_ids": invalid_ids,
        },
    }


__all__ = [
    "DOMAIN_TAXONOMY", "GEOGRAPHIC_SCOPES", "MATURITY_LEVELS",
    "IMPLEMENTATION_STATUSES", "list_domains", "get_domain",
    "get_domain_by_name", "search_domains", "get_domain_catalog",
    "validate_domain_taxonomy",
]
