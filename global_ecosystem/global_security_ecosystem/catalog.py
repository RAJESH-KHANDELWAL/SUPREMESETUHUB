"""Security domain catalog and maturity taxonomy."""
DOMAINS = {
 "identity": ("identity lifecycle", "authentication", "account recovery"),
 "access_control": ("RBAC", "ABAC", "least privilege", "policy evaluation"),
 "cryptography": ("encryption", "hashing", "key lifecycle", "digital signatures"),
 "secrets": ("secret inventory", "rotation policy", "vault integration contracts"),
 "network_security": ("segmentation", "firewall policy", "zero trust", "TLS posture"),
 "application_security": ("secure coding", "input validation", "dependency risk", "API protection"),
 "cloud_security": ("cloud posture", "workload identity", "configuration risk"),
 "endpoint_security": ("device inventory", "hardening", "endpoint telemetry"),
 "threat_intelligence": ("indicators", "advisories", "threat context"),
 "vulnerability_management": ("asset exposure", "risk scoring", "remediation tracking"),
 "incident_response": ("triage", "containment planning", "recovery", "lessons learned"),
 "data_protection": ("classification", "DLP policy", "backup protection", "retention"),
 "privacy": ("data minimization", "consent", "privacy requests", "impact assessment"),
 "compliance": ("control mapping", "evidence", "audit readiness"),
 "physical_security": ("facility access", "visitor management", "environmental controls"),
 "supply_chain": ("vendor risk", "software provenance", "SBOM", "third-party review"),
 "security_operations": ("monitoring", "alert handling", "case management", "metrics"),
}
MATURITY_LEVELS = ("basic", "standard", "advanced", "enterprise", "supreme")
SCOPES = ("local", "regional", "India", "international", "global")
def get_security_domains():
    return dict(DOMAINS)
