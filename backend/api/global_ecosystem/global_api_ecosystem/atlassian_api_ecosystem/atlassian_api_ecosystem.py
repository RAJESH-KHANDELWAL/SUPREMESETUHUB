"""Atlassian provider API ecosystem metadata; catalog only, not a live connector."""

PROVIDER_API_ECOSYSTEM = {
    "provider_id": "atlassian",
    "name": "ATLASSIAN API ECOSYSTEM",
    "vendor": "Atlassian",
    "families": ["BUSINESS", "DEVELOPER", "TOOLS"],
    "products": [
        "Jira Cloud Platform", "Confluence Cloud",
        "Jira Service Management", "Bitbucket Cloud",
        "Atlassian Administration and identity",
    ],
    "scope": (
        "Provider catalog for Atlassian cloud products. Product availability, "
        "tenant permissions, OAuth scopes and API versions must be verified "
        "before enabling each operation."
    ),
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
}


def list_atlassian_api_ecosystems():
    """Return the declared Atlassian product/API areas."""
    return list(PROVIDER_API_ECOSYSTEM["products"])
