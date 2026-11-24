"""Privacy request and data-minimization checklist helpers."""
def assess_privacy_request(*, request_type, identity_verified, jurisdiction_known, data_scope_defined):
    allowed={"access", "rectification", "erasure", "portability", "objection", "consent_withdrawal"}
    findings=[]
    if request_type not in allowed: findings.append("unsupported_request_type")
    if not identity_verified: findings.append("identity_verification_required")
    if not jurisdiction_known: findings.append("jurisdiction_review_required")
    if not data_scope_defined: findings.append("data_scope_must_be_defined")
    return tuple(findings)
