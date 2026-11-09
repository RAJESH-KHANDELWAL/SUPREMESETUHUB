"""Typed API contract for sourced Government Jobs recruitment notices."""
from typing import Literal, NotRequired, TypedDict

VerificationStatus = Literal["unverified", "source_checked", "authority_confirmed", "expired", "withdrawn"]

class RecruitmentNoticeRecord(TypedDict):
    """Minimum provenance fields; presence does not prove notice authenticity."""
    notice_id: str
    title: str
    issuing_authority: str
    jurisdiction: str
    official_notice_url: str
    notice_or_advertisement_id: str
    publication_date: str
    application_deadline: str | None
    last_verified_at: str
    verification_status: VerificationStatus
    employment_type: NotRequired[str]
    work_location: NotRequired[str]
    qualification_summary: NotRequired[str]
