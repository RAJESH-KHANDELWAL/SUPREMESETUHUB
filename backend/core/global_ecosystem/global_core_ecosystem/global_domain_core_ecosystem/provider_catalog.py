"""Canonical Core inventory for provider folders in the inspected repository snapshot.

Eight other child folders are capability packages, not providers; they are
listed separately to prevent category folders inflating provider totals.
No row implies API availability, entitlement, adapter readiness or connectivity.
"""
from __future__ import annotations
from copy import deepcopy
from typing import Any

DOMAIN_PROVIDER_CATALOG: tuple[dict[str, Any], ...] = (
    {"provider_id": "abelohost", "package_name": "abelohost_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-ABELOHOST-CORE-ECOSYSTEM", "name": "ABELOHOST", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "acme", "package_name": "acme_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-ACME-CORE-ECOSYSTEM", "name": "ACME", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "afilias", "package_name": "afilias_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-AFILIAS-CORE-ECOSYSTEM", "name": "AFILIAS", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "afraid", "package_name": "afraid_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-AFRAID-CORE-ECOSYSTEM", "name": "AFRAID", "category": "DNS_AND_NAMESERVER", "capabilities": ["DNS_ZONE_METADATA","DNS_RECORD_METADATA","NAMESERVER_AND_DELEGATION_METADATA","DNSSEC_POLICY_METADATA"]},
    {"provider_id": "akamai", "package_name": "akamai_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-AKAMAI-CORE-ECOSYSTEM", "name": "AKAMAI", "category": "HOSTING_AND_INFRASTRUCTURE", "capabilities": ["DOMAIN_HOSTING_ASSOCIATION_METADATA","ORIGIN_AND_DEPLOYMENT_REFERENCE","INFRASTRUCTURE_LINK_METADATA"]},
    {"provider_id": "alexhost", "package_name": "alexhost_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-ALEXHOST-CORE-ECOSYSTEM", "name": "ALEXHOST", "category": "HOSTING_AND_INFRASTRUCTURE", "capabilities": ["DOMAIN_HOSTING_ASSOCIATION_METADATA","ORIGIN_AND_DEPLOYMENT_REFERENCE","INFRASTRUCTURE_LINK_METADATA"]},
    {"provider_id": "aws", "package_name": "aws_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-AWS-CORE-ECOSYSTEM", "name": "AWS", "category": "HOSTING_AND_INFRASTRUCTURE", "capabilities": ["DOMAIN_HOSTING_ASSOCIATION_METADATA","ORIGIN_AND_DEPLOYMENT_REFERENCE","INFRASTRUCTURE_LINK_METADATA"]},
    {"provider_id": "azure", "package_name": "azure_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-AZURE-CORE-ECOSYSTEM", "name": "AZURE", "category": "HOSTING_AND_INFRASTRUCTURE", "capabilities": ["DOMAIN_HOSTING_ASSOCIATION_METADATA","ORIGIN_AND_DEPLOYMENT_REFERENCE","INFRASTRUCTURE_LINK_METADATA"]},
    {"provider_id": "bind", "package_name": "bind_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-BIND-CORE-ECOSYSTEM", "name": "BIND", "category": "DNS_AND_NAMESERVER", "capabilities": ["DNS_ZONE_METADATA","DNS_RECORD_METADATA","NAMESERVER_AND_DELEGATION_METADATA","DNSSEC_POLICY_METADATA"]},
    {"provider_id": "blueangelhost", "package_name": "blueangelhost_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-BLUEANGELHOST-CORE-ECOSYSTEM", "name": "BLUEANGELHOST", "category": "HOSTING_AND_INFRASTRUCTURE", "capabilities": ["DOMAIN_HOSTING_ASSOCIATION_METADATA","ORIGIN_AND_DEPLOYMENT_REFERENCE","INFRASTRUCTURE_LINK_METADATA"]},
    {"provider_id": "centralnic", "package_name": "centralnic_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-CENTRALNIC-CORE-ECOSYSTEM", "name": "CENTRALNIC", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "certbot", "package_name": "certbot_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-CERTBOT-CORE-ECOSYSTEM", "name": "CERTBOT", "category": "CERTIFICATE_AND_TLS", "capabilities": ["CERTIFICATE_INVENTORY_METADATA","TLS_LIFECYCLE_METADATA","CERTIFICATE_EXPIRY_METADATA"]},
    {"provider_id": "cloudflare", "package_name": "cloudflare_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-CLOUDFLARE-CORE-ECOSYSTEM", "name": "CLOUDFLARE", "category": "DNS_AND_NAMESERVER", "capabilities": ["DNS_ZONE_METADATA","DNS_RECORD_METADATA","NAMESERVER_AND_DELEGATION_METADATA","DNSSEC_POLICY_METADATA"]},
    {"provider_id": "constellix", "package_name": "constellix_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-CONSTELLIX-CORE-ECOSYSTEM", "name": "CONSTELLIX", "category": "DNS_AND_NAMESERVER", "capabilities": ["DNS_ZONE_METADATA","DNS_RECORD_METADATA","NAMESERVER_AND_DELEGATION_METADATA","DNSSEC_POLICY_METADATA"]},
    {"provider_id": "desec", "package_name": "desec_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-DESEC-CORE-ECOSYSTEM", "name": "DESEC", "category": "DNS_AND_NAMESERVER", "capabilities": ["DNS_ZONE_METADATA","DNS_RECORD_METADATA","NAMESERVER_AND_DELEGATION_METADATA","DNSSEC_POLICY_METADATA"]},
    {"provider_id": "digitalocean", "package_name": "digitalocean_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-DIGITALOCEAN-CORE-ECOSYSTEM", "name": "DIGITALOCEAN", "category": "HOSTING_AND_INFRASTRUCTURE", "capabilities": ["DOMAIN_HOSTING_ASSOCIATION_METADATA","ORIGIN_AND_DEPLOYMENT_REFERENCE","INFRASTRUCTURE_LINK_METADATA"]},
    {"provider_id": "dnsexit", "package_name": "dnsexit_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-DNSEXIT-CORE-ECOSYSTEM", "name": "DNSEXIT", "category": "DNS_AND_NAMESERVER", "capabilities": ["DNS_ZONE_METADATA","DNS_RECORD_METADATA","NAMESERVER_AND_DELEGATION_METADATA","DNSSEC_POLICY_METADATA"]},
    {"provider_id": "dnsmadeeasy", "package_name": "dnsmadeeasy_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-DNSMADEEASY-CORE-ECOSYSTEM", "name": "DNSMADEEASY", "category": "DNS_AND_NAMESERVER", "capabilities": ["DNS_ZONE_METADATA","DNS_RECORD_METADATA","NAMESERVER_AND_DELEGATION_METADATA","DNSSEC_POLICY_METADATA"]},
    {"provider_id": "duckdns", "package_name": "duckdns_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-DUCKDNS-CORE-ECOSYSTEM", "name": "DUCKDNS", "category": "DNS_AND_NAMESERVER", "capabilities": ["DNS_ZONE_METADATA","DNS_RECORD_METADATA","NAMESERVER_AND_DELEGATION_METADATA","DNSSEC_POLICY_METADATA"]},
    {"provider_id": "dynadot", "package_name": "dynadot_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-DYNADOT-CORE-ECOSYSTEM", "name": "DYNADOT", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "dynu", "package_name": "dynu_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-DYNU-CORE-ECOSYSTEM", "name": "DYNU", "category": "DNS_AND_NAMESERVER", "capabilities": ["DNS_ZONE_METADATA","DNS_RECORD_METADATA","NAMESERVER_AND_DELEGATION_METADATA","DNSSEC_POLICY_METADATA"]},
    {"provider_id": "easydns", "package_name": "easydns_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-EASYDNS-CORE-ECOSYSTEM", "name": "EASYDNS", "category": "DNS_AND_NAMESERVER", "capabilities": ["DNS_ZONE_METADATA","DNS_RECORD_METADATA","NAMESERVER_AND_DELEGATION_METADATA","DNSSEC_POLICY_METADATA"]},
    {"provider_id": "enom", "package_name": "enom_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-ENOM-CORE-ECOSYSTEM", "name": "ENOM", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "eurid", "package_name": "eurid_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-EURID-CORE-ECOSYSTEM", "name": "EURID", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "flokinet", "package_name": "flokinet_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-FLOKINET-CORE-ECOSYSTEM", "name": "FLOKINET", "category": "CROSS_PROVIDER_DOMAIN_OPERATIONS", "capabilities": ["DOMAIN_PORTFOLIO_METADATA","DOMAIN_LIFECYCLE_METADATA","CROSS_PROVIDER_DISCOVERY"]},
    {"provider_id": "flyio", "package_name": "flyio_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-FLYIO-CORE-ECOSYSTEM", "name": "FLYIO", "category": "HOSTING_AND_INFRASTRUCTURE", "capabilities": ["DOMAIN_HOSTING_ASSOCIATION_METADATA","ORIGIN_AND_DEPLOYMENT_REFERENCE","INFRASTRUCTURE_LINK_METADATA"]},
    {"provider_id": "gandi", "package_name": "gandi_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-GANDI-CORE-ECOSYSTEM", "name": "GANDI", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "gcore", "package_name": "gcore_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-GCORE-CORE-ECOSYSTEM", "name": "GCORE", "category": "HOSTING_AND_INFRASTRUCTURE", "capabilities": ["DOMAIN_HOSTING_ASSOCIATION_METADATA","ORIGIN_AND_DEPLOYMENT_REFERENCE","INFRASTRUCTURE_LINK_METADATA"]},
    {"provider_id": "godaddy", "package_name": "godaddy_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-GODADDY-CORE-ECOSYSTEM", "name": "GODADDY", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "google_cloud", "package_name": "google_cloud_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-GOOGLE-CLOUD-CORE-ECOSYSTEM", "name": "GOOGLE CLOUD", "category": "HOSTING_AND_INFRASTRUCTURE", "capabilities": ["DOMAIN_HOSTING_ASSOCIATION_METADATA","ORIGIN_AND_DEPLOYMENT_REFERENCE","INFRASTRUCTURE_LINK_METADATA"]},
    {"provider_id": "he", "package_name": "he_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-HE-CORE-ECOSYSTEM", "name": "HE", "category": "DNS_AND_NAMESERVER", "capabilities": ["DNS_ZONE_METADATA","DNS_RECORD_METADATA","NAMESERVER_AND_DELEGATION_METADATA","DNSSEC_POLICY_METADATA"]},
    {"provider_id": "hetzner", "package_name": "hetzner_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-HETZNER-CORE-ECOSYSTEM", "name": "HETZNER", "category": "HOSTING_AND_INFRASTRUCTURE", "capabilities": ["DOMAIN_HOSTING_ASSOCIATION_METADATA","ORIGIN_AND_DEPLOYMENT_REFERENCE","INFRASTRUCTURE_LINK_METADATA"]},
    {"provider_id": "hexonet", "package_name": "hexonet_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-HEXONET-CORE-ECOSYSTEM", "name": "HEXONET", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "hostinger", "package_name": "hostinger_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-HOSTINGER-CORE-ECOSYSTEM", "name": "HOSTINGER", "category": "HOSTING_AND_INFRASTRUCTURE", "capabilities": ["DOMAIN_HOSTING_ASSOCIATION_METADATA","ORIGIN_AND_DEPLOYMENT_REFERENCE","INFRASTRUCTURE_LINK_METADATA"]},
    {"provider_id": "hostkey", "package_name": "hostkey_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-HOSTKEY-CORE-ECOSYSTEM", "name": "HOSTKEY", "category": "HOSTING_AND_INFRASTRUCTURE", "capabilities": ["DOMAIN_HOSTING_ASSOCIATION_METADATA","ORIGIN_AND_DEPLOYMENT_REFERENCE","INFRASTRUCTURE_LINK_METADATA"]},
    {"provider_id": "hostsailor", "package_name": "hostsailor_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-HOSTSAILOR-CORE-ECOSYSTEM", "name": "HOSTSAILOR", "category": "HOSTING_AND_INFRASTRUCTURE", "capabilities": ["DOMAIN_HOSTING_ASSOCIATION_METADATA","ORIGIN_AND_DEPLOYMENT_REFERENCE","INFRASTRUCTURE_LINK_METADATA"]},
    {"provider_id": "iana", "package_name": "iana_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-IANA-CORE-ECOSYSTEM", "name": "IANA", "category": "REGISTRY_GOVERNANCE_AND_LOOKUP", "capabilities": ["DOMAIN_LOOKUP_METADATA","RDAP_WHOIS_REFERENCE_METADATA","REGISTRY_POLICY_REFERENCE"]},
    {"provider_id": "icann", "package_name": "icann_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-ICANN-CORE-ECOSYSTEM", "name": "ICANN", "category": "REGISTRY_GOVERNANCE_AND_LOOKUP", "capabilities": ["DOMAIN_LOOKUP_METADATA","RDAP_WHOIS_REFERENCE_METADATA","REGISTRY_POLICY_REFERENCE"]},
    {"provider_id": "internetbs", "package_name": "internetbs_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-INTERNETBS-CORE-ECOSYSTEM", "name": "INTERNETBS", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "ionos", "package_name": "ionos_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-IONOS-CORE-ECOSYSTEM", "name": "IONOS", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "iwantmyname", "package_name": "iwantmyname_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-IWANTMYNAME-CORE-ECOSYSTEM", "name": "IWANTMYNAME", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "joker", "package_name": "joker_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-JOKER-CORE-ECOSYSTEM", "name": "JOKER", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "keysystems", "package_name": "keysystems_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-KEYSYSTEMS-CORE-ECOSYSTEM", "name": "KEYSYSTEMS", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "letsencrypt", "package_name": "letsencrypt_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-LETSENCRYPT-CORE-ECOSYSTEM", "name": "LETSENCRYPT", "category": "CERTIFICATE_AND_TLS", "capabilities": ["CERTIFICATE_INVENTORY_METADATA","TLS_LIFECYCLE_METADATA","CERTIFICATE_EXPIRY_METADATA"]},
    {"provider_id": "namecheap", "package_name": "namecheap_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-NAMECHEAP-CORE-ECOSYSTEM", "name": "NAMECHEAP", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "namecom", "package_name": "namecom_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-NAMECOM-CORE-ECOSYSTEM", "name": "NAMECOM", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "namesilo", "package_name": "namesilo_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-NAMESILO-CORE-ECOSYSTEM", "name": "NAMESILO", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "netlify", "package_name": "netlify_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-NETLIFY-CORE-ECOSYSTEM", "name": "NETLIFY", "category": "HOSTING_AND_INFRASTRUCTURE", "capabilities": ["DOMAIN_HOSTING_ASSOCIATION_METADATA","ORIGIN_AND_DEPLOYMENT_REFERENCE","INFRASTRUCTURE_LINK_METADATA"]},
    {"provider_id": "nic_io", "package_name": "nic_io_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-NIC-IO-CORE-ECOSYSTEM", "name": "NIC IO", "category": "REGISTRY_GOVERNANCE_AND_LOOKUP", "capabilities": ["DOMAIN_LOOKUP_METADATA","RDAP_WHOIS_REFERENCE_METADATA","REGISTRY_POLICY_REFERENCE"]},
    {"provider_id": "noip", "package_name": "noip_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-NOIP-CORE-ECOSYSTEM", "name": "NOIP", "category": "DNS_AND_NAMESERVER", "capabilities": ["DNS_ZONE_METADATA","DNS_RECORD_METADATA","NAMESERVER_AND_DELEGATION_METADATA","DNSSEC_POLICY_METADATA"]},
    {"provider_id": "nominet", "package_name": "nominet_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-NOMINET-CORE-ECOSYSTEM", "name": "NOMINET", "category": "REGISTRY_GOVERNANCE_AND_LOOKUP", "capabilities": ["DOMAIN_LOOKUP_METADATA","RDAP_WHOIS_REFERENCE_METADATA","REGISTRY_POLICY_REFERENCE"]},
    {"provider_id": "ns1", "package_name": "ns1_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-NS1-CORE-ECOSYSTEM", "name": "NS1", "category": "DNS_AND_NAMESERVER", "capabilities": ["DNS_ZONE_METADATA","DNS_RECORD_METADATA","NAMESERVER_AND_DELEGATION_METADATA","DNSSEC_POLICY_METADATA"]},
    {"provider_id": "octodns", "package_name": "octodns_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-OCTODNS-CORE-ECOSYSTEM", "name": "OCTODNS", "category": "DNS_AND_NAMESERVER", "capabilities": ["DNS_ZONE_METADATA","DNS_RECORD_METADATA","NAMESERVER_AND_DELEGATION_METADATA","DNSSEC_POLICY_METADATA"]},
    {"provider_id": "opensrs", "package_name": "opensrs_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-OPENSRS-CORE-ECOSYSTEM", "name": "OPENSRS", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "ovhcloud", "package_name": "ovhcloud_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-OVHCLOUD-CORE-ECOSYSTEM", "name": "OVHCLOUD", "category": "HOSTING_AND_INFRASTRUCTURE", "capabilities": ["DOMAIN_HOSTING_ASSOCIATION_METADATA","ORIGIN_AND_DEPLOYMENT_REFERENCE","INFRASTRUCTURE_LINK_METADATA"]},
    {"provider_id": "pdr", "package_name": "pdr_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-PDR-CORE-ECOSYSTEM", "name": "PDR", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "pir", "package_name": "pir_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-PIR-CORE-ECOSYSTEM", "name": "PIR", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "porkbun", "package_name": "porkbun_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-PORKBUN-CORE-ECOSYSTEM", "name": "PORKBUN", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "powerdns", "package_name": "powerdns_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-POWERDNS-CORE-ECOSYSTEM", "name": "POWERDNS", "category": "DNS_AND_NAMESERVER", "capabilities": ["DNS_ZONE_METADATA","DNS_RECORD_METADATA","NAMESERVER_AND_DELEGATION_METADATA","DNSSEC_POLICY_METADATA"]},
    {"provider_id": "rdap", "package_name": "rdap_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-RDAP-CORE-ECOSYSTEM", "name": "RDAP", "category": "REGISTRY_GOVERNANCE_AND_LOOKUP", "capabilities": ["DOMAIN_LOOKUP_METADATA","RDAP_WHOIS_REFERENCE_METADATA","REGISTRY_POLICY_REFERENCE"]},
    {"provider_id": "realtimeregister", "package_name": "realtimeregister_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-REALTIMEREGISTER-CORE-ECOSYSTEM", "name": "REALTIMEREGISTER", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "render", "package_name": "render_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-RENDER-CORE-ECOSYSTEM", "name": "RENDER", "category": "HOSTING_AND_INFRASTRUCTURE", "capabilities": ["DOMAIN_HOSTING_ASSOCIATION_METADATA","ORIGIN_AND_DEPLOYMENT_REFERENCE","INFRASTRUCTURE_LINK_METADATA"]},
    {"provider_id": "resellerclub", "package_name": "resellerclub_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-RESELLERCLUB-CORE-ECOSYSTEM", "name": "RESELLERCLUB", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "rrpproxy", "package_name": "rrpproxy_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-RRPPROXY-CORE-ECOSYSTEM", "name": "RRPPROXY", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "shinjiru", "package_name": "shinjiru_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-SHINJIRU-CORE-ECOSYSTEM", "name": "SHINJIRU", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "technitium", "package_name": "technitium_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-TECHNITIUM-CORE-ECOSYSTEM", "name": "TECHNITIUM", "category": "DNS_AND_NAMESERVER", "capabilities": ["DNS_ZONE_METADATA","DNS_RECORD_METADATA","NAMESERVER_AND_DELEGATION_METADATA","DNSSEC_POLICY_METADATA"]},
    {"provider_id": "tucows", "package_name": "tucows_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-TUCOWS-CORE-ECOSYSTEM", "name": "TUCOWS", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "vercel", "package_name": "vercel_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-VERCEL-CORE-ECOSYSTEM", "name": "VERCEL", "category": "HOSTING_AND_INFRASTRUCTURE", "capabilities": ["DOMAIN_HOSTING_ASSOCIATION_METADATA","ORIGIN_AND_DEPLOYMENT_REFERENCE","INFRASTRUCTURE_LINK_METADATA"]},
    {"provider_id": "verisign", "package_name": "verisign_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-VERISIGN-CORE-ECOSYSTEM", "name": "VERISIGN", "category": "REGISTRAR_AND_RESELLER", "capabilities": ["DOMAIN_REGISTRATION_METADATA","DOMAIN_TRANSFER_METADATA","RENEWAL_AND_EXPIRY_METADATA","REGISTRAR_ACCOUNT_BOUNDARY"]},
    {"provider_id": "whois", "package_name": "whois_domain_core_ecosystem", "ecosystem_id": "GLOBAL-DOMAIN-WHOIS-CORE-ECOSYSTEM", "name": "WHOIS", "category": "REGISTRY_GOVERNANCE_AND_LOOKUP", "capabilities": ["DOMAIN_LOOKUP_METADATA","RDAP_WHOIS_REFERENCE_METADATA","REGISTRY_POLICY_REFERENCE"]},
)

