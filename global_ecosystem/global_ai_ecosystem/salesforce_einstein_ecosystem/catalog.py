"""Catalog metadata for Salesforce Einstein; API integration is not implied."""

PROVIDER = {
    "id": "salesforce_einstein",
    "name": "Salesforce Einstein",
    "vendor": "Salesforce",
    "category": "enterprise_ai_platform",
    "api_endpoint": None,
    "credential_env": None,
    "models_or_services": ["Einstein AI","Agentforce","CRM AI workflows"],
    "integration_status": "catalog_only",
    "notes": "Enterprise CRM AI platform; APIs, permissions and org configuration are Salesforce-instance specific.",
}
