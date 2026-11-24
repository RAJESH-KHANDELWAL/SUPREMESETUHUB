"""Atlassian product and capability catalog; entries do not imply live access."""
from types import MappingProxyType
from .constants import (
    PROVIDER_ID, PROVIDER_NAME, DOMAIN_VERSION, STATUS_CATALOG_ONLY,
    PRODUCT_JIRA, PRODUCT_CONFLUENCE, PRODUCT_JSM, PRODUCT_BITBUCKET, PRODUCT_ADMIN,
)
from .models import AtlassianProduct

ATLASSIAN_PRODUCTS = MappingProxyType({
    PRODUCT_JIRA: AtlassianProduct(PRODUCT_JIRA, "Jira Cloud", "Projects, issues, workflows and agile work management.", "Jira Cloud Platform REST API"),
    PRODUCT_CONFLUENCE: AtlassianProduct(PRODUCT_CONFLUENCE, "Confluence Cloud", "Spaces, pages, knowledge bases and collaborative documentation.", "Confluence Cloud REST API"),
    PRODUCT_JSM: AtlassianProduct(PRODUCT_JSM, "Jira Service Management", "Service projects, customer requests, queues and service workflows.", "Jira Service Management REST API"),
    PRODUCT_BITBUCKET: AtlassianProduct(PRODUCT_BITBUCKET, "Bitbucket Cloud", "Workspaces, repositories, pull requests and pipelines.", "Bitbucket Cloud REST API"),
    PRODUCT_ADMIN: AtlassianProduct(PRODUCT_ADMIN, "Atlassian Administration and identity", "Organization, directory, managed-account and administrative operations where available.", "Atlassian Admin and identity APIs", requires_admin_consent=True),
})

ATLASSIAN_CAPABILITIES = MappingProxyType({
    "jira_projects": (PRODUCT_JIRA, "List and inspect Jira projects."),
    "jira_issues": (PRODUCT_JIRA, "Create, read and update Jira issues subject to project permissions."),
    "jira_workflows": (PRODUCT_JIRA, "Inspect workflow metadata and transitions."),
    "confluence_spaces": (PRODUCT_CONFLUENCE, "Discover Confluence spaces."),
    "confluence_pages": (PRODUCT_CONFLUENCE, "Read and manage pages subject to space restrictions."),
    "jsm_requests": (PRODUCT_JSM, "Manage service requests subject to agent and customer permissions."),
    "bitbucket_repositories": (PRODUCT_BITBUCKET, "Discover repositories in authorized workspaces."),
    "bitbucket_pull_requests": (PRODUCT_BITBUCKET, "Inspect and manage pull requests subject to repository permissions."),
    "admin_identity": (PRODUCT_ADMIN, "Administrative identity and organization operations; requires separate approval."),
})

ATLASSIAN_PROVIDER = MappingProxyType({
    "provider_id": PROVIDER_ID,
    "provider_name": PROVIDER_NAME,
    "domain_version": DOMAIN_VERSION,
    "products": tuple(ATLASSIAN_PRODUCTS),
    "status": STATUS_CATALOG_ONLY,
    "live_connection_verified": False,
})

def get_product(product_id: str) -> AtlassianProduct:
    key = str(product_id or "").strip().lower()
    try:
        return ATLASSIAN_PRODUCTS[key]
    except KeyError as exc:
        raise KeyError(f"Unknown Atlassian product: {product_id}") from exc

def list_products() -> tuple[AtlassianProduct, ...]:
    return tuple(ATLASSIAN_PRODUCTS.values())

def list_capabilities(product_id: str | None = None) -> tuple[dict, ...]:
    result = tuple(
        {"capability_id": key, "product_id": value[0], "description": value[1]}
        for key, value in ATLASSIAN_CAPABILITIES.items()
    )
    if product_id is not None:
        key = str(product_id).strip().lower()
        result = tuple(row for row in result if row["product_id"] == key)
    return result