DOMAIN_CAPABILITY_PACKAGE_CATALOG: tuple[dict[str, str], ...] = (
    {"package_id": "deployment_domains", "package_name": "deployment_domains_domain_core_ecosystem", "classification": "DOMAIN_CAPABILITY_PACKAGE"},
    {"package_id": "dns_services", "package_name": "dns_services_domain_core_ecosystem", "classification": "DOMAIN_CAPABILITY_PACKAGE"},
    {"package_id": "dnssec", "package_name": "dnssec_domain_core_ecosystem", "classification": "DOMAIN_CAPABILITY_PACKAGE"},
    {"package_id": "domain_lookup", "package_name": "domain_lookup_domain_core_ecosystem", "classification": "DOMAIN_CAPABILITY_PACKAGE"},
    {"package_id": "hosting", "package_name": "hosting_domain_core_ecosystem", "classification": "DOMAIN_CAPABILITY_PACKAGE"},
    {"package_id": "registrars_resellers", "package_name": "registrars_resellers_domain_core_ecosystem", "classification": "DOMAIN_CAPABILITY_PACKAGE"},
    {"package_id": "registries_governance", "package_name": "registries_governance_domain_core_ecosystem", "classification": "DOMAIN_CAPABILITY_PACKAGE"},
    {"package_id": "tls_certificate", "package_name": "tls_certificate_domain_core_ecosystem", "classification": "DOMAIN_CAPABILITY_PACKAGE"},
)

