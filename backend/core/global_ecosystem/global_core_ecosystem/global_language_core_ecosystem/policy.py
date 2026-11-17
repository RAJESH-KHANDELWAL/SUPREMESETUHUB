"""Language catalog safety and privacy metadata helpers."""
from collections.abc import Mapping
from copy import deepcopy

SENSITIVE_KEYS=frozenset({"api_key","access_token","refresh_token","client_secret","token","secret","password","private_key","authorization","email","phone","mobile","address","date_of_birth","government_id","passport_number","aadhaar_number","pan_number"})

def redact_sensitive_metadata(value):
    if isinstance(value, Mapping):
        return {str(k):redact_sensitive_metadata(v) for k,v in value.items() if str(k).lower() not in SENSITIVE_KEYS}
    if isinstance(value,list):
        return [redact_sensitive_metadata(v) for v in value]
    if isinstance(value,tuple):
        return tuple(redact_sensitive_metadata(v) for v in value)
    return deepcopy(value)

def adult_content_policy():
    return {
        "age_restricted":True,
        "verified_adults_only":True,
        "informed_consent_required":True,
        "content_rights_required":True,
        "regional_legal_review_required":True,
        "moderation_and_takedown_required":True,
        "prohibited":["sexual content involving minors","non-consensual intimate imagery","coercion","trafficking","exploitation","illegal sexual content"],
    }
