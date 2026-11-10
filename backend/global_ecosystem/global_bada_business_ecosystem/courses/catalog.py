"""Course/program discovery over the canonical Bada Business resource catalog.

This module exposes only data already captured in this repository. It does not
claim current enrollment availability, official partnership, or live API access.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

from ..platform_resources.programs.bb_impact import BB_IMPACT
from ..platform_resources.programs.idea_to_ipo import IDEA_TO_IPO
from ..platform_resources.programs.lfp_digital import LFP_DIGITAL

_COURSES: dict[str, dict[str, Any]] = {
    "lfp_digital": LFP_DIGITAL,
    "bb_impact": BB_IMPACT,
    "idea_to_ipo": IDEA_TO_IPO,
}


def list_courses(*, include_past_events: bool = True) -> tuple[dict[str, Any], ...]:
    """Return course/program snapshots without exposing mutable source objects."""
    records = []
    for course in _COURSES.values():
        item = deepcopy(course)
        event = item.get("webinar", {})
        if not include_past_events and event.get("status") == "PAST_EVENT_DATE":
            continue
        records.append(item)
    return tuple(records)


def get_course(course_id: str) -> dict[str, Any] | None:
    """Look up a course by stable ID; whitespace and case are ignored."""
    if not isinstance(course_id, str):
        return None
    item = _COURSES.get(course_id.strip().lower())
    return deepcopy(item) if item is not None else None


def search_courses(query: str) -> tuple[dict[str, Any], ...]:
    """Search IDs, names, descriptions and framework titles."""
    term = (query or "").strip().lower()
    if not term:
        return ()
    matches = []
    for course in _COURSES.values():
        haystack = " ".join([
            str(course.get("program_id", "")),
            str(course.get("name", "")),
            str(course.get("tagline", "")),
            " ".join(course.get("outcomes", [])),
            " ".join(course.get("frameworks", [])),
        ]).lower()
        if term in haystack:
            matches.append(deepcopy(course))
    return tuple(matches)


def validate_course_catalog() -> tuple[str, ...]:
    """Return catalog integrity errors; empty means IDs and names are valid."""
    errors: list[str] = []
    seen: set[str] = set()
    for key, course in _COURSES.items():
        if key in seen:
            errors.append(f"duplicate course id: {key}")
        seen.add(key)
        if course.get("program_id") != key:
            errors.append(f"{key}: program_id does not match catalog key")
        if not course.get("name"):
            errors.append(f"{key}: missing name")
    return tuple(errors)
