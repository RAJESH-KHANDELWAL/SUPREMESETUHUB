"""Canonical provider metadata registry; no API transport."""
from copy import deepcopy
from typing import Any
GLOBAL_TOOLS_CORE_ECOSYSTEM: dict[str,Any]={
  "ecosystem_id": "GLOBAL-TOOLS-CORE-ECOSYSTEM",
  "name": "GLOBAL TOOLS CORE ECOSYSTEM",
  "parent_id": "GLOBAL-CORE-ECOSYSTEM",
  "status": "REGISTERED",
  "enabled": true,
  "providers": [
    {
      "provider_id": "atlassian",
      "name": "Atlassian",
      "ecosystem_id": "ATLASSIAN-TOOLS-CORE-ECOSYSTEM",
      "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_tools_core_ecosystem/atlassian_tools_core_ecosystem",
      "status": "REGISTERED_CATALOG_ONLY",
      "enabled": true,
      "live_connection_verified": false,
      "capabilities": [
        "PROVIDER_IDENTITY",
        "PRODUCT_DISCOVERY",
        "TENANT_CONNECTION_METADATA",
        "READINESS_METADATA",
        "POLICY_BOUNDARY"
      ]
    },
    {
      "provider_id": "aws",
      "name": "Amazon Web Services",
      "ecosystem_id": "AWS-TOOLS-CORE-ECOSYSTEM",
      "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_tools_core_ecosystem/aws_tools_core_ecosystem",
      "status": "REGISTERED_CATALOG_ONLY",
      "enabled": true,
      "live_connection_verified": false,
      "capabilities": [
        "PROVIDER_IDENTITY",
        "PRODUCT_DISCOVERY",
        "TENANT_CONNECTION_METADATA",
        "READINESS_METADATA",
        "POLICY_BOUNDARY"
      ]
    },
    {
      "provider_id": "crakrevenue",
      "name": "CrakRevenue",
      "ecosystem_id": "CRAKREVENUE-TOOLS-CORE-ECOSYSTEM",
      "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_tools_core_ecosystem/crakrevenue_tools_core_ecosystem",
      "status": "REGISTERED_CATALOG_ONLY",
      "enabled": true,
      "live_connection_verified": false,
      "capabilities": [
        "PROVIDER_IDENTITY",
        "PRODUCT_DISCOVERY",
        "TENANT_CONNECTION_METADATA",
        "READINESS_METADATA",
        "POLICY_BOUNDARY"
      ]
    },
    {
      "provider_id": "exoclick",
      "name": "ExoClick",
      "ecosystem_id": "EXOCLICK-TOOLS-CORE-ECOSYSTEM",
      "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_tools_core_ecosystem/exoclick_tools_core_ecosystem",
      "status": "REGISTERED_CATALOG_ONLY",
      "enabled": true,
      "live_connection_verified": false,
      "capabilities": [
        "PROVIDER_IDENTITY",
        "PRODUCT_DISCOVERY",
        "TENANT_CONNECTION_METADATA",
        "READINESS_METADATA",
        "POLICY_BOUNDARY"
      ]
    },
    {
      "provider_id": "github",
      "name": "GitHub",
      "ecosystem_id": "GITHUB-TOOLS-CORE-ECOSYSTEM",
      "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_tools_core_ecosystem/github_tools_core_ecosystem",
      "status": "REGISTERED_CATALOG_ONLY",
      "enabled": true,
      "live_connection_verified": false,
      "capabilities": [
        "PROVIDER_IDENTITY",
        "PRODUCT_DISCOVERY",
        "TENANT_CONNECTION_METADATA",
        "READINESS_METADATA",
        "POLICY_BOUNDARY"
      ]
    },
    {
      "provider_id": "google",
      "name": "Google",
      "ecosystem_id": "GOOGLE-TOOLS-CORE-ECOSYSTEM",
      "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_tools_core_ecosystem/google_tools_core_ecosystem",
      "status": "REGISTERED_CATALOG_ONLY",
      "enabled": true,
      "live_connection_verified": false,
      "capabilities": [
        "PROVIDER_IDENTITY",
        "PRODUCT_DISCOVERY",
        "TENANT_CONNECTION_METADATA",
        "READINESS_METADATA",
        "POLICY_BOUNDARY"
      ]
    },
    {
      "provider_id": "microsoft",
      "name": "Microsoft",
      "ecosystem_id": "MICROSOFT-TOOLS-CORE-ECOSYSTEM",
      "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_tools_core_ecosystem/microsoft_tools_core_ecosystem",
      "status": "REGISTERED_CATALOG_ONLY",
      "enabled": true,
      "live_connection_verified": false,
      "capabilities": [
        "PROVIDER_IDENTITY",
        "PRODUCT_DISCOVERY",
        "TENANT_CONNECTION_METADATA",
        "READINESS_METADATA",
        "POLICY_BOUNDARY"
      ]
    },
    {
      "provider_id": "openai",
      "name": "OpenAI",
      "ecosystem_id": "OPENAI-TOOLS-CORE-ECOSYSTEM",
      "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_tools_core_ecosystem/openai_tools_core_ecosystem",
      "status": "REGISTERED_CATALOG_ONLY",
      "enabled": true,
      "live_connection_verified": false,
      "capabilities": [
        "PROVIDER_IDENTITY",
        "PRODUCT_DISCOVERY",
        "TENANT_CONNECTION_METADATA",
        "READINESS_METADATA",
        "POLICY_BOUNDARY"
      ]
    },
    {
      "provider_id": "salesforce",
      "name": "Salesforce",
      "ecosystem_id": "SALESFORCE-TOOLS-CORE-ECOSYSTEM",
      "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_tools_core_ecosystem/salesforce_tools_core_ecosystem",
      "status": "REGISTERED_CATALOG_ONLY",
      "enabled": true,
      "live_connection_verified": false,
      "capabilities": [
        "PROVIDER_IDENTITY",
        "PRODUCT_DISCOVERY",
        "TENANT_CONNECTION_METADATA",
        "READINESS_METADATA",
        "POLICY_BOUNDARY"
      ]
    },
    {
      "provider_id": "trafficjunky",
      "name": "TrafficJunky",
      "ecosystem_id": "TRAFFICJUNKY-TOOLS-CORE-ECOSYSTEM",
      "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_tools_core_ecosystem/trafficjunky_tools_core_ecosystem",
      "status": "REGISTERED_CATALOG_ONLY",
      "enabled": true,
      "live_connection_verified": false,
      "capabilities": [
        "PROVIDER_IDENTITY",
        "PRODUCT_DISCOVERY",
        "TENANT_CONNECTION_METADATA",
        "READINESS_METADATA",
        "POLICY_BOUNDARY"
      ]
    },
    {
      "provider_id": "twilio",
      "name": "Twilio",
      "ecosystem_id": "TWILIO-TOOLS-CORE-ECOSYSTEM",
      "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_tools_core_ecosystem/twilio_tools_core_ecosystem",
      "status": "REGISTERED_CATALOG_ONLY",
      "enabled": true,
      "live_connection_verified": false,
      "capabilities": [
        "PROVIDER_IDENTITY",
        "PRODUCT_DISCOVERY",
        "TENANT_CONNECTION_METADATA",
        "READINESS_METADATA",
        "POLICY_BOUNDARY"
      ]
    }
  ],
  "capabilities": [
    "PROVIDER_REGISTRY",
    "PRODUCT_DISCOVERY",
    "DOMAIN_CLASSIFICATION",
    "TENANT_CONNECTION_METADATA",
    "POLICY_GUARDRAILS",
    "READINESS_METADATA"
  ],
  "api_transport_in_core": false,
  "live_connections_verified": 0
}
def get_catalog(): return deepcopy(GLOBAL_TOOLS_CORE_ECOSYSTEM)
def list_providers(): return get_catalog()["providers"]
def get_provider(provider_id):
 k=provider_id.strip().casefold(); return next((x for x in list_providers() if k in (x["provider_id"],x["name"].casefold())),None)
