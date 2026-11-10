"""Canonical GLOBAL BADA BUSINESS ECOSYSTEM package.

This package owns Bada Business resource discovery and domain-level workflows.
Public HTTP routes, shared CORE contracts, orchestration ENGINE, and persistent
DATABASE adapters remain in their independent architecture layers.
"""
from .platform_resources import ECOSYSTEM_ID, ECOSYSTEM_NAME, get_catalog, get_program, list_programs
from .courses import get_course, list_courses, search_courses
from .events import get_event, list_events
from .registration import RegistrationDraft, create_registration_draft, validate_registration
from .referrals import extract_referral_code, normalize_referral_url

ECOSYSTEM = {
    "id": "GLOBAL_BADA_BUSINESS_ECOSYSTEM",
    "name": "GLOBAL BADA BUSINESS ECOSYSTEM",
    "provider": "Bada Business",
}

__all__ = [
    "ECOSYSTEM", "ECOSYSTEM_ID", "ECOSYSTEM_NAME", "get_catalog",
    "get_program", "list_programs", "get_course", "list_courses",
    "search_courses", "get_event", "list_events", "RegistrationDraft",
    "create_registration_draft", "validate_registration",
    "extract_referral_code", "normalize_referral_url",
]
