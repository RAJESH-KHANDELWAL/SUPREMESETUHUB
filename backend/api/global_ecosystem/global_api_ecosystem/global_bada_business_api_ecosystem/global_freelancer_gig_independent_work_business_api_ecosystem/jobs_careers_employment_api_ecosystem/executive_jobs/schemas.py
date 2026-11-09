"""Shared typed contract for work-and-career taxonomy records."""
from typing import NotRequired, TypedDict

class WorkCareerTrackRecord(TypedDict):
    """A taxonomy record, not a verified vacancy or eligibility decision."""
    id: str
    name: str
    description: str
    keywords: NotRequired[list[str]]
    related_track_ids: NotRequired[list[str]]