def list_domain_providers() -> list[dict[str, Any]]:
    result = []
    for source in DOMAIN_PROVIDER_CATALOG:
        item = deepcopy(source)
        item.update({
            "status": "CORE_CATALOG_ONLY",
            "enabled": True,
            "connected": False,
            "live_connection_verified": False,
            "api_available": None,
            "api_calls_performed": 0,
        })
        item["core_module"] = "backend/core/global_ecosystem/global_core_ecosystem/global_domain_core_ecosystem/" + item["package_name"]
        result.append(item)
    return result

def list_domain_capability_packages() -> list[dict[str, str]]:
    return deepcopy(list(DOMAIN_CAPABILITY_PACKAGE_CATALOG))

def get_domain_provider(provider_id: str) -> dict[str, Any] | None:
    needle = str(provider_id or "").strip().casefold()
    if not needle:
        return None
    return next((item for item in list_domain_providers()
                 if item["provider_id"].casefold() == needle
                 or item["ecosystem_id"].casefold() == needle
                 or item["name"].casefold() == needle), None)

def domain_provider_summary() -> dict[str, Any]:
    providers = list_domain_providers()
    counts: dict[str, int] = {}
    for item in providers:
        counts[item["category"]] = counts.get(item["category"], 0) + 1
    return {
        "success": True,
        "provider_count": len(providers),
        "capability_package_count": len(DOMAIN_CAPABILITY_PACKAGE_CATALOG),
        "domain_related_child_folder_count": len(providers) + len(DOMAIN_CAPABILITY_PACKAGE_CATALOG),
        "catalog_only_count": len(providers),
        "live_connections_verified": 0,
        "api_calls_performed": 0,
        "category_counts": counts,
        "providers": providers,
        "capability_packages": list_domain_capability_packages(),
        "note": "Inventory is metadata only; verify official API documentation, scopes, eligibility and adapter tests before enabling operations.",
    }
