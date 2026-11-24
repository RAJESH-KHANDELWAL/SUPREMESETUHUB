"""Business governance and safety guardrails."""
SENSITIVE_BUSINESS_TYPES = {"FINANCE", "COMPLIANCE", "ANIMAL", "AQUATIC", "RESOURCES", "TRADE"}

def capability_policy(domain: dict):
    kind = domain.get("business_type", "")
    return {
        "authorization_required": kind in SENSITIVE_BUSINESS_TYPES,
        "jurisdictional_compliance_required": True,
        "provider_verification_required": True,
        "catalog_is_not_operational_proof": True,
    }
