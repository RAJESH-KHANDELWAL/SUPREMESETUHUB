"""Typed records for government recruitment tracks and notice provenance."""
from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True, slots=True)
class GovernmentJobTrack:
    id: str
    name: str
    description: str
    authority_scope: str
    role_families: Tuple[str, ...]
    source_expectation: str
    classification_caution: str

@dataclass(frozen=True, slots=True)
class RecruitmentNoticeProvenance:
    issuing_authority: str
    jurisdiction: str
    official_notice_url: str
    notice_or_advertisement_id: str
    publication_date: str
    application_deadline: str | None
    last_verified_at: str
    verification_status: str
