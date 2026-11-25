"""Lifecycle, evidence and risk guardrails for CORE metadata."""
from .contracts import ServiceWorkBusinessRecord
ALLOWED_STATUSES = {"DRAFT","REVIEW_REQUIRED","APPROVED","ACTIVE","SUSPENDED","RETIRED"}
ALLOWED_RISK_LEVELS = {"UNASSESSED","LOW","MEDIUM","HIGH","CRITICAL"}
REVIEW_DOMAINS = {"BUSINESS_COMPLIANCE","CLASSIFICATION_AND_STANDARDS","GOVERNMENT_PUBLIC_SERVICES_AND_SOCIAL_IMPACT"}
def validate_record_policy(record: ServiceWorkBusinessRecord) -> list[str]:
    record.validate_shape()
    errors: list[str] = []
    status, risk = record.lifecycle_status.strip().upper(), record.risk_level.strip().upper()
    if status not in ALLOWED_STATUSES: errors.append("UNSUPPORTED_LIFECYCLE_STATUS")
    if risk not in ALLOWED_RISK_LEVELS: errors.append("UNSUPPORTED_RISK_LEVEL")
    if status in {"APPROVED","ACTIVE"} and not record.evidence_refs: errors.append("APPROVAL_REQUIRES_EVIDENCE_REFERENCES")
    if record.domain_id.strip().upper() in REVIEW_DOMAINS and status == "ACTIVE" and not record.source_refs: errors.append("REGULATED_OR_PUBLIC_DOMAIN_REQUIRES_SOURCE_REFERENCES")
    if risk in {"HIGH","CRITICAL"} and status == "ACTIVE": errors.append("HIGH_RISK_ACTIVE_RECORD_REQUIRES_SEPARATE_AUTHORIZED_REVIEW")
    return errors
