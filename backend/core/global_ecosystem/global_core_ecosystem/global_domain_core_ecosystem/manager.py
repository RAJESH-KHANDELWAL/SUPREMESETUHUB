"""Canonical manager and in-module catalog for GLOBAL DOMAIN CORE ECOSYSTEM."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

# Sector taxonomy consolidated from the former sector_catalog.py.
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

# Domain catalog metadata consolidated from the former catalog.py.
"""Canonical catalog metadata with standardized ecosystem names."""
from copy import deepcopy
from typing import Any
ECOSYSTEM_ID = "GLOBAL-DOMAIN-CORE-ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL DOMAIN CORE ECOSYSTEM"
PARENT_ID = "GLOBAL-CORE-ECOSYSTEM"
PROVIDER_DIRECTORIES = ["abelohost_domain_core_ecosystem","acme_domain_core_ecosystem","afilias_domain_core_ecosystem","afraid_domain_core_ecosystem","akamai_domain_core_ecosystem","alexhost_domain_core_ecosystem","aws_domain_core_ecosystem","azure_domain_core_ecosystem","bind_domain_core_ecosystem","blueangelhost_domain_core_ecosystem","centralnic_domain_core_ecosystem","certbot_domain_core_ecosystem","cloudflare_domain_core_ecosystem","constellix_domain_core_ecosystem","deployment_domains_domain_core_ecosystem","desec_domain_core_ecosystem","digitalocean_domain_core_ecosystem","dns_services_domain_core_ecosystem","dnsexit_domain_core_ecosystem","dnsmadeeasy_domain_core_ecosystem","dnssec_domain_core_ecosystem","domain_lookup_domain_core_ecosystem","duckdns_domain_core_ecosystem","dynadot_domain_core_ecosystem","dynu_domain_core_ecosystem","easydns_domain_core_ecosystem","enom_domain_core_ecosystem","eurid_domain_core_ecosystem","flokinet_domain_core_ecosystem","flyio_domain_core_ecosystem","gandi_domain_core_ecosystem","gcore_domain_core_ecosystem","godaddy_domain_core_ecosystem","google_cloud_domain_core_ecosystem","he_domain_core_ecosystem","hetzner_domain_core_ecosystem","hexonet_domain_core_ecosystem","hosting_domain_core_ecosystem","hostinger_domain_core_ecosystem","hostkey_domain_core_ecosystem","hostsailor_domain_core_ecosystem","iana_domain_core_ecosystem","icann_domain_core_ecosystem","internetbs_domain_core_ecosystem","ionos_domain_core_ecosystem","iwantmyname_domain_core_ecosystem","joker_domain_core_ecosystem","keysystems_domain_core_ecosystem","letsencrypt_domain_core_ecosystem","namecheap_domain_core_ecosystem","namecom_domain_core_ecosystem","namesilo_domain_core_ecosystem","netlify_domain_core_ecosystem","nic_io_domain_core_ecosystem","noip_domain_core_ecosystem","nominet_domain_core_ecosystem","ns1_domain_core_ecosystem","octodns_domain_core_ecosystem","opensrs_domain_core_ecosystem","ovhcloud_domain_core_ecosystem","pdr_domain_core_ecosystem","pir_domain_core_ecosystem","porkbun_domain_core_ecosystem","powerdns_domain_core_ecosystem","rdap_domain_core_ecosystem","realtimeregister_domain_core_ecosystem","registrars_resellers_domain_core_ecosystem","registries_governance_domain_core_ecosystem","render_domain_core_ecosystem","resellerclub_domain_core_ecosystem","rrpproxy_domain_core_ecosystem","shinjiru_domain_core_ecosystem","technitium_domain_core_ecosystem","tls_certificate_domain_core_ecosystem","tucows_domain_core_ecosystem","vercel_domain_core_ecosystem","verisign_domain_core_ecosystem","whois_domain_core_ecosystem"]
DOMAIN_DEFINITIONS = {"REGISTRY_GOVERNANCE":{"name":"Registry Governance","purpose":"ICANN/IANA, registry oversight, policy, and delegated namespace governance."},"REGISTRAR_SERVICES":{"name":"Registrar Services","purpose":"Registration, renewal, transfer, ownership, reseller and registrar account boundaries."},"DNS_HOSTING_AND_OPERATIONS":{"name":"DNS Hosting and Operations","purpose":"Authoritative DNS, zone management, record lifecycle, DNS hosting and nameservers."},"DNS_SECURITY":{"name":"DNS Security","purpose":"DNSSEC, secure delegation, validation and integrity controls."},"DOMAIN_DISCOVERY_AND_LOOKUP":{"name":"Domain Discovery and Lookup","purpose":"WHOIS/RDAP lookup, availability discovery and domain intelligence."},"DOMAIN_AUTOMATION":{"name":"Domain Automation","purpose":"Automated registration, renewal, DNS updates and lifecycle orchestration boundaries."},"DOMAIN_RESELLER_AND_CHANNEL":{"name":"Reseller and Channel","purpose":"Reseller platforms, registrar distribution, account and customer lifecycle."},"DOMAIN_DEPLOYMENT_AND_BINDING":{"name":"Deployment and Domain Binding","purpose":"Deployment domain mapping, application binding, routing and edge configuration."},"TLS_CERTIFICATES_AND_TRUST":{"name":"TLS Certificates and Trust","purpose":"Certificate issuance, ACME, renewals, validation and trust-chain metadata."},"CLOUD_AND_PLATFORM_DOMAINS":{"name":"Cloud and Platform Domains","purpose":"Cloud provider domain products and integrated infrastructure services."},"DOMAIN_POLICY_AND_COMPLIANCE":{"name":"Domain Policy and Compliance","purpose":"Legal, registration policy, abuse response, privacy and compliance boundaries."},"DOMAIN_PROVIDER_ADAPTERS":{"name":"Provider Adapter Inventory","purpose":"Provider classification, adapter readiness, capability and transport ownership."},"DOMAIN_TENANCY_AND_ACCESS":{"name":"Tenant and Access Governance","purpose":"Tenant-scoped ownership, authorization, account context and secret references."},"DOMAIN_HEALTH_AND_OBSERVABILITY":{"name":"Health and Observability","purpose":"Readiness, health metadata, audit events, usage limits and provider status."},"DOMAIN_DATA_AND_STORAGE":{"name":"Domain Data and Storage","purpose":"Domain metadata models, storage boundaries, retention and data export contracts."},"DOMAIN_LIFECYCLE":{"name":"Domain Lifecycle","purpose":"Create, configure, renew, transfer, suspend, expire, restore and delete lifecycle metadata."},"DOMAIN_INTEGRATION_AND_INTEROPERABILITY":{"name":"Integration and Interoperability","purpose":"Provider integrations, standard interfaces and protocol interoperability."},"DOMAIN_SPECIALTY_SERVICES":{"name":"Specialty Domain Services","purpose":"Specialty, legacy, country-code and niche provider classifications."}}

SECTOR_ECOSYSTEMS = tuple({
    "ecosystem_id": item["ecosystem_id"],
    "name": item["ecosystem_name"],
    "ecosystem_type": "CORE_SERVICE",
    "parent_id": ECOSYSTEM_ID,
    "capabilities": [item["sector_id"]],
    "metadata": {"sector_id": item["sector_id"], "description": item["description"], "status": "CATALOG_ONLY", "live_connection_verified": False},
} for item in list_sectors())

ROOT = {
 "ecosystem_id": ECOSYSTEM_ID, "name": ECOSYSTEM_NAME,
 "ecosystem_type": "CORE_SERVICE", "parent_id": PARENT_ID,
 "status": "CORE_CATALOG_ONLY", "enabled": True,
 "capabilities": ["DOMAIN_REGISTRY","DOMAIN_LIFECYCLE_METADATA","DNS_PROVIDER_CLASSIFICATION","REGISTRAR_PROVIDER_CLASSIFICATION","DNSSEC_AND_TLS_METADATA","PROVIDER_DISCOVERY","TENANT_SCOPED_DOMAIN_METADATA","POLICY_AND_READINESS","SECTOR_ECOSYSTEM_REGISTRY"],
 "metadata": {"legacy_provider_directory_count": len(PROVIDER_DIRECTORIES), "legacy_domain_responsibility_count": len(DOMAIN_DEFINITIONS), "sector_ecosystem_count": len(SECTOR_ECOSYSTEMS), "live_connection_verified": False, "api_transport_in_core": False, "credential_storage": "EXTERNAL_SECRET_STORE_ONLY", "coverage_exhaustive": False}
}
def get_catalog() -> dict[str, Any]:
    return deepcopy(ROOT)
def list_provider_directories() -> list[str]:
    return list(PROVIDER_DIRECTORIES)
def list_domains() -> list[dict[str, Any]]:
    return [{"domain_id": key, **deepcopy(value)} for key,value in DOMAIN_DEFINITIONS.items()]
def list_sector_ecosystems() -> list[dict[str, Any]]:
    return deepcopy(list(SECTOR_ECOSYSTEMS))

# Canonical manager.
"""Canonical manager for GLOBAL DOMAIN CORE ECOSYSTEM."""
class GlobalDomainCoreManager:
    NAME=ECOSYSTEM_NAME
    ECOSYSTEM_ID=ECOSYSTEM_ID
    def __init__(self):
        from .orchestrator import DomainCoreOrchestrator
        from .service import GlobalDomainCoreService
        self.orchestrator=DomainCoreOrchestrator()
        self.service=GlobalDomainCoreService()
    def status(self):
        result=self.service.status()
        result["ecosystem_name"]=self.NAME
        result["sector_ecosystem_count"]=len(list_sector_ecosystems())
        result["naming_standard"]="GLOBAL + SUBJECT + CORE ECOSYSTEM"
        return result
    def health(self): return self.orchestrator.health()
    def list_providers(self): return self.orchestrator.providers()
    def list_domains(self): return self.orchestrator.domains()
    def list_sector_ecosystems(self): return list_sector_ecosystems()
    def get_sector_ecosystem(self,ecosystem_id:str):
        return next((row for row in list_sector_ecosystems() if row["ecosystem_id"]==ecosystem_id),None)
    def get_domain_manager(self, domain_id:str):
        from .module_service import DomainModuleService
        return DomainModuleService(domain_id)
def get_manager() -> GlobalDomainCoreManager:
    return GlobalDomainCoreManager()
__all__=["GlobalDomainCoreManager","get_manager"]
