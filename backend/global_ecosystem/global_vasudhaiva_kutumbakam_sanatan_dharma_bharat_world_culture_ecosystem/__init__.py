"""Cultural identity, heritage knowledge and respectful discovery domain."""

from .domain import CULTURAL_PILLARS, CULTURAL_AREAS, CulturalResource
from .governance import assess_publication

ECOSYSTEM = {
    "id": "GLOBAL_VASUDHAIVA_KUTUMBAKAM_SANATAN_DHARMA_BHARAT_WORLD_CULTURE_ECOSYSTEM",
    "name": "GLOBAL VASUDHAIVA KUTUMBAKAM | SANATAN DHARMA | BHARAT SANSKRITI | WORLD CULTURE",
    "purpose": "Preserve, understand, learn and respectfully connect the cultures and knowledge traditions of Bharat and the world.",
    "pillars": tuple(CULTURAL_PILLARS),
    "business_expression": "backend.global_ecosystem.global_bada_business_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_business_ecosystem",
}

__all__ = ["ECOSYSTEM", "CULTURAL_PILLARS", "CULTURAL_AREAS", "CulturalResource", "assess_publication"]
