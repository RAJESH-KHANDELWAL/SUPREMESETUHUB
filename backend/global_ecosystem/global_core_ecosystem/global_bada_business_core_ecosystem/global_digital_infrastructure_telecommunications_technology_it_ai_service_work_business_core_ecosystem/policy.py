"""Fail-closed validation rules for engagement metadata."""
from .domain_catalog import get_domain
from .provider_registry import get_provider
ALLOWED_LIFECYCLE = {"DRAFT","PROPOSED","APPROVED","ACTIVE","SUSPENDED","COMPLETED","CLOSED"}
ALLOWED_RISK = {"UNASSESSED","LOW","MEDIUM","HIGH","CRITICAL"}
def validate_engagement(record) -> list[str]:
    errors = []
    if not record.record_id.strip(): errors.append("RECORD_ID_REQUIRED")
    if get_domain(record.domain_id) is None: errors.append("UNKNOWN_DOMAIN_ID")
    if not record.service_type.strip(): errors.append("SERVICE_TYPE_REQUIRED")
    if not record.description.strip(): errors.append("DESCRIPTION_REQUIRED")
    if not record.jurisdiction.strip(): errors.append("JURISDICTION_REQUIRED")
    if record.provider_id and get_provider(record.provider_id) is None: errors.append("UNKNOWN_PROVIDER_ID")
    if record.lifecycle_status not in ALLOWED_LIFECYCLE: errors.append("INVALID_LIFECYCLE_STATUS")
    if record.risk_level not in ALLOWED_RISK: errors.append("INVALID_RISK_LEVEL")
    if record.lifecycle_status in {"APPROVED","ACTIVE"} and not record.evidence_references: errors.append("APPROVAL_REQUIRES_EVIDENCE_REFERENCES")
    if record.lifecycle_status in {"APPROVED","ACTIVE"} and not record.approval_reference: errors.append("APPROVAL_REFERENCE_REQUIRED")
    if record.risk_level in {"HIGH","CRITICAL"} and not record.evidence_references: errors.append("ELEVATED_RISK_REQUIRES_EVIDENCE")
    return errors
