"""Bharat-to-global domain taxonomy and ecosystem namespace package.

This package exposes read-only catalogue operations. It does not own runtime
business logic; CORE, API, ENGINE, DATABASE and SECURITY remain independent.
"""
from .domain_taxonomy import (
    get_domain,
    get_domain_by_name,
    get_domain_catalog,
    list_domains,
    search_domains,
    validate_domain_taxonomy,
)
from .catalog import GLOBAL_BUSINESS_ECOSYSTEMS, GLOBAL_DOMAIN_ECOSYSTEMS, VENDOR_ECOSYSTEMS

__all__ = [
    "list_domains",
    "get_domain",
    "get_domain_by_name",
    "search_domains",
    "get_domain_catalog",
    "validate_domain_taxonomy",
    "GLOBAL_BUSINESS_ECOSYSTEMS",
    "GLOBAL_DOMAIN_ECOSYSTEMS",
    "VENDOR_ECOSYSTEMS",
]
