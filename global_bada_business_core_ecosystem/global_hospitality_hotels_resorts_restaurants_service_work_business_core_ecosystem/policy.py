"""Commercial service and provider guardrails."""
SENSITIVE_FIELDS = {"password", "access_token", "refresh_token", "card_number", "cvv", "identity_document"}
RESTRICTED_CLAIMS = {"licensed", "certified", "approved", "verified", "guaranteed"}
HIGH_IMPACT_ACTIONS = {"take_payment", "sign_contract", "hire_worker", "publish_offer", "delete_record"}
def validate_fields(fields):
    blocked = sorted(set(fields or ()) & SENSITIVE_FIELDS)
    return {"allowed": not blocked, "blocked_fields": blocked}
def validate_provider_claim(claim, evidence_attached=False):
    restricted = str(claim or "").strip().lower() in RESTRICTED_CLAIMS
    return {"allowed": not restricted or evidence_attached, "evidence_required": restricted, "status": "EVIDENCE_REVIEW_REQUIRED" if restricted and not evidence_attached else "CLAIM_ACCEPTED_FOR_REVIEW"}
def authorize(action, authenticated=False, authorized=False, consent=False):
    if not authenticated or not authorized: return {"allowed": False, "reason": "AUTHENTICATION_AND_AUTHORIZATION_REQUIRED"}
    if action in HIGH_IMPACT_ACTIONS and not consent: return {"allowed": False, "reason": "EXPLICIT_CONSENT_REQUIRED"}
    return {"allowed": True, "reason": "AUTHORIZED_AT_APPLICATION_LAYER"}
