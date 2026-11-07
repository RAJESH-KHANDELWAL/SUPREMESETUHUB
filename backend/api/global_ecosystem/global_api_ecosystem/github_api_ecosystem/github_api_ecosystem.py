"""GitHub provider-owned API ecosystem metadata.

Catalog and architecture metadata only; this module performs no authentication
or network requests.
"""
from __future__ import annotations

GITHUB_API_ECOSYSTEM = {
    "provider_id": "github",
    "name": "GITHUB API ECOSYSTEM",
    "status": "AUTHENTICATED_REST_CLIENT_CONFIGURATION_REQUIRED",
    "live_connection_verified": False,
    "purpose": "GitHub REST and GraphQL APIs for repository development, collaboration, automation, apps, security and organization operations",
    "api_families": [
        "github_rest_api_ecosystem",
        "github_graphql_api_ecosystem",
        "github_repositories_api_ecosystem",
        "github_issues_api_ecosystem",
        "github_pull_requests_api_ecosystem",
        "github_actions_api_ecosystem",
        "github_apps_api_ecosystem",
        "github_authentication_api_ecosystem",
        "github_webhooks_api_ecosystem",
        "github_checks_api_ecosystem",
        "github_security_api_ecosystem",
        "github_organizations_api_ecosystem",
    ],
    "shared_categories": ["DEVELOPER", "SOFTWARE", "TOOLS"],
    "existing_code_path": "backend/api/connectors.py",
    "existing_code_scope": "Public repository status checking only; not full authenticated GitHub API integration",
    "credential_source": "environment_or_managed_secret_store",
    "provider_catalog_path": "backend/api/global_ecosystem/global_api_ecosystem/github_api_ecosystem",
}
