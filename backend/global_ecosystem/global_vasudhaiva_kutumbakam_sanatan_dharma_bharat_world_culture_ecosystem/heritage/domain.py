"""Structured domain model for Global Heritage.

This module defines discoverable subject areas, evidence metadata and a small
validated record model. It does not assert that every listed topic has already
been researched or that every resource is cleared for public reuse.
"""
from dataclasses import dataclass, field
from typing import Optional, Tuple

DOMAIN_ID = "HERITAGE"
DOMAIN_NAME = "Global Heritage"
DOMAIN_DESCRIPTION = "Tangible, intangible, natural and documentary heritage, with stewardship and provenance safeguards."

SUBJECT_AREAS: Tuple[str, ...] = (
    "archaeological_sites",
    "monuments_and_architecture",
    "manuscripts_and_archives",
    "museum_collections",
    "intangible_cultural_heritage",
    "cultural_landscapes",
    "natural_and_mixed_heritage",
    "conservation_and_restoration",
    "heritage_law_and_stewardship",
)

SOURCE_KINDS = frozenset({
    "primary_text", "archaeological_evidence", "archival_record",
    "peer_reviewed_research", "academic_reference", "oral_history",
    "community_account", "institutional_record", "interpretation",
    "traditional_account", "unspecified",
})
CONFIDENCE_LEVELS = frozenset({"high", "medium", "low", "contested", "unknown"})
ACCESS_LEVELS = frozenset({"public", "community", "restricted"})
CONSENT_STATES = frozenset({"granted", "pending", "denied", "not_required"})
RIGHTS_STATES = frozenset({"public_domain", "licensed", "permission_required", "restricted", "unknown"})

@dataclass(frozen=True)
class KnowledgeRecord:
    """A source-aware record in the Global Heritage domain."""
    record_id: str
    title: str
    subject_area: str
    summary: str
    source_kind: str = "unspecified"
    source_title: Optional[str] = None
    source_url: Optional[str] = None
    creator_or_custodian: Optional[str] = None
    date_or_period: Optional[str] = None
    geographic_context: Optional[str] = None
    language: Optional[str] = None
    confidence: str = "unknown"
    access_level: str = "public"
    consent: str = "not_required"
    rights: str = "unknown"
    tags: Tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self):
        if not self.record_id.strip() or not self.title.strip() or not self.summary.strip():
            raise ValueError("record_id, title and summary are required")
        if self.subject_area not in SUBJECT_AREAS:
            raise ValueError("subject_area must be a canonical heritage area")
        if self.source_kind not in SOURCE_KINDS:
            raise ValueError("unsupported source_kind")
        if self.confidence not in CONFIDENCE_LEVELS:
            raise ValueError("unsupported confidence")
        if self.access_level not in ACCESS_LEVELS:
            raise ValueError("unsupported access_level")
        if self.consent not in CONSENT_STATES:
            raise ValueError("unsupported consent state")
        if self.rights not in RIGHTS_STATES:
            raise ValueError("unsupported rights state")

def search_records(records, keyword: str, subject_area: Optional[str] = None):
    """Deterministic keyword search; callers must apply publication governance."""
    needle = keyword.strip().casefold()
    if subject_area is not None and subject_area not in SUBJECT_AREAS:
        raise ValueError("unknown subject_area")
    if not needle:
        return tuple()
    return tuple(
        record for record in records
        if (subject_area is None or record.subject_area == subject_area)
        and needle in " ".join((
            record.title, record.summary, record.subject_area,
            " ".join(record.tags)
        )).casefold()
    )
