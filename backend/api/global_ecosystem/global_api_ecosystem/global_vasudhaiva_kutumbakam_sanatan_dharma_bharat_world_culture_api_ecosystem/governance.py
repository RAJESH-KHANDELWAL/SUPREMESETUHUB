"""Publication safeguards for cultural knowledge and heritage resources."""
from dataclasses import dataclass
from .domain import CulturalResource

@dataclass(frozen=True)
class PublicationAssessment:
    approved_for_public_discovery: bool
    reasons: tuple

def assess_publication(resource: CulturalResource) -> PublicationAssessment:
    """Apply conservative rights, consent, provenance and access checks.

    This is a domain-level checklist, not a legal determination. Restricted
    community material is never made public by this function.
    """
    reasons = []
    if resource.access_level != "public":
        reasons.append("resource_access_is_not_public")
    if resource.consent_status in {"pending", "denied"}:
        reasons.append("community_or_rights_holder_consent_not_granted")
    if resource.rights_status in {"permission_required", "restricted", "unknown"}:
        reasons.append("reuse_rights_not_cleared")
    if not resource.source_reference:
        reasons.append("source_provenance_missing")
    if resource.source_kind == "unspecified":
        reasons.append("source_kind_not_classified")
    return PublicationAssessment(not reasons, tuple(reasons))
