"""Structured domain model for Knowledge Verification.

Defines discoverable subject areas, evidence metadata and a validated record.
The taxonomy is not a claim that every topic has already been researched.
"""
from dataclasses import dataclass, field
from typing import Optional, Tuple

DOMAIN_ID = "VERIFICATION"
DOMAIN_NAME = "Knowledge Verification"
DOMAIN_DESCRIPTION = "Source criticism, evidence grading, correction workflows and responsible publication checks."
SUBJECT_AREAS: Tuple[str, ...] = (
    "primary_source_review",
    "secondary_source_review",
    "source_provenance",
    "date_and_attribution_checks",
    "translation_and_transcription_review",
    "claim_confidence_and_uncertainty",
    "correction_and_takedown_workflows",
    "citation_quality",
    "editorial_review",
)
SOURCE_KINDS = frozenset({"primary_text", "archaeological_evidence", "archival_record", "peer_reviewed_research", "academic_reference", "oral_history", "community_account", "institutional_record", "interpretation", "traditional_account", "unspecified"})
CONFIDENCE_LEVELS = frozenset({"high", "medium", "low", "contested", "unknown"})
ACCESS_LEVELS = frozenset({"public", "community", "restricted"})
CONSENT_STATES = frozenset({"granted", "pending", "denied", "not_required"})
RIGHTS_STATES = frozenset({"public_domain", "licensed", "permission_required", "restricted", "unknown"})

@dataclass(frozen=True)
class KnowledgeRecord:
    """Source-aware record in the Knowledge Verification domain."""
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
            raise ValueError("subject_area must be a canonical verification area")
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
    """Deterministic keyword search; publication governance is a separate check."""
    needle = keyword.strip().casefold()
    if subject_area is not None and subject_area not in SUBJECT_AREAS:
        raise ValueError("unknown subject_area")
    if not needle:
        return tuple()
    return tuple(record for record in records
                 if (subject_area is None or record.subject_area == subject_area)
                 and needle in " ".join((record.title, record.summary, record.subject_area, " ".join(record.tags))).casefold())
