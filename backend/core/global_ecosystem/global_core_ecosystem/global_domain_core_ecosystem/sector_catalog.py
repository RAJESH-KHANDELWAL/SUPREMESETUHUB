"""Expanded domain ecosystem sector taxonomy (classification, not integrations)."""
SECTORS = {
 "DOMAIN_REGISTRY_OPERATORS": "Registry operators, TLD registry services and delegated namespace administration",
 "ICANN_IANA_GOVERNANCE": "ICANN, IANA, registrar accreditation and global namespace governance",
 "GTLD_REGISTRARS": "Accredited and commercial gTLD registrar services",
 "CCTLD_REGISTRIES": "Country-code registry operators, local policy and country registration rules",
 "DOMAIN_RESELLERS": "Registrar reseller channels, wholesale platforms and white-label registration",
 "DOMAIN_MARKETPLACES": "Domain marketplaces, listing, brokerage and acquisition services",
 "DOMAIN_AUCTIONS": "Expired, premium, aftermarket and auction workflows",
 "DOMAIN_BACKORDER": "Backorder, drop-catching and pending-delete acquisition services",
 "DOMAIN_PORTFOLIO_MANAGEMENT": "Bulk portfolio management, ownership inventory and portfolio analytics",
 "DOMAIN_LIFECYCLE": "Registration, renewal, transfer, expiry, restoration and deletion lifecycle",
 "DOMAIN_TRANSFER": "Inter-registrar transfer, authorization codes and transfer lock workflows",
 "DOMAIN_AVAILABILITY": "Availability lookup, registration eligibility and premium-name discovery",
 "WHOIS_RDAP": "WHOIS and RDAP discovery, registration data and privacy-aware query boundaries",
 "DNS_AUTHORITATIVE_HOSTING": "Authoritative DNS, zone hosting, record operations and nameservers",
 "DNS_RECURSIVE_RESOLVERS": "Recursive DNS resolver and resolution service classification",
 "DNSSEC": "DNSSEC signing, delegation, validation and integrity",
 "DNS_PRIVACY_FILTERING": "DNS filtering, privacy, threat protection and policy resolvers",
 "DNS_MANAGEMENT_AUTOMATION": "DNS APIs, infrastructure-as-code, orchestration and multi-provider management",
 "DNS_LOAD_BALANCING": "DNS-based routing, traffic steering, failover and load distribution",
 "DNS_MONITORING": "DNS health, propagation checks, diagnostics and monitoring",
 "NAMESERVER_INFRASTRUCTURE": "Nameserver networks, glue, delegation and infrastructure metadata",
 "TLS_CERTIFICATE_AUTHORITIES": "Certificate authorities, certificate issuance and trust-chain metadata",
 "ACME_CERTIFICATE_AUTOMATION": "ACME protocol, challenge automation, issuance and renewal",
 "DOMAIN_BRANDING_PROTECTION": "Trademark, cybersquatting, brand and domain abuse monitoring",
 "DOMAIN_DISPUTES": "UDRP/URS, disputes, takedown processes and legal escalation references",
 "DOMAIN_REPUTATION_SECURITY": "Domain reputation, malware/phishing signals and abuse reporting",
 "IDN_AND_UNICODE_DOMAINS": "Internationalized domain names, Unicode and punycode handling",
 "DOMAIN_PARKING_MONETIZATION": "Parking, monetization, forwarding and landing-page services",
 "DOMAIN_REDIRECT_FORWARDING": "Web forwarding, URL redirects and email forwarding classifications",
 "DOMAIN_EMAIL_CONFIGURATION": "MX, SPF, DKIM, DMARC and domain email configuration metadata",
 "DOMAIN_DEPLOYMENT_BINDING": "Application/site binding, platform deployment and edge routing",
 "DOMAIN_API_INTEROPERABILITY": "Provider APIs, standards, capability contracts and adapter boundaries",
 "DOMAIN_TENANT_SECURITY": "Tenant ownership, permission scope, audit and external secret references",
 "DOMAIN_DATA_RETENTION": "Domain data model, retention, privacy and export/import boundaries",
 "DOMAIN_HEALTH_OBSERVABILITY": "Provider readiness, operational status, metrics and incident metadata",
 "DOMAIN_PRICING_RENEWAL": "Price/renewal metadata, premium pricing and fee transparency",
 "DOMAIN_ABUSE_COMPLIANCE": "Registration policy, abuse handling, privacy and compliance processes",
 "DOMAIN_REGIONAL_LOCALIZATION": "Country-specific rules, local language and regional service coverage",
 "DOMAIN_LEGACY_SPECIALTY": "Legacy, niche, specialty and uncommon domain service types",
}

def _sector_title(sector_id: str) -> str:
    subject = sector_id.replace("_", " ").strip()
    return f"GLOBAL {subject} CORE ECOSYSTEM"

def _sector_ecosystem_id(sector_id: str) -> str:
    return f"GLOBAL-{sector_id.replace('_', '-')}-CORE-ECOSYSTEM"

def list_sectors():
    return [
        {
            "sector_id": key,
            "ecosystem_id": _sector_ecosystem_id(key),
            "ecosystem_name": _sector_title(key),
            "name": _sector_title(key),
            "description": value,
            "naming_standard": "GLOBAL + SUBJECT + CORE ECOSYSTEM",
            "status": "CATALOG_ONLY",
            "live_connection_verified": False,
        }
        for key, value in SECTORS.items()
    ]
