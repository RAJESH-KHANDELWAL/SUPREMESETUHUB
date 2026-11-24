"""Singular provider package for external integrations.

Provider-specific modules implement the shared IntegrationProvider contract.
Canonical Bada Business resource facts remain in backend.global_ecosystem.global_bada_business_ecosystem.
"""
from .bada_business import BadaBusinessProvider

__all__ = ["BadaBusinessProvider"]
