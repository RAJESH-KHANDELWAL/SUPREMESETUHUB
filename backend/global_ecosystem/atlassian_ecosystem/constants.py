"""Stable identifiers and policy constants for the Atlassian domain."""
PROVIDER_ID = "atlassian"
PROVIDER_NAME = "Atlassian"
DOMAIN_VERSION = "1.0.0"
STATUS_CATALOG_ONLY = "CATALOG_ONLY"
STATUS_CONFIGURED_NOT_VERIFIED = "CONFIGURED_NOT_VERIFIED"
STATUS_CONNECTED = "CONNECTED"
PRODUCT_JIRA = "jira_cloud"
PRODUCT_CONFLUENCE = "confluence_cloud"
PRODUCT_JSM = "jira_service_management"
PRODUCT_BITBUCKET = "bitbucket_cloud"
PRODUCT_ADMIN = "admin_identity"
SENSITIVE_PRODUCTS = frozenset({PRODUCT_ADMIN})
SENSITIVE_OPERATIONS = frozenset({"delete", "archive", "revoke", "disable", "remove", "transfer"})
