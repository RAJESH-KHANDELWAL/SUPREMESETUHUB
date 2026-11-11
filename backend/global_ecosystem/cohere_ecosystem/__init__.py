"""Cohere global ecosystem domain package.

Owns provider-level business/domain taxonomy, capability discovery, request
validation and safe request planning. API transport, AI runtime, ENGINE, CORE,
DATABASE, credentials and authorization enforcement remain separate layers.
"""
from .catalog import COHERE_PROVIDER, COHERE_PRODUCTS, COHERE_CAPABILITIES
from .service import CohereEcosystemService

__all__ = [
    "COHERE_PROVIDER",
    "COHERE_PRODUCTS",
    "COHERE_CAPABILITIES",
    "CohereEcosystemService",
]
