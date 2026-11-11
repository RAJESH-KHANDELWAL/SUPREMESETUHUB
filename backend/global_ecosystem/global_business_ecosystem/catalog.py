"""Master catalog for Bharat-to-global business domains and connected packages."""
from __future__ import annotations
from copy import deepcopy
from .constants import ECOSYSTEM_ID, ECOSYSTEM_NAME, STATUS_CATALOGED

BUSINESS_ECOSYSTEMS = (
    {
        "id": "global_bada_business_ecosystem",
        "name": "GLOBAL BADA BUSINESS ECOSYSTEM",
        "category": "business_education_and_provider_resources",
        "package_path": "backend.global_ecosystem.global_bada_business_ecosystem",
        "relationship": "connected_provider_business_vertical",
        "status": "CODE_CONNECTED_RESOURCE_CATALOG",
        "source_of_truth": "backend.global_ecosystem.global_bada_business_ecosystem",
    },
    {
        "id": "global_company_companies_ecosystem",
        "name": "GLOBAL COMPANY & COMPANIES ECOSYSTEM",
        "category": "companies_and_corporate",
        "package_path": "backend.global_ecosystem.global_company_companies_ecosystem",
        "relationship": "business_domain_namespace",
        "status": "CATALOG_NAMESPACE",
    },
    {
        "id": "global_organizations_ecosystem",
        "name": "GLOBAL ORGANIZATIONS ECOSYSTEM",
        "category": "organizations_and_institutions",
        "package_path": "backend.global_ecosystem.global_organizations_ecosystem",
        "relationship": "business_domain_namespace",
        "status": "CATALOG_NAMESPACE",
    },
    {
        "id": "global_finance_ecosystem",
        "name": "GLOBAL FINANCE ECOSYSTEM",
        "category": "finance_and_fintech",
        "package_path": "backend.global_ecosystem.global_finance_ecosystem",
        "relationship": "business_domain_namespace",
        "status": "CATALOG_NAMESPACE",
    },
    {
        "id": "global_payment_ecosystem",
        "name": "GLOBAL PAYMENT ECOSYSTEM",
        "category": "payments_and_commerce",
        "package_path": "backend.global_ecosystem.global_payment_ecosystem",
        "relationship": "business_domain_namespace",
        "status": "CATALOG_NAMESPACE",
    },
)

BUSINESS_CATEGORIES = (
    "business_strategy_and_management",
    "entrepreneurship_and_startups",
    "companies_and_corporate",
    "organizations_and_institutions",
    "business_education_and_training",
    "network_marketing_and_direct_selling",
    "affiliate_and_partner_marketing",
    "sales_and_customer_relationships",
    "marketing_and_branding",
    "finance_accounting_and_tax",
    "payments_and_commerce",
    "marketplaces_and_ecommerce",
    "human_resources_and_workforce",
    "legal_compliance_and_governance",
    "supply_chain_and_operations",
    "franchising_and_licensing",
    "professional_and_consulting_services",
    "social_enterprise_and_nonprofit",
    "international_trade_and_cross_border_business",
    "digital_and_platform_business",
    "research_frontier_and_enterprise_business",
)

def list_business_ecosystems(*, category: str | None = None) -> tuple[dict, ...]:
    """Return defensive copies of registered business namespaces."""
    items = BUSINESS_ECOSYSTEMS
    if category:
        key = category.strip().lower()
        items = tuple(item for item in items if item["category"] == key)
    return tuple(deepcopy(item) for item in items)

def get_catalog() -> dict:
    """Return the umbrella catalog and explicit connection boundaries."""
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "ecosystem_name": ECOSYSTEM_NAME,
        "layer": "GLOBAL_ECOSYSTEM",
        "status": STATUS_CATALOGED,
        "geographic_scope": [
            "bharat_india", "south_asia", "asia_pacific", "middle_east",
            "africa", "europe", "north_america", "latin_america_caribbean",
            "oceania", "global_cross_border",
        ],
        "maturity_scope": [
            "basic_normal", "standard", "professional", "advanced", "expert",
            "enterprise_industrial", "research", "frontier", "supreme_long_horizon",
        ],
        "categories": list(BUSINESS_CATEGORIES),
        "ecosystems": list_business_ecosystems(),
        "ecosystem_count": len(BUSINESS_ECOSYSTEMS),
        "connected_provider_ecosystems": ["global_bada_business_ecosystem"],
        "architecture_ownership": {
            "ecosystem": "business taxonomy, catalog and namespace relationships",
            "api": "HTTP interfaces and transport contracts",
            "core": "shared business rules and stable domain contracts",
            "engine": "orchestration and runtime execution",
            "database": "persistence and data access",
            "security_identity": "authentication, authorization, secrets and audit",
        },
    }

__all__ = ["BUSINESS_ECOSYSTEMS", "BUSINESS_CATEGORIES", "get_catalog", "list_business_ecosystems"]
