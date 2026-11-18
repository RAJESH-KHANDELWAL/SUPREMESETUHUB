"""Business listing gates for consent, rights, provenance and responsible trade."""
from dataclasses import dataclass
from .business_domain import BusinessOffering

@dataclass(frozen=True)
class ListingAssessment:
    eligible_for_publication: bool
    reasons: tuple

def assess_listing(offering: BusinessOffering) -> ListingAssessment:
    """Check minimum evidence gates before an offering can be published.

    Passing these checks is not a legal opinion, regulatory approval or proof
    that the provider is genuinely operating. Human review remains required.
    """
    reasons = []
    if offering.provider.verification_status != "verified":
        reasons.append("provider_not_verified")
    if offering.consent_status in {"pending", "denied"}:
        reasons.append("cultural_or_rights_holder_consent_not_granted")
    if offering.rights_status in {"permission_required", "restricted", "unknown"}:
        reasons.append("commercial_rights_not_cleared")
    if not offering.provenance_reference:
        reasons.append("provenance_evidence_missing")
    if not offering.fair_compensation_defined:
        reasons.append("fair_compensation_terms_not_defined")
    if not offering.safety_reviewed:
        reasons.append("safety_review_not_completed")
    if not offering.legal_reviewed:
        reasons.append("applicable_legal_review_not_completed")
    if offering.status not in {"approved", "published"}:
        reasons.append("offering_not_approved")
    return ListingAssessment(not reasons, tuple(reasons))
