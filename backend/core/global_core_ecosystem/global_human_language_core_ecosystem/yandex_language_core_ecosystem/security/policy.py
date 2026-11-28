"""Provider policy metadata for YANDEX LANGUAGE; not a substitute for app authorization."""
def evaluate(*, tenant_authenticated=False, provider_authorized=False, consent_verified=False):
    if not tenant_authenticated:
        return {"allowed": False, "reason": "AUTHENTICATED_TENANT_CONTEXT_REQUIRED"}
    if not provider_authorized:
        return {"allowed": False, "reason": "PROVIDER_AUTHORIZATION_REQUIRED"}
    if not consent_verified:
        return {"allowed": False, "reason": "CONSENT_OR_LEGAL_BASIS_REVIEW_REQUIRED"}
    return {"allowed": True, "reason": "APPLICATION_AND_PROVIDER_CHECKS_PASSED"}
