"""Provider evidence, privacy and commercial action guardrails."""
SENSITIVE_FIELDS = frozenset({"password","access_token","refresh_token","client_secret","card_number","cvv","identity_document","bank_account_number"})
RESTRICTED_CLAIMS = frozenset({"licensed","certified","approved","verified","insured","accredited","guaranteed"})
HIGH_IMPACT_ACTIONS = frozenset({"take_payment","sign_contract","hire_worker","publish_offer","approve_provider","delete_record","issue_refund"})
def validate_fields(fields):
    blocked = sorted({str(x).strip().lower() for x in (fields or ())} & SENSITIVE_FIELDS)
    return {"allowed": not blocked, "blocked_fields": blocked}
def validate_provider_claim(claim, evidence_attached=False):
    restricted = str(claim or "").strip().lower() in RESTRICTED_CLAIMS
    return {"allowed": not restricted or bool(evidence_attached), "evidence_required": restricted, "status": "EVIDENCE_REVIEW_REQUIRED" if restricted and not evidence_attached else "ACCEPTED_FOR_REVIEW"}
def authorize(action, authenticated=False, authorized=False, consent=False):
    if not authenticated or not authorized: return {"allowed": False, "reason": "AUTHENTICATION_AND_AUTHORIZATION_REQUIRED"}
    if str(action or "").strip().lower() in HIGH_IMPACT_ACTIONS and not consent: return {"allowed": False, "reason": "EXPLICIT_CONSENT_REQUIRED"}
    return {"allowed": True, "reason": "APPLICATION_LAYER_AUTHORIZED"}
