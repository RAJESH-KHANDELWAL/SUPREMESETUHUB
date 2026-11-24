"""Read-only adapter to the canonical Global Bada Business resource package."""
from __future__ import annotations
from typing import Any
from backend.global_ecosystem.global_bada_business_ecosystem.platform_resources import get_catalog, get_program, list_programs
from backend.global_ecosystem.global_bada_business_ecosystem.links import list_platform_links
from backend.global_ecosystem.global_bada_business_ecosystem.courses import get_course, list_courses, search_courses
from backend.global_ecosystem.global_bada_business_ecosystem.events import list_events
from backend.global_ecosystem.global_bada_business_ecosystem.registration import validate_registration
from backend.global_ecosystem.global_bada_business_ecosystem.referrals import extract_referral_code

class BadaBusinessResourceAdapter:
    """Read canonical provider records without copying or mutating them."""
    def catalog(self) -> dict[str, Any]: return get_catalog()
    def programs(self) -> list[dict[str, Any]]: return list_programs()
    def program(self, program_id: str) -> dict[str, Any] | None: return get_program(program_id)
    def courses(self) -> tuple[dict[str, Any], ...]: return list_courses()
    def course(self, course_id: str) -> dict[str, Any] | None: return get_course(course_id)
    def search_courses(self, query: str) -> tuple[dict[str, Any], ...]: return search_courses(query)
    def events(self) -> tuple[dict[str, Any], ...]: return list_events()
    def links(self) -> list[dict[str, Any]]: return list_platform_links()
    def validate_registration(self, payload: dict[str, Any]) -> dict[str, str]: return validate_registration(payload)
    def referral_code(self, url: str) -> str | None: return extract_referral_code(url)
    def products(self) -> list[dict[str, Any]]:
        # The canonical products namespace currently has no published records.
        return []
