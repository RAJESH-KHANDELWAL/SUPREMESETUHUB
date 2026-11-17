"""Fail-closed policy metadata evaluation; no legal decision is automated."""

from __future__ import annotations

from .contracts import PolicyEvidence, result_envelope

REQUIRED_GATES = (
    "all_depicted_persons_verified_adults",
    "informed_consent_documented",
    "distribution_rights_documented",
    "moderation_approved",
    "jurisdiction_permitted",
)


def evaluate_content_metadata(evidence: PolicyEvidence) -> dict:
    reasons = [
        field.upper()
        for field in REQUIRED_GATES
        if not getattr(evidence, field, False)
    ]
    if evidence.prohibited_content_detected:
        reasons.append("PROHIBITED_CONTENT_FLAGGED")
    allowed = not reasons
    return result_envelope(
        allowed=allowed,
        status="ELIGIBLE_METADATA" if allowed else "BLOCKED_OR_REVIEW_REQUIRED",
        reasons=reasons,
    )
