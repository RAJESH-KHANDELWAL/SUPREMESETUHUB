"""Security and governance requirements for GitHub integrations."""
REQUIRED_CONTROLS = (
    "least-privilege GitHub App permissions",
    "explicit repository and organization authorization",
    "secret storage outside source control",
    "token rotation and revocation",
    "webhook signature verification and replay protection",
    "rate-limit and abuse-limit handling",
    "audit logging for privileged actions",
    "human confirmation for destructive or externally visible mutations",
    "data minimization and retention controls",
    "organization rulesets and branch-protection compliance",
)

def governance_profile():
    return {
        "provider": "github", "controls": list(REQUIRED_CONTROLS),
        "credential_storage_in_this_package": False,
        "authorization_implemented_in_this_package": False,
        "production_compliance_verified": False,
    }
