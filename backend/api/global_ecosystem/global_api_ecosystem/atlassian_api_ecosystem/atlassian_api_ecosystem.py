"""Atlassian provider API ecosystem metadata and family listing."""

PROVIDER_API_ECOSYSTEM = {
    "provider_id": "atlassian",
    "name": "ATLASSIAN API ECOSYSTEM",
    "vendor": "Atlassian",
    "families": [
        "BUSINESS", "DEVELOPER", "TOOLS",
    ],
    "products": [
        "Jira Cloud Platform",
        "Confluence Cloud",
        "Jira Service Management",
        "Bitbucket Cloud",
        "Atlassian Administration and identity APIs",
    ],
    "api_family_paths": [
        "atlassian_jira_api_ecosystem",
        "atlassian_confluence_api_ecosystem",
        "atlassian_jira_service_management_api_ecosystem",
        "atlassian_bitbucket_api_ecosystem",
        "atlassian_admin_identity_api_ecosystem",
    ],
    "scope": (
        "Atlassian cloud product APIs with tenant-specific permissions, "
        "OAuth scopes, product entitlements and API-version boundaries."
    ),
    "status": "CONFIGURATION_READINESS_SCAFFOLD",
    "live_connection_verified": False,
}


def list_atlassian_api_ecosystems():
    """Return the declared Atlassian product/API areas."""
    return list(PROVIDER_API_ECOSYSTEM["products"])


def get_atlassian_api_ecosystem():
    """Return a copy of provider metadata for catalog consumers."""
    return {
        **PROVIDER_API_ECOSYSTEM,
        "products": list(PROVIDER_API_ECOSYSTEM["products"]),
        "api_family_paths": list(PROVIDER_API_ECOSYSTEM["api_family_paths"]),
        "families": list(PROVIDER_API_ECOSYSTEM["families"]),
    }
