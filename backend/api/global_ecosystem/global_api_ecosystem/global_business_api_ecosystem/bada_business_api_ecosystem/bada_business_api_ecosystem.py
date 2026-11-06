"""Bada Business provider link-ecosystem metadata."""

PROVIDER_API_ECOSYSTEM = {
    "provider_id": "bada_business",
    "name": "BADA BUSINESS API ECOSYSTEM",
    "vendor": "Bada Business",
    "family": "BUSINESS",
    "category_catalog_path": "backend/api/global_ecosystem/global_api_ecosystem/global_business_api_ecosystem",
    "product_api_path": "backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem",
    "scope": (
        "Curated link directory for official Bada Business pages, courses, "
        "products, services, referrals, partner resources and API documentation."
    ),
    "status": "LINK_CATALOG_SCAFFOLD",
    "official_api_verified": False,
    "live_connection_verified": False,
}

def get_bada_business_api_ecosystem():
    return dict(PROVIDER_API_ECOSYSTEM)
