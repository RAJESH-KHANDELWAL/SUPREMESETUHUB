"""Catalog metadata for Snowflake Cortex; API integration is not implied."""

PROVIDER = {
    "id": "snowflake_cortex",
    "name": "Snowflake Cortex",
    "vendor": "Snowflake",
    "category": "enterprise_ai_platform",
    "api_endpoint": None,
    "credential_env": None,
    "models_or_services": ["Cortex AI","Cortex Search","Cortex Analyst"],
    "integration_status": "catalog_only",
    "notes": "AI capabilities inside Snowflake; availability depends on cloud region, account and SQL feature support.",
}
