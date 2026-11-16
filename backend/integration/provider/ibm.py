"""IBM Cloud API configuration-readiness adapter.

This adapter checks for a server-side IBM Cloud IAM API key. It does not
exchange the key for an IAM token or make a live IBM API request.
"""
from __future__ import annotations

import os
from typing import Any, Dict

from ..base import IntegrationProvider
from .readiness import provider_health


class IBMProvider(IntegrationProvider):
    """Reports IBM Cloud credential readiness without claiming connectivity."""

    name = "IBM"
    category = "ENTERPRISE_CLOUD_AND_AI"

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "official_api": "IBM Cloud APIs, watsonx and supported IBM enterprise services",
            "capabilities": [
                "IBM_CLOUD_PLATFORM",
                "IBM_IAM_IDENTITY",
                "IBM_WATSONX_AI",
                "IBM_WATSONX_DATA",
                "IBM_DB2",
                "IBM_CLOUDANT",
                "IBM_CLOUD_OBJECT_STORAGE",
                "IBM_VPC_COMPUTE_NETWORKING",
                "IBM_KUBERNETES_CONTAINERS",
                "IBM_CODE_ENGINE",
                "IBM_API_CONNECT",
                "IBM_KEY_PROTECT_SECURITY",
                "IBM_SECRETS_MANAGER",
                "IBM_MONITORING_ACTIVITY_TRACKER",
                "IBM_RESOURCE_CONTROLLER_CATALOG",
                "IBM_BILLING_USAGE_COST",
            ],
            "auth_method": "IBM Cloud IAM API key; product-specific auth and entitlements may also be required",
            "connection": "NOT_TESTED",
            "setup_guide": "backend/api/global_ecosystem/global_api_ecosystem/ibm_api_ecosystem/README.md",
        }

    def health(self) -> Dict[str, Any]:
        required = ["IBM_CLOUD_API_KEY"]
        configured = bool(os.getenv("IBM_CLOUD_API_KEY", "").strip())
        return provider_health(
            provider=self.name,
            category=self.category,
            configured=configured,
            auth_method="IBM Cloud IAM API key (readiness check only; no token exchange)",
            required_configuration=required,
            capabilities=[
                "CLOUD_PLATFORM", "IAM_IDENTITY", "WATSONX_AI", "WATSONX_DATA",
                "DB2", "CLOUDANT", "CLOUD_OBJECT_STORAGE", "VPC_COMPUTE_NETWORKING",
                "KUBERNETES_CONTAINERS", "CODE_ENGINE", "API_CONNECT",
                "KEY_PROTECT_SECURITY", "SECRETS_MANAGER",
                "MONITORING_ACTIVITY_TRACKER", "RESOURCE_CONTROLLER_CATALOG",
                "BILLING_USAGE_COST",
            ],
        )
