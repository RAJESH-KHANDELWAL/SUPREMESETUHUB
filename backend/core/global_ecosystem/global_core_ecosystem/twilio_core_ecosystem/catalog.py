"""Canonical Twilio provider catalog; metadata only, no API transport."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

API_CATALOG_PATH = "backend/api/global_ecosystem/global_api_ecosystem/twilio_api_ecosystem/twilio_api_ecosystem.py"
COMMUNICATION_API_PATH = "backend/api/global_ecosystem/global_api_ecosystem/global_communication_api_ecosystem/twilio_communication_api_ecosystem"
TOOLS_API_PATH = "backend/api/global_ecosystem/global_api_ecosystem/global_tools_api_ecosystem/twilio_tools_api_ecosystem"

TWILIO_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": "TWILIO-CORE-ECOSYSTEM",
    "name": "TWILIO CORE ECOSYSTEM",
    "provider_id": "twilio",
    "provider": "Twilio",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "ecosystem_type": "PROVIDER_CORE",
    "status": "REGISTERED_CATALOG_ONLY",
    "enabled": True,
    "api_catalog_ref": API_CATALOG_PATH,
    "capabilities": [
        "PROVIDER_IDENTITY", "PRODUCT_DISCOVERY", "COMMUNICATION_DOMAIN_CLASSIFICATION",
        "TENANT_CONNECTION_METADATA", "READINESS_METADATA", "POLICY_BOUNDARY",
        "DEPENDENCY_DISCOVERY", "MASTER_CATALOG_ALIGNMENT",
    ],
    "product_families": [
        {"product_id": "twilio_messaging", "name": "Programmable Messaging", "family": "MESSAGING", "status": "CORE_CATALOG_ONLY", "api_ref": COMMUNICATION_API_PATH},
        {"product_id": "twilio_voice", "name": "Programmable Voice", "family": "VOICE", "status": "CORE_CATALOG_ONLY", "api_ref": COMMUNICATION_API_PATH},
        {"product_id": "twilio_video", "name": "Programmable Video", "family": "VIDEO", "status": "CORE_CATALOG_ONLY", "api_ref": COMMUNICATION_API_PATH},
        {"product_id": "twilio_verify", "name": "Verify", "family": "IDENTITY_VERIFICATION", "status": "CORE_CATALOG_ONLY", "api_ref": COMMUNICATION_API_PATH},
        {"product_id": "twilio_sendgrid", "name": "SendGrid Email API", "family": "EMAIL", "status": "CORE_CATALOG_ONLY", "api_ref": TOOLS_API_PATH, "availability_note": "Separate SendGrid product/account entitlement; not assumed included in Twilio API access."},
    ],
    "category_refs": [
        {"category": "COMMUNICATION", "path": COMMUNICATION_API_PATH},
        {"category": "TOOLS", "path": TOOLS_API_PATH},
    ],
    "layer_ownership": {
        "core": "Provider identity, product taxonomy, policy metadata and readiness",
        "api": "Authentication, SDK/HTTP transport, webhooks and response normalization",
        "engine": "Execution, retries, queues and scheduling",
        "database": "Durable tenant and communication records",
        "storage": "Media and message artifacts",
    },
    "live_connection_verified": False,
    "credentials_configured": False,
    "api_transport_in_core": False,
}

def get_catalog() -> dict[str, Any]:
    return deepcopy(TWILIO_CORE_ECOSYSTEM)

def list_products(*, enabled_only: bool = False) -> list[dict[str, Any]]:
    items = get_catalog()["product_families"]
    return [item for item in items if not enabled_only or item.get("enabled", True)]
