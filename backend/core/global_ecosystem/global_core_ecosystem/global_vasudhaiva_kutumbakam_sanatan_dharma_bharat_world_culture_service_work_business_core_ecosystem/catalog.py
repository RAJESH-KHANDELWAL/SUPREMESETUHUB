"""Canonical culture, service, work and business capability catalogue.

This is a taxonomy/foundation catalogue, not a live provider, vacancy or job feed.
"""
from __future__ import annotations
from copy import deepcopy
from typing import Any

ECOSYSTEM_ID = "GLOBAL_VASUDHAIVA_KUTUMBAKAM_SANATAN_DHARMA_BHARAT_WORLD_CULTURE_SERVICE_WORK_BUSINESS"

_CATALOG: tuple[dict[str, Any], ...] = (
    {"id":"cultural_education","name":"Cultural Education & Learning","domain":"SERVICE","description":"Courses, workshops, learning programmes and cultural literacy.","work_types":["teaching","curriculum_design","training","research_assistance"],"business_types":["education_provider","training_institute","learning_platform"],"keywords":["education","learning","course","teaching","workshop","school"]},
    {"id":"language_translation","name":"Languages, Translation & Interpretation","domain":"SERVICE","description":"Translation, interpretation, language learning and localization across Bharat and world languages.","work_types":["translation","interpretation","transcription","localization","language_tutoring"],"business_types":["translation_agency","language_institute","localization_studio"],"keywords":["language","translation","interpretation","localization","transcription"]},
    {"id":"heritage_conservation","name":"Heritage Conservation & Restoration","domain":"SERVICE","description":"Documentation, conservation, restoration and responsible stewardship of cultural heritage.","work_types":["conservation","restoration","documentation","archival_research"],"business_types":["conservation_studio","heritage_consultancy","archive_service"],"keywords":["heritage","conservation","restoration","museum","archive","monument"]},
    {"id":"arts_crafts_design","name":"Arts, Crafts & Cultural Design","domain":"BUSINESS","description":"Traditional and contemporary arts, crafts, design, artisan production and creative commerce.","work_types":["craft_production","design","illustration","curation","quality_assurance"],"business_types":["artisan_enterprise","craft_cooperative","design_studio","gallery"],"keywords":["art","craft","handicraft","artisan","design","textile","weaving","pottery"]},
    {"id":"culture_tourism","name":"Cultural Tourism & Experiences","domain":"BUSINESS","description":"Responsible cultural travel, guided interpretation, heritage walks and community-led experiences.","work_types":["tour_guiding","itinerary_design","visitor_services","interpretation"],"business_types":["tour_operator","heritage_walk_operator","homestay","experience_provider"],"keywords":["tourism","travel","heritage walk","guide","experience","pilgrimage"]},
    {"id":"events_festivals","name":"Cultural Events & Festivals","domain":"SERVICE","description":"Planning, production and delivery of cultural events, festivals, exhibitions and performances.","work_types":["event_planning","production","stage_management","artist_coordination"],"business_types":["event_company","festival_organizer","production_house"],"keywords":["event","festival","exhibition","performance","concert","celebration"]},
    {"id":"research_publishing","name":"Cultural Research & Publishing","domain":"WORK","description":"Research, editing, publishing, oral-history documentation and source verification.","work_types":["research","editing","writing","fact_checking","oral_history"],"business_types":["research_collective","publishing_house","documentation_agency"],"keywords":["research","publishing","writing","editing","oral history","documentation"]},
    {"id":"media_content","name":"Cultural Media & Content Production","domain":"BUSINESS","description":"Documentaries, educational media, photography, audio, video and digital storytelling.","work_types":["filmmaking","photography","video_editing","podcasting","content_writing"],"business_types":["media_house","production_studio","digital_publisher"],"keywords":["media","documentary","film","photography","video","podcast","content"]},
    {"id":"traditional_knowledge","name":"Traditional Knowledge & Wellness Education","domain":"SERVICE","description":"Responsible education and documentation of traditional knowledge systems, with appropriate evidence and safety boundaries.","work_types":["knowledge_documentation","instruction","translation","research"],"business_types":["education_provider","research_institute","knowledge_publisher"],"keywords":["traditional knowledge","yoga","ayurveda","wellness","heritage knowledge"]},
    {"id":"community_cultural_orgs","name":"Cultural Communities & Organizations","domain":"BUSINESS","description":"Cultural associations, community organizations, cooperatives and non-profit initiatives.","work_types":["community_management","programme_coordination","fundraising","volunteer_management"],"business_types":["association","cooperative","nonprofit","community_enterprise"],"keywords":["community","association","cooperative","nonprofit","society","organization"]},
    {"id":"performing_arts","name":"Performing Arts & Artist Services","domain":"WORK","description":"Music, dance, theatre, performance practice, artist representation and production support.","work_types":["performing","choreography","music_instruction","artist_management","technical_crew"],"business_types":["artist_collective","performing_arts_company","talent_agency"],"keywords":["music","dance","theatre","artist","performing","choreography"]},
    {"id":"cultural_consulting","name":"Cultural Advisory & Intercultural Services","domain":"SERVICE","description":"Cultural advisory, intercultural communication, localization strategy and responsible engagement.","work_types":["consulting","training","research","facilitation"],"business_types":["consultancy","training_provider","advisory_firm"],"keywords":["consulting","advisory","intercultural","culture strategy","facilitation"]},
)

def list_capabilities(domain: str | None = None) -> list[dict[str, Any]]:
    selected = _CATALOG if domain is None else tuple(x for x in _CATALOG if x["domain"] == domain.upper())
    return deepcopy(list(selected))

def get_capability(capability_id: str) -> dict[str, Any] | None:
    item = next((x for x in _CATALOG if x["id"] == str(capability_id).strip().lower()), None)
    return deepcopy(item) if item else None

def catalog_status() -> dict[str, Any]:
    return {"ecosystem_id": ECOSYSTEM_ID, "capability_count": len(_CATALOG),
            "domains": ["SERVICE", "WORK", "BUSINESS"], "classification_only": True,
            "live_providers": False, "live_jobs_or_gigs": False}
