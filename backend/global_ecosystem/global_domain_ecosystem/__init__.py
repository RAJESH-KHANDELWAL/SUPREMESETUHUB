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

from .business import get_business_domain_map
from .technology import get_technology_domain_map
from .health_and_life import get_health_and_life_map
from .society_and_governance import get_society_domain_map
from .industry_and_infrastructure import get_industry_domain_map
from .media_and_entertainment import get_media_domain_map
from .education_and_research import get_education_domain_map
from .travel_and_services import get_travel_services_map

__all__ += [
    "get_business_domain_map", "get_technology_domain_map",
    "get_health_and_life_map", "get_society_domain_map",
    "get_industry_domain_map", "get_media_domain_map",
    "get_education_domain_map", "get_travel_services_map",
]
from .finance_and_commerce import get_finance_commerce_map
from .security_and_trust import get_security_trust_map
from .environment_and_climate import get_environment_map
from .adult_safety_and_rights import get_adult_safety_framework
from .quality_and_operations import get_quality_operations_map

__all__ += [
    "get_finance_commerce_map", "get_security_trust_map",
    "get_environment_map", "get_adult_safety_framework",
    "get_quality_operations_map",
]
