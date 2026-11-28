"""Provider-neutral taxonomy for the global website ecosystem."""
from __future__ import annotations

DOMAIN_DEFINITIONS = (
    ("WEBSITE_GOVERNANCE", "Website Governance and Lifecycle", "Ownership, classification, lifecycle, environments and change-control metadata."),
    ("DOMAIN_NAME_MANAGEMENT", "Domain Name Management", "Domain registration references, renewal lifecycle, ownership and transfer metadata."),
    ("DNS_AND_ZONE_MANAGEMENT", "DNS and Zone Management", "DNS zones, records, delegation, resolution and change metadata."),
    ("SHARED_HOSTING", "Shared Website Hosting", "Shared hosting plans, isolation boundaries and resource capability metadata."),
    ("CLOUD_HOSTING", "Cloud Website Hosting", "Cloud hosting models, infrastructure dependencies and service capability metadata."),
    ("MANAGED_HOSTING", "Managed Website Hosting", "Managed hosting responsibilities, support boundaries and service-level metadata."),
    ("STATIC_HOSTING", "Static Website Hosting", "Static site hosting, asset publishing and origin capability metadata."),
    ("WEBSITE_BUILDERS", "Website Builders", "Hosted builders, templates, themes, site editing and export capability metadata."),
    ("CONTENT_MANAGEMENT_SYSTEMS", "Content Management Systems", "CMS platforms, content models, extension and publishing capability metadata."),
    ("HEADLESS_CMS", "Headless CMS", "API-first content delivery and decoupled publishing metadata."),
    ("WEB_SERVER_RUNTIME", "Web Server and Runtime", "Web server roles, language runtimes, process models and compatibility metadata."),
    ("DEPLOYMENT_RELEASES", "Deployment and Releases", "Build artifacts, deployment targets, release channels and rollback metadata."),
    ("CI_CD_AND_AUTOMATION", "CI/CD and Website Automation", "Build pipelines, deployment automation and approval boundaries."),
    ("TLS_CERTIFICATES", "TLS Certificates and HTTPS", "Certificate lifecycle, HTTPS posture and renewal responsibility metadata."),
    ("WAF_AND_DDOS", "Web Application Firewall and DDoS", "Application-layer filtering, DDoS protection and security capability metadata."),
    ("IDENTITY_ACCESS_AND_SECRETS", "Website Identity, Access and Secrets", "Authentication, authorization, service identities and external secret references."),
    ("CDN_AND_EDGE_DELIVERY", "CDN and Edge Delivery", "Content delivery networks, edge caching and geographic delivery metadata."),
    ("CACHING_AND_OPTIMIZATION", "Caching and Website Optimization", "Browser/server caching, compression, image optimization and performance budgets."),
    ("AVAILABILITY_AND_RECOVERY", "Availability, Backup and Recovery", "Availability objectives, backup references, recovery and continuity metadata."),
    ("SEO_AND_INDEXING", "SEO and Search Indexing", "Crawling, indexing, canonical URLs, sitemaps and structured metadata."),
    ("WEB_ANALYTICS_AND_TAGGING", "Website Analytics and Tagging", "Analytics ownership, tag governance, consent and measurement metadata."),
    ("ACCESSIBILITY_AND_COMPLIANCE", "Website Accessibility and Compliance", "Accessibility standards, privacy, cookies, legal notices and jurisdiction metadata."),
    ("WEBSITE_COMMERCE", "Website Commerce", "Storefront, checkout, catalog and commerce capability classification; no payment execution."),
    ("WEBSITE_INTEGRATIONS", "Website Integrations", "External integration inventory and dependency metadata; no API transport."),
    ("WEBSITE_MIGRATION", "Website Migration", "Migration planning, redirects, content portability and cutover metadata."),
    ("MULTI_SITE_AND_MULTI_TENANCY", "Multi-site and Multi-tenancy", "Multi-site architecture, tenant isolation and domain mapping metadata."),
)

def list_domain_inventory() -> list[dict]:
    return [
        {"domain_id": key, "name": name, "description": description,
         "layer": "CORE", "implementation_mode": "SHARED_METADATA_TAXONOMY"}
        for key, name, description in DOMAIN_DEFINITIONS
    ]

def get_domain(domain_id: str) -> dict | None:
    key = str(domain_id).strip().upper()
    return next((item for item in list_domain_inventory() if item["domain_id"] == key), None)

def domain_summary() -> dict:
    items = list_domain_inventory()
    return {"domain_count": len(items), "domain_ids": [item["domain_id"] for item in items]}
