"""Metadata redaction and restricted-domain policy guardrails."""
from collections.abc import Mapping
from copy import deepcopy
SENSITIVE_KEYS=frozenset({"token","access_token","refresh_token","client_secret","api_key","secret","authorization","password","credential","credential_value","private_key","webhook_secret","signing_secret","cookie","session","email","phone","mobile","address","date_of_birth","dob","government_id","passport_number","aadhaar_number","pan_number","bank_account","card_number","customer_payload","raw_payload"})
class IntegrationPolicyError(PermissionError): pass
def redact_sensitive_metadata(value):
    if isinstance(value,Mapping):
        return {str(k):redact_sensitive_metadata(v) for k,v in value.items() if str(k).casefold() not in SENSITIVE_KEYS}
    if isinstance(value,list): return [redact_sensitive_metadata(v) for v in value]
    if isinstance(value,tuple): return tuple(redact_sensitive_metadata(v) for v in value)
    return deepcopy(value)
def validate_domain_access(domain,*,age_assurance_verified=False,consent_verified=False,explicitly_authorized=False):
    if domain.get("age_restricted") and not age_assurance_verified: raise IntegrationPolicyError("AGE_ASSURANCE_REQUIRED")
    if domain.get("consent_required") and not consent_verified: raise IntegrationPolicyError("EXPLICIT_CONSENT_REQUIRED")
    if domain.get("sensitivity")=="RESTRICTED" and not explicitly_authorized: raise IntegrationPolicyError("EXPLICIT_AUTHORIZATION_REQUIRED")
def assert_catalog_only_operation(operation):
    if operation.strip().upper() not in {"DISCOVER","DESCRIBE","LIST","HEALTH","SEARCH"}:
        raise IntegrationPolicyError("CORE_LAYER_DOES_NOT_EXECUTE_PROVIDER_OPERATIONS")
