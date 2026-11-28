"""Cultural Core policy; metadata never grants publication or reuse rights."""
from typing import Any
from .governance import validate_cultural_record, assess_evidence
class CulturalCorePolicyError(PermissionError): pass
class CulturalCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any):
        if context is None: raise CulturalCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        validator=getattr(context,"validate",None)
        if not callable(validator): raise CulturalCorePolicyError("INVALID_TENANT_CONTEXT")
        validator()
    @staticmethod
    def validate_record(record): return validate_cultural_record(record)
    @staticmethod
    def classify_access(record):
        access=str(record.get("access_level","public")).lower(); rights=str(record.get("rights_status","unknown")).lower(); consent=str(record.get("consent_status","not_required")).lower()
        if access=="restricted" or rights=="restricted" or consent=="denied": return "RESTRICTED_ACCESS_DENIED"
        if access=="community" or rights in {"permission_required","unknown"} or consent=="pending": return "COMMUNITY_OR_PERMISSION_REVIEW_REQUIRED"
        return "PUBLIC_METADATA_ELIGIBLE_SUBJECT_TO_SOURCE_TERMS"
    @staticmethod
    def safe_record_summary(record):
        blocked={"private_notes","personal_phone","personal_email","access_token","refresh_token","api_key","secret"}
        return {k:v for k,v in record.items() if k.casefold() not in blocked}
