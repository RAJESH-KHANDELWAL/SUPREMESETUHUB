"""Cultural identity, heritage knowledge and respectful discovery domain."""

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

ECOSYSTEM = {
    "id": "GLOBAL_VASUDHAIVA_KUTUMBAKAM_SANATAN_DHARMA_BHARAT_WORLD_CULTURE_ECOSYSTEM",
    "name": "GLOBAL VASUDHAIVA KUTUMBAKAM | SANATAN DHARMA | BHARAT SANSKRITI | WORLD CULTURE",
    "purpose": "Preserve, understand, learn and respectfully connect the cultures and knowledge traditions of Bharat and the world.",
    "pillars": tuple(CULTURAL_PILLARS),
    "business_expression": "backend.global_ecosystem.global_bada_business_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_business_ecosystem",
    "foundational_knowledge": KNOWLEDGE_ID,
}

__all__ = [
    "ECOSYSTEM", "CULTURAL_PILLARS", "CULTURAL_AREAS", "CulturalResource",
    "assess_publication", "KNOWLEDGE_ID", "VASUDHAIVA_CORE_IDEA",
    "VASUDHAIVA_PRIMARY_TEXT", "VASUDHAIVA_HISTORICAL_QUESTIONS",
    "get_core_idea", "get_primary_text", "answer_historical_question",
    "get_complete_knowledge", "search_knowledge",
]
