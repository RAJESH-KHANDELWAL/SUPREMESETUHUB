"""Microsoft provider-owned API ecosystem metadata.

Catalog metadata only. This module does not authenticate or make network requests.
"""
from __future__ import annotations

MICROSOFT_API_ECOSYSTEM = {
    "provider_id": "microsoft",
    "name": "MICROSOFT API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "live_connection_verified": False,
    "platforms": [
        "Microsoft 365", "Azure Portal", "Microsoft Entra",
        "Microsoft Graph", "Power Platform", "Microsoft Store"
    ],
    "api_families": [
        "identity_oauth", "microsoft_graph", "outlook_mail_calendar",
        "teams", "onedrive_sharepoint", "excel_word", "planner",
        "azure_compute", "azure_app_service", "azure_functions",
        "azure_blob", "azure_sql_cosmos", "azure_dns", "azure_ai",
        "security_defender", "devops"
    ],
    "related_ecosystems": [
        "AI", "APP", "BUSINESS", "CLOUD", "COMMUNICATION", "DATABASE",
        "DEVELOPER", "HOSTING", "SECURITY", "SERVER", "STORAGE",
        "WEB", "WEBSITE"
    ],
    "adapter_path": "backend/integrations/providers/microsoft.py",
    "credential_source": "environment_or_managed_secret_store",
}
