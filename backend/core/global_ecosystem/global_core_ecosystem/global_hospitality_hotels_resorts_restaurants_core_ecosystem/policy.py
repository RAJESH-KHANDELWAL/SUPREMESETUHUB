"""Privacy and authorization guardrails; not a compliance certification."""
SENSITIVE_FIELDS = frozenset({"password","access_token","refresh_token","client_secret","card_number","cvv","passport_number","identity_document"})
HIGH_IMPACT_ACTIONS = frozenset({"confirm_booking","cancel_booking","take_payment","issue_refund","export_guest_data","delete_record"})
def validate_fields(fields):
    blocked=sorted({str(x).strip().lower() for x in (fields or ())} & SENSITIVE_FIELDS)
    return {"allowed": not blocked, "blocked_fields": blocked}
def authorize(action, authenticated=False, authorized=False, consent=False):
    if not authenticated or not authorized: return {"allowed":False,"reason":"AUTHENTICATION_AND_AUTHORIZATION_REQUIRED"}
    if str(action or "").strip().lower() in HIGH_IMPACT_ACTIONS and not consent: return {"allowed":False,"reason":"EXPLICIT_CONSENT_REQUIRED"}
    return {"allowed":True,"reason":"APPLICATION_LAYER_AUTHORIZED"}
