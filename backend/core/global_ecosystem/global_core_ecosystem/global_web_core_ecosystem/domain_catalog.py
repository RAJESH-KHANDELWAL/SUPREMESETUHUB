"""Provider-neutral taxonomy for the global web ecosystem."""
from __future__ import annotations
from copy import deepcopy

DOMAIN_DEFINITIONS = (
    ("WEB_GOVERNANCE", "Web Governance and Lifecycle", "Ownership, classification, lifecycle and standards metadata."),
    ("WEB_INFRASTRUCTURE", "Web Infrastructure", "Infrastructure capability and service classification."),
    ("DOMAINS_AND_DNS", "Domains and DNS", "Domain identity, registration lifecycle, DNS zones and records."),
    ("WEB_HOSTING_AND_DEPLOYMENT", "Web Hosting and Deployment", "Hosting models, deployment targets and release metadata."),
    ("WEB_SERVERS_AND_RUNTIME", "Web Servers and Runtime", "Server roles, runtime families and compatibility metadata."),
    ("CDN_AND_EDGE", "CDN and Edge", "Content delivery, edge compute and geographic delivery metadata."),
    ("WEB_PROTOCOLS_AND_STANDARDS", "Web Protocols and Standards", "HTTP, HTTPS, TLS, web standards and protocol capability metadata."),
    ("WEB_SECURITY_AND_PRIVACY", "Web Security and Privacy", "TLS posture, WAF, identity, privacy and security control metadata."),
    ("WEB_DEVELOPMENT", "Web Development", "Frontend, backend, frameworks, build and development capabilities."),
    ("CMS_AND_WEBSITE_PLATFORMS", "CMS and Website Platforms", "Content management and website platform classification."),
    ("WEB_APPLICATIONS", "Web Applications", "Application types, web experiences and application capability metadata."),
    ("SEARCH_AND_INDEXING", "Search and Indexing", "Crawling, indexing, discoverability and structured metadata."),
    ("WEB_ANALYTICS_AND_OBSERVABILITY", "Web Analytics and Observability", "Usage measurement, telemetry, logs and performance signals."),
    ("WEB_PERFORMANCE_AND_RELIABILITY", "Web Performance and Reliability", "Caching, availability, latency and reliability objectives."),
    ("WEB_STORAGE_AND_ASSETS", "Web Storage and Assets", "Static assets, media delivery and storage capability classification."),
    ("WEB_API_INTEROPERABILITY", "Web API Interoperability", "API styles, integration patterns and interoperability metadata."),
    ("BROWSER_AND_CLIENT_COMPATIBILITY", "Browser and Client Compatibility", "Browser engines, client support and compatibility matrices."),
    ("WEB_ACCESSIBILITY_AND_INCLUSION", "Web Accessibility and Inclusion", "Accessibility standards and inclusive web capability metadata."),
    ("WEB_IDENTITY_AND_ACCESS", "Web Identity and Access", "Identity federation, authentication and authorization concepts."),
    ("WEB_COMMERCE_AND_MONETIZATION", "Web Commerce and Monetization", "Commerce, checkout, subscription and monetization capability metadata."),
    ("WEB_COMPLIANCE_AND_JURISDICTION", "Web Compliance and Jurisdiction", "Legal, regulatory, data residency and jurisdiction metadata."),
)
def list_domain_inventory() -> list[dict]:
    return [{"domain_id": key, "name": name, "description": description,
             "layer": "CORE", "implementation_mode": "SHARED_METADATA_TAXONOMY"}
            for key, name, description in DOMAIN_DEFINITIONS]
def get_domain(domain_id: str) -> dict | None:
    key = str(domain_id).strip().upper()
    return next((item for item in list_domain_inventory() if item["domain_id"] == key), None)
def domain_summary() -> dict:
    items = list_domain_inventory()
    return {"domain_count": len(items), "domain_ids": [x["domain_id"] for x in items]}
