"""Claim verification model: evidence, provenance, uncertainty and review state."""
from dataclasses import dataclass, field
from typing import Tuple

@dataclass(frozen=True)
class EvidenceItem:
    evidence_id: str
    source_title: str
    source_type: str
    locator: str
    supports: str
    limitations: str = ""

@dataclass(frozen=True)
class HistoricalClaim:
    claim_id: str
    statement: str
    claim_type: str
    evidence: Tuple[EvidenceItem, ...] = field(default_factory=tuple)
    confidence: str = "unknown"
    review_status: str = "unreviewed"
    counter_evidence: Tuple[str, ...] = ()

    def __post_init__(self):
        if not self.claim_id.strip() or not self.statement.strip():
            raise ValueError("CLAIM_ID_AND_STATEMENT_REQUIRED")
        if self.confidence not in {"high","medium","low","contested","unknown"}:
            raise ValueError("INVALID_CLAIM_CONFIDENCE")
        if self.review_status not in {"unreviewed","in_review","verified","qualified","rejected"}:
            raise ValueError("INVALID_REVIEW_STATUS")
        if self.review_status == "verified" and not self.evidence:
            raise ValueError("VERIFIED_CLAIM_REQUIRES_EVIDENCE")

def verification_report(claim: HistoricalClaim) -> dict:
    return {
      "claim_id":claim.claim_id,"statement":claim.statement,
      "review_status":claim.review_status,"confidence":claim.confidence,
      "evidence_count":len(claim.evidence),
      "counter_evidence_count":len(claim.counter_evidence),
      "publication_ready":claim.review_status=="verified" and bool(claim.evidence),
      "warning":"A verified record still requires transparent citations and scope limits."
    }
