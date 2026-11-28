"""Safe public product map for the SUPREME relationship-first ecosystem.

This is a product-navigation registry, not an adult catalog or commerce backend.
Explicit media, age assurance, orders, provider integrations and playback remain
disabled until their implementation and compliance gates are complete.
"""
from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/products", tags=["SUPREME product ecosystem"])

PRODUCTS = [
    {
        "product_id": "relationship",
        "name": "RELATIONSHIP",
        "sequence": 1,
        "status": "FOUNDATION",
        "access_mode": "standalone_or_combined",
        "audience": "general relationship guidance and resources",
        "capabilities": ["communication_resources", "relationship_books", "wellbeing_education"],
        "age_gate_required": False,
        "public_catalog_enabled": True,
    },
    {
        "product_id": "romance",
        "name": "ROMANCE",
        "sequence": 2,
        "status": "PLANNED",
        "access_mode": "optional_combined_journey_or_standalone",
        "audience": "opt-in romantic resources and non-explicit content",
        "capabilities": ["date_ideas", "romantic_books", "non_explicit_creator_products"],
        "age_gate_required": False,
        "public_catalog_enabled": False,
    },
    {
        "product_id": "intimacy",
        "name": "INTIMACY 18+",
        "sequence": 3,
        "status": "LOCKED_PENDING_COMPLIANCE",
        "access_mode": "standalone_or_optional_combined_journey",
        "audience": "eligible adults only, subject to region-specific law",
        "capabilities": [
            "authorized_adult_media",
            "adult_lifestyle_products",
            "adult_books",
            "rights_cleared_posters_and_prints",
            "creator_storefronts",
        ],
        "age_gate_required": True,
        "region_gate_required": True,
        "performer_consent_and_distribution_rights_required": True,
        "public_catalog_enabled": False,
        "reason_unavailable": "AGE_REGION_RIGHTS_PROVIDER_AND_MODERATION_GATES_NOT_IMPLEMENTED",
    },
    {
        "product_id": "family_safe_store",
        "name": "FAMILY-SAFE STORE",
        "sequence": 4,
        "status": "PLANNED",
        "access_mode": "separate_storefront",
        "audience": "family-appropriate, non-explicit books, posters and general merchandise",
        "capabilities": ["general_books", "non_explicit_posters", "ordinary_merchandise"],
        "age_gate_required": False,
        "must_exclude_explicit_content": True,
        "public_catalog_enabled": False,
    },
    {
        "product_id": "supreme_plus",
        "name": "SUPREME PLUS",
        "sequence": 5,
        "status": "PLANNED",
        "access_mode": "optional_bundle",
        "audience": "eligible users with explicit per-product entitlements",
        "capabilities": ["optional_relationship_romance_bundle", "eligible_adult_product_entitlement"],
        "age_gate_required": True,
        "must_not_bypass_product_gates": True,
        "public_catalog_enabled": False,
    },
]

PROVIDERS = [
    {
        "provider_id": "vicetemple",
        "provider_type": "adult_hosting_candidate",
        "status": "NOT_CONNECTED",
        "integration": "none",
        "requires": [
            "owner_purchases_and_configures_account",
            "written_plan_and_streaming_suitability_confirmation",
            "legal_and_content_policy_review",
            "domain_dns_tls_and_security_setup",
            "deployment_and_load_tests",
        ],
    },
    {
        "provider_id": "faphouse",
        "provider_type": "external_platform_candidate",
        "status": "NOT_CONNECTED",
        "integration": "none",
        "requires": [
            "written_api_or_affiliate_access_confirmation",
            "content_distribution_rights_if_content_is_embedded_or_republished",
            "terms_and_privacy_review",
        ],
    },
    {
        "provider_id": "print_on_demand",
        "provider_type": "commerce_provider_category",
        "status": "EXISTING_INTERNAL_API_REQUIRES_PROVIDER_REVIEW",
        "integration": "existing_print_on_demand_router",
        "requires": [
            "provider_category_approval",
            "rights_and_consent_review_for_each_design",
            "region_and_shipping_rules",
            "checkout_and_fulfillment_tests",
        ],
    },
]


@router.get("/catalog")
def product_catalog():
    """Return non-sensitive navigation metadata; never expose adult media."""
    return {
        "success": True,
        "ecosystem": "SUPREMESETUHUB",
        "combined_journey": ["relationship", "romance", "intimacy"],
        "journey_is_optional": True,
        "standalone_access_supported": True,
        "consent_is_never_inferred": True,
        "minors_must_not_access_explicit_products": True,
        "products": PRODUCTS,
        "commerce": {
            "print_on_demand": "DESIGN_ONLY_UNTIL_PROVIDER_AND_RIGHTS_GATES_PASS",
            "books_and_toys": "CATALOG_AND_CHECKOUT_NOT_YET_ENABLED",
            "adult_media_streaming": "DISABLED_PENDING_AUTHORIZED_CATALOG_AND_COMPLIANCE",
        },
    }


@router.get("/provider-readiness")
def provider_readiness():
    """Expose only high-level integration state; never credentials or private settings."""
    return {"success": True, "providers": PROVIDERS}
