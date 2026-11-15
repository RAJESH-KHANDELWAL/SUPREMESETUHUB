"""Global cultural knowledge ecosystem domain package.

This package owns cultural knowledge taxonomies and source-aware domain
records. Runtime infrastructure (API, CORE, ENGINE, AI, DATABASE, STORAGE,
authentication and payments) remains in its separately owned architecture.
"""
from .domain import CULTURAL_PILLARS, CULTURAL_AREAS, CulturalResource
from .governance import assess_publication
from .knowledge import (
    KNOWLEDGE_ID,
    CORE_IDEA as VASUDHAIVA_CORE_IDEA,
    PRIMARY_TEXT as VASUDHAIVA_PRIMARY_TEXT,
    HISTORICAL_QUESTIONS as VASUDHAIVA_HISTORICAL_QUESTIONS,
    get_core_idea,
    get_primary_text,
    answer_historical_question,
    get_complete_knowledge,
    search_knowledge,
)

from . import (
    sanatan_dharma,
    bharat_sanskriti,
    bharat_civilization,
    world_cultures,
    world_civilizations,
    languages,
    heritage,
    festivals,
    arts_and_traditions,
    knowledge_and_education,
    oral_history,
    timeline,
    verification,
)

CULTURAL_DOMAINS = {
    "sanatan_dharma": sanatan_dharma,
    "bharat_sanskriti": bharat_sanskriti,
    "bharat_civilization": bharat_civilization,
    "world_cultures": world_cultures,
    "world_civilizations": world_civilizations,
    "languages": languages,
    "heritage": heritage,
    "festivals": festivals,
    "arts_and_traditions": arts_and_traditions,
    "knowledge_and_education": knowledge_and_education,
    "oral_history": oral_history,
    "timeline": timeline,
    "verification": verification,
}

ECOSYSTEM = {
    "id": "GLOBAL_VASUDHAIVA_KUTUMBAKAM_SANATAN_DHARMA_BHARAT_WORLD_CULTURE_ECOSYSTEM",
    "name": "GLOBAL VASUDHAIVA KUTUMBAKAM | SANATAN DHARMA | BHARAT SANSKRITI | WORLD CULTURE",
    "purpose": "Preserve, understand, learn and respectfully connect the cultures and knowledge traditions of Bharat and the world.",
    "pillars": tuple(CULTURAL_PILLARS),
    "cultural_domains": tuple(CULTURAL_DOMAINS),
    "foundational_knowledge": KNOWLEDGE_ID,
    "business_expression": "backend.global_ecosystem.global_bada_business_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_business_ecosystem",
}

__all__ = [
    "ECOSYSTEM", "CULTURAL_PILLARS", "CULTURAL_AREAS", "CulturalResource",
    "assess_publication", "KNOWLEDGE_ID", "VASUDHAIVA_CORE_IDEA",
    "VASUDHAIVA_PRIMARY_TEXT", "VASUDHAIVA_HISTORICAL_QUESTIONS",
    "get_core_idea", "get_primary_text", "answer_historical_question",
    "get_complete_knowledge", "search_knowledge", "CULTURAL_DOMAINS",
]
