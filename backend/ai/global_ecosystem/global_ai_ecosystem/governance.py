"""Security and governance controls expressed as policy descriptors."""
from .schemas import CatalogRecord

GOVERNANCE_CONTROLS = tuple(
    CatalogRecord(key, name, "governance_control", description, metadata={"default": "DENY_UNTIL_CONFIGURED"})
    for key, name, description in (
        ("identity", "Identity", "Authenticate users, services and workload identities."),
        ("authorization", "Authorization", "Apply least-privilege access to models and tools."),
        ("secret_handling", "Secret handling", "Keep provider credentials outside source code and logs."),
        ("privacy", "Privacy", "Minimize, classify and protect personal or sensitive data."),
        ("retention", "Data retention", "Define retention, deletion and training-use boundaries."),
        ("moderation", "Safety moderation", "Apply input and output safety policies."),
        ("audit", "Audit trail", "Record security-relevant actions and approvals."),
        ("cost_limits", "Cost and quota controls", "Enforce usage budgets, quotas and rate limits."),
        ("human_oversight", "Human oversight", "Require approval for consequential external actions."),
    )
)
