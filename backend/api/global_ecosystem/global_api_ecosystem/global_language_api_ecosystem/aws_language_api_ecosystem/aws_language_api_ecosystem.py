"""Amazon Web Services provider mapping for the Global Language API Ecosystem.

Catalog metadata only. Verify current official product documentation,
regional availability, terms, and API access before implementing an adapter.
"""
PROVIDER_ID = "aws"
PROVIDER_NAME = "Amazon Web Services"
CATEGORY_ID = "LANGUAGE"
CATEGORY_NAME = "GLOBAL LANGUAGE API ECOSYSTEM"
PROVIDER_CATALOG_PATH = "backend/api/global_ecosystem/global_api_ecosystem/global_aws_api_ecosystem"
CATEGORY_CATALOG_PATH = "backend/api/global_ecosystem/global_api_ecosystem/global_language_api_ecosystem"
SCOPE = "Provider-to-language-category mapping. Individual language, translation, speech, or detection capabilities must be verified against official documentation."
IMPLEMENTATION_STATUS = "CATALOG_ONLY"
API_DOCUMENTATION_VERIFIED = False
LIVE_CONNECTION_VERIFIED = False

AWS_LANGUAGE_API_ECOSYSTEM = {
    "provider_id": PROVIDER_ID,
    "provider_name": PROVIDER_NAME,
    "family": "LANGUAGE",
    "status": IMPLEMENTATION_STATUS,
    "api_documentation_verified": API_DOCUMENTATION_VERIFIED,
    "live_connection_verified": LIVE_CONNECTION_VERIFIED,
}
