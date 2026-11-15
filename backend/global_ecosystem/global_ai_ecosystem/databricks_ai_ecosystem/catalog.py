"""Catalog metadata for Databricks AI; API integration is not implied."""

PROVIDER = {
    "id": "databricks_ai",
    "name": "Databricks AI",
    "vendor": "Databricks",
    "category": "enterprise_ai_platform",
    "api_endpoint": None,
    "credential_env": None,
    "models_or_services": ["Mosaic AI","Model serving","Data and AI platform"],
    "integration_status": "catalog_only",
    "notes": "Enterprise data and AI platform; workspace host, serving endpoints and credentials are workspace-specific.",
}
