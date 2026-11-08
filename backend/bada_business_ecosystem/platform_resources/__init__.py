"""Canonical Bada Business platform links and program resources.

Backward-compatible implementation currently resides under the former
backend.bada_business.global_ecosystem package. New consumers should import
through this top-level Bada Business Ecosystem package.
"""
from backend.bada_business.global_ecosystem.global_bada_business_ecosystem.platform_resources import (
    ECOSYSTEM_ID,
    ECOSYSTEM_NAME,
    get_catalog,
    get_program,
    list_programs,
)

__all__ = [
    "ECOSYSTEM_ID",
    "ECOSYSTEM_NAME",
    "get_catalog",
    "get_program",
    "list_programs",
]
