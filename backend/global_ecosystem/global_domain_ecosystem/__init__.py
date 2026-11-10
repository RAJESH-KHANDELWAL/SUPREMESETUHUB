"""Bharat-to-global domain ecosystem catalog namespace."""
from .catalog import DOMAIN_GROUPS, GEOGRAPHIC_SCOPES, MATURITY_LEVELS, get_domain_catalog
from .models import DomainProfile
from .registry import DomainRegistry
from .governance import validate_domain_profile
from .adult_domains import get_adult_domain_requirements, validate_adult_domain
from .regional import get_regional_scope
from .classification import classify_domain

__all__ = [
    "DOMAIN_GROUPS", "GEOGRAPHIC_SCOPES", "MATURITY_LEVELS",
    "get_domain_catalog", "DomainProfile", "DomainRegistry",
    "validate_domain_profile", "get_adult_domain_requirements",
    "validate_adult_domain", "get_regional_scope", "classify_domain",
]
