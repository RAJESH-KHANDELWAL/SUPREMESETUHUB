"""Atlassian global ecosystem domain package.

This layer owns provider/product taxonomy, capability metadata, domain validation,
request planning and readiness descriptions. API transport, CORE, ENGINE, DATABASE,
credential storage and authorization enforcement remain separately owned layers.
"""
from .catalog import ATLASSIAN_PROVIDER, ATLASSIAN_PRODUCTS, ATLASSIAN_CAPABILITIES
from .service import AtlassianEcosystemService

__all__ = [
    "ATLASSIAN_PROVIDER",
    "ATLASSIAN_PRODUCTS",
    "ATLASSIAN_CAPABILITIES",
    "AtlassianEcosystemService",
]
