"""Capability catalog for culture-related services, work and business."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
ECOSYSTEM_ID = "GLOBAL-VASUDHAIVA-KUTUMBAKAM-SANATAN-DHARMA-BHARAT-WORLD-CULTURE-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM"
PARENT_ECOSYSTEM_ID = "GLOBAL-VASUDHAIVA-KUTUMBAKAM-SANATAN-DHARMA-BHARAT-WORLD-CULTURE-CORE-ECOSYSTEM"
PARENT_PATH = "backend/core/global_ecosystem/global_core_ecosystem/global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_core_ecosystem/"
CAPABILITIES: tuple[dict[str, Any], ...] = (
 {"id":"cultural_education_learning","name":"Cultural Education & Learning","domains":["SERVICE","WORK","BUSINESS"],"work":["teaching","facilitation","curriculum_design","research_assistance"],"business":["courses","workshops","learning_programmes","education_services"]},
 {"id":"language_translation","name":"Language, Translation & Interpretation","domains":["SERVICE","WORK","BUSINESS"],"work":["translation","interpretation","transcription","localization","tutoring"],"business":["translation_services","language_learning","localization"]},
 {"id":"heritage_conservation","name":"Heritage, Archives & Conservation","domains":["SERVICE","WORK","BUSINESS"],"work":["archival_research","documentation","conservation","restoration"],"business":["heritage_consultancy","archive_services","conservation_studios"]},
 {"id":"arts_crafts_design","name":"Arts, Crafts & Design","domains":["WORK","BUSINESS"],"work":["craft","art","design","production","curation"],"business":["artisan_enterprises","cooperatives","studios","galleries"]},
 {"id":"cultural_tourism_experiences","name":"Cultural Tourism & Experiences","domains":["SERVICE","WORK","BUSINESS"],"work":["guiding","interpretation","visitor_support","itinerary_design"],"business":["tours","heritage_walks","community_experiences","homestays"]},
 {"id":"festivals_events","name":"Festivals, Events & Programs","domains":["SERVICE","WORK","BUSINESS"],"work":["event_planning","production","coordination","performing"],"business":["event_services","festival_operations","cultural_programming"]},
 {"id":"research_publishing","name":"Research, Documentation & Publishing","domains":["SERVICE","WORK","BUSINESS"],"work":["research","editing","writing","documentation"],"business":["publishing","research_services","editorial_services"]},
 {"id":"media_content","name":"Cultural Media & Content","domains":["SERVICE","WORK","BUSINESS"],"work":["video","audio","photography","writing","editing"],"business":["production","media_studios","content_services"]},
 {"id":"community_cultural_orgs","name":"Community & Cultural Organizations","domains":["SERVICE","WORK","BUSINESS"],"work":["community_programs","coordination","volunteering","administration"],"business":["organizations","associations","social_enterprises"]},
 {"id":"performing_arts","name":"Performing Arts","domains":["WORK","BUSINESS"],"work":["music","dance","theatre","performance","production"],"business":["performing_groups","venues","production_services"]},
 {"id":"cultural_advisory","name":"Cultural Advisory & Intercultural Services","domains":["SERVICE","WORK","BUSINESS"],"work":["advisory","facilitation","consulting","protocol"],"business":["consultancies","advisory_services","cross_cultural_training"]},
 {"id":"traditional_knowledge_education","name":"Traditional Knowledge & Cultural Wellness Education","domains":["SERVICE","WORK","BUSINESS"],"work":["education","documentation","facilitation"],"business":["educational_programs","cultural_wellness_education"]},
)
def list_capabilities(domain: str | None = None) -> list[dict[str, Any]]:
 d = domain.upper() if domain else None
 return [deepcopy(x) for x in CAPABILITIES if d is None or d in x["domains"]]
def get_capability(capability_id: str) -> dict[str, Any] | None:
 for item in CAPABILITIES:
  if item["id"] == capability_id: return deepcopy(item)
 return None
