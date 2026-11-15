"""Canonical functional taxonomy for GLOBAL DOMAIN storage."""
DOMAIN_CATEGORIES = {
 "domain_identity_and_portfolio": "Internal identity, normalized names, portfolios, ownership references",
 "domain_registration_and_acquisition": "Registrar references, registration metadata, acquisition provenance",
 "domain_dns_and_nameservers": "DNS zone metadata, record metadata, nameserver sets, delegation",
 "domain_hosting_and_infrastructure": "Hosting associations, origin references, deployment metadata",
 "domain_security_and_certificates": "DNSSEC, TLS certificate metadata, security posture",
 "domain_lifecycle_renewal_and_transfer": "Creation, expiry, renewal, transfer, suspension, deletion",
 "domain_compliance_and_governance": "Jurisdiction, policy, consent, audit, retention, legal hold",
 "domain_analytics_and_health": "Inventory metrics, availability observations, drift, health history",
}
def get_domain_catalog() -> dict:
 return dict(DOMAIN_CATEGORIES)
