"""Core policy guards; not a legal-compliance certification."""
SENSITIVE_FIELDS = {"password", "access_token", "refresh_token", "card_number", "cvv", "identity_document"}
HIGH_IMPACT_ACTIONS = {"confirm_booking", "take_payment", "issue_refund", "publish_listing", "delete_record"}

def validate_fields(fields):
    blocked = sorted(set(fields or ()) & SENSITIVE_FIELDS)
    return {"allowed": not blocked, "blocked_fields": blocked}

def authorize(action, authenticated=False, authorized=False, consent=False):
    if not authenticated or not authorized:
        return {"allowed": False, "reason": "AUTHENTICATION_AND_AUTHORIZATION_REQUIRED"}
    if action in HIGH_IMPACT_ACTIONS and not consent:
        return {"allowed": False, "reason": "EXPLICIT_CONSENT_REQUIRED"}
    return {"allowed": True, "reason": "AUTHORIZED_AT_APPLICATION_LAYER"}
