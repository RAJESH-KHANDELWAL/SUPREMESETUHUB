"""Cultural business domain: ethical offerings, providers and market organization."""

from .business_domain import BUSINESS_DOMAINS, BusinessOffering, ProviderProfile
from .governance import assess_listing

ECOSYSTEM = {
    "id": "GLOBAL_VASUDHAIVA_KUTUMBAKAM_SANATAN_DHARMA_BHARAT_WORLD_CULTURE_BUSINESS_ECOSYSTEM",
    "name": "GLOBAL VASUDHAIVA KUTUMBAKAM | SANATAN DHARMA | BHARAT SANSKRITI | WORLD CULTURE BUSINESS",
    "parent": "GLOBAL_BADA_BUSINESS_ECOSYSTEM",
    "role": "Organize ethical businesses, services, products, learning, experiences and partnerships connected with cultural heritage.",
    "cultural_domain": "GLOBAL_VASUDHAIVA_KUTUMBAKAM_SANATAN_DHARMA_BHARAT_WORLD_CULTURE_ECOSYSTEM",
}

__all__ = ["ECOSYSTEM", "BUSINESS_DOMAINS", "BusinessOffering", "ProviderProfile", "assess_listing"]
