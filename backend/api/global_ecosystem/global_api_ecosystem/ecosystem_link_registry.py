"""Shared, non-duplicating crosswalk across the three global ecosystems.

Business categories remain canonical in Global Bada Business.
Legal-entity classes remain canonical in Global Company & Companies.
Platform domains remain canonical in Global Platforms.

These links are classification references only; they do not assert that a
company/platform record exists, is verified, or has a live external connection.
"""
from __future__ import annotations

BUSINESS_TO_PLATFORM_DOMAINS = {
    "ecommerce": ("commerce",),
    "retail-wholesale": ("commerce",),
    "technology-software": ("ai_data", "cloud_infrastructure", "software_development"),
    "telecommunications": ("communication", "cloud_infrastructure"),
    "finance-banking": ("finance_payments",),
    "professional-services": ("work_business",),
    "marketing-media": ("communication", "content_media"),
    "education-training": ("education",),
    "healthcare": ("health_wellness",),
    "transport-logistics": ("travel_transport",),
    "automotive": ("travel_transport",),
    "travel-tourism": ("travel_transport",),
    "arts-entertainment": ("content_media",),
    "food-hospitality": ("commerce", "travel_transport"),
    "real-estate": ("commerce",),
    "agencies-platforms": ("work_business", "commerce", "communication"),
    "government-nonprofit": ("public_services",),
    "adult-entertainment": ("adult_industry",),
    "adult-retail": ("adult_industry", "commerce"),
}

COMPANY_RECORD_CLASSES = ("company", "enterprise", "corporate_group")


def get_ecosystem_linkage(include_adult: bool = False) -> dict:
    """Return the shared taxonomy crosswalk without copying source registries."""
    from .global_bada_business_api_ecosystem.business_catalog import BUSINESS_CATEGORIES
    from .global_platforms_api_ecosystem.catalog import PLATFORM_DOMAINS

    business_categories = [
        item for item in BUSINESS_CATEGORIES
        if include_adult or not item.get("adult_only", False)
    ]
    platform_domains = [
        item for item in PLATFORM_DOMAINS
        if include_adult or not item.get("adult_only", False)
    ]
    visible_platform_ids = {item["domain_id"] for item in platform_domains}

    category_links = []
    for category in business_categories:
        category_id = category["id"]
        mapped_domains = [
            domain_id for domain_id in BUSINESS_TO_PLATFORM_DOMAINS.get(category_id, ())
            if domain_id in visible_platform_ids
        ]
        category_links.append({
            "business_category_id": category_id,
            "business_category_name": category["name"],
            "compatible_company_record_classes": list(COMPANY_RECORD_CLASSES),
            "related_platform_domain_ids": mapped_domains,
            "classification_only": True,
            "adult_only": bool(category.get("adult_only", False)),
        })

    platform_links = []
    for domain in platform_domains:
        domain_id = domain["domain_id"]
        related_categories = [
            item["id"] for item in business_categories
            if domain_id in BUSINESS_TO_PLATFORM_DOMAINS.get(item["id"], ())
        ]
        platform_links.append({
            "platform_domain_id": domain_id,
            "platform_domain_name": domain["name"],
            "related_business_category_ids": related_categories,
            "owner_entity_record_classes": list(COMPANY_RECORD_CLASSES),
            "classification_only": True,
            "adult_only": bool(domain.get("adult_only", False)),
        })

    return {
        "success": True,
        "integration_id": "global_business_company_platform_crosswalk",
        "integration_mode": "shared_read_only_taxonomy_references",
        "canonical_sources": {
            "business_categories": "global_bada_business_api_ecosystem.business_catalog",
            "company_record_classes": "global_company_companies_api_ecosystem.classification_registry",
            "platform_domains": "global_platforms_api_ecosystem.catalog",
            "entity_ownership_relationships": "global_entity_relationships_api_ecosystem",
        },
        "business_category_count": len(business_categories),
        "platform_domain_count": len(platform_domains),
        "company_record_classes": list(COMPANY_RECORD_CLASSES),
        "include_adult": include_adult,
        "adult_policy": "Excluded by default; include_adult only reveals separately classified taxonomy and is not age verification or legal approval.",
        "registry_policy": "No company/platform profiles are created by this crosswalk. Ownership/operator edges remain in the shared entity-relationships ecosystem.",
        "business_category_links": category_links,
        "platform_domain_links": platform_links,
        "live_external_connections": False,
    }
