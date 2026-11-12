"""GLOBAL BADA BUSINESS ECOSYSTEM package.

This is the user's broader business ecosystem. The separate BADA BUSINESS
ECOSYSTEM catalog below represents the external Bada Business platform.
"""
from .platform_resources import (
    ECOSYSTEM_ID as BADA_BUSINESS_ECOSYSTEM_ID,
    ECOSYSTEM_NAME as BADA_BUSINESS_ECOSYSTEM_NAME,
    get_catalog, get_program, list_programs,
)
from .courses import get_course, list_courses, search_courses
from .events import get_event, list_events
from .registration import RegistrationDraft, create_registration_draft, validate_registration
from .referrals import extract_referral_code, normalize_referral_url
from .business_verticals import (
    list_verticals, get_vertical, search_verticals,
    geographic_scopes, maturity_levels, get_vertical_guardrails,
    validate_adult_business_record,
)

GLOBAL_BADA_BUSINESS_ECOSYSTEM = {
    "id": "GLOBAL_BADA_BUSINESS_ECOSYSTEM",
    "name": "GLOBAL BADA BUSINESS ECOSYSTEM",
    "provider": "Independent ecosystem",
}
ECOSYSTEM = GLOBAL_BADA_BUSINESS_ECOSYSTEM

__all__ = [
    "ECOSYSTEM", "GLOBAL_BADA_BUSINESS_ECOSYSTEM",
    "BADA_BUSINESS_ECOSYSTEM_ID", "BADA_BUSINESS_ECOSYSTEM_NAME",
    "get_catalog", "get_program", "list_programs", "get_course",
    "list_courses", "search_courses", "get_event", "list_events",
    "RegistrationDraft", "create_registration_draft", "validate_registration",
    "extract_referral_code", "normalize_referral_url",
    "list_verticals", "get_vertical", "search_verticals",
    "geographic_scopes", "maturity_levels", "get_vertical_guardrails",
    "validate_adult_business_record",
]
