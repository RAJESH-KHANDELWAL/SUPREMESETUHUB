"""Microsoft Core domain taxonomy and deterministic product assignment."""
from __future__ import annotations
from collections import Counter
from typing import Any
from .catalog import get_microsoft_core_catalog

DOMAIN_DEFINITIONS: dict[str, dict[str, str]] = {
"PROVIDER_GOVERNANCE": {"name":"Provider Governance and Product Lifecycle","purpose":"Microsoft provider identity, product registration, lifecycle, readiness and governance."},
"IDENTITY_AND_ADMINISTRATION": {"name":"Identity, Entra ID and Administration","purpose":"Entra ID, tenants, OAuth metadata, directory, roles, devices and administration boundaries."},
"MICROSOFT_365_AND_COLLABORATION": {"name":"Microsoft 365 and Workspace Collaboration","purpose":"Office, Outlook, Teams, Planner, OneDrive, SharePoint and Microsoft Graph resource families."},
"AZURE_COMPUTE_AND_APPLICATION_HOSTING": {"name":"Azure Compute and Application Hosting","purpose":"Virtual machines, containers, App Service, Functions and application hosting."},
"AZURE_NETWORKING": {"name":"Azure Networking and DNS","purpose":"Virtual networks, connectivity, DNS, routing, load balancing and edge metadata."},
"AZURE_DATA_AND_STORAGE": {"name":"Azure Storage, Databases and Data Platforms","purpose":"Object and file storage, queues, managed databases, data integration and analytics platforms."},
"AI_ML_AND_INTELLIGENCE": {"name":"Microsoft AI, Copilot and Machine Learning","purpose":"Azure AI, Copilot product families, model services, AI governance and machine learning."},
"ANALYTICS_AND_OBSERVABILITY": {"name":"Analytics, Power BI and Observability","purpose":"Power BI, Fabric, monitoring, logging, telemetry and business intelligence."},
"DEVELOPER_AND_APPLICATION_PLATFORM": {"name":"Developer Tools and Application Platforms","purpose":"Azure DevOps, GitHub-related Microsoft offerings, Visual Studio, Power Platform and app lifecycle."},
"WINDOWS_AND_ENDPOINTS": {"name":"Windows, PC and Endpoint Ecosystem","purpose":"Windows client and server, endpoint management, deployment and device experiences."},
"SECURITY_PRIVACY_AND_COMPLIANCE": {"name":"Security, Defender, Purview and Compliance","purpose":"Defender, Sentinel, Entra security, Purview, privacy, risk and compliance boundaries."},
"ADVERTISING_COMMERCE_AND_MONETIZATION": {"name":"Advertising, Commerce and Monetization","purpose":"Microsoft advertising, commercial marketplace, commerce and publisher monetization."},
"SEARCH_AND_BROWSER_DISCOVERY": {"name":"Bing, Edge, Search and Discovery","purpose":"Bing search, Edge browser, discovery and web experiences."},
"GAMING_AND_MEDIA": {"name":"Xbox, Gaming and Media","purpose":"Xbox services, gaming subscriptions, game distribution and media experiences."},
"BUSINESS_EDUCATION_AND_ENTERPRISE": {"name":"Business, Education and Enterprise Services","purpose":"Dynamics 365, industry clouds, education, enterprise management and business applications."},
"PAYMENTS_BILLING_AND_SUBSCRIPTIONS": {"name":"Payments, Billing and Subscriptions","purpose":"Azure billing, Microsoft commerce accounts, licensing and subscription metadata."},
"DEVICES_AND_HARDWARE": {"name":"Surface, Devices and Hardware","purpose":"Surface, accessories, device families and hardware lifecycle."},
"LANGUAGE_ACCESSIBILITY_AND_PRODUCTIVITY": {"name":"Language, Accessibility and Productivity","purpose":"Translation, accessibility, assistive technology and productivity utilities."},
"SPECIALTY_AND_CROSS_PRODUCT": {"name":"Specialty and Cross-Product Services","purpose":"Cross-cutting or not-yet-classified Microsoft offerings requiring explicit review."},
}

def list_microsoft_domain_inventory() -> list[dict[str, Any]]:
    catalog = get_microsoft_core_catalog()
    result = []
    for product in catalog["children"]:
        domain_id = product.get("domain_id", "SPECIALTY_AND_CROSS_PRODUCT")
        definition = DOMAIN_DEFINITIONS.get(domain_id, DOMAIN_DEFINITIONS["SPECIALTY_AND_CROSS_PRODUCT"])
        result.append({**product, "core_domain_id": domain_id, "core_domain_name": definition["name"], "domain_assignment": "EXPLICIT_PRODUCT_REGISTRY"})
    return result

def microsoft_domain_summary() -> dict[str, Any]:
    inventory = list_microsoft_domain_inventory()
    counts = Counter(item["core_domain_id"] for item in inventory)
    return {
        "success": True,
        "domain_count": len(DOMAIN_DEFINITIONS),
        "offering_count": len(inventory),
        "assigned_offering_count": sum(1 for item in inventory if item["core_domain_id"] in DOMAIN_DEFINITIONS),
        "unmapped_offering_ids": [],
        "domains": [{"domain_id": key, **value, "offering_count": counts.get(key, 0)} for key, value in DOMAIN_DEFINITIONS.items()],
        "live_connections_verified": 0,
        "note": "Domain classification is metadata only; it does not establish API availability, entitlement, authorization or live connectivity.",
    }
