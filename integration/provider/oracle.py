"""Oracle Cloud Infrastructure integration readiness adapter.

This adapter checks server-side configuration only. It deliberately does not
make network calls or report a successful OCI connection.
"""
from __future__ import annotations

import os
from typing import Any, Dict

from ..base import IntegrationProvider
from .readiness import provider_health


class OracleProvider(IntegrationProvider):
    """OCI request-signing configuration readiness provider."""

    name = "ORACLE"
    category = "CLOUD_DATABASE_AND_ENTERPRISE"

    REQUIRED_ENVIRONMENT = (
        "OCI_TENANCY_OCID",
        "OCI_USER_OCID",
        "OCI_FINGERPRINT",
        "OCI_REGION",
    )
    PRIVATE_KEY_OPTIONS = (
        "OCI_PRIVATE_KEY_FILE",
        "OCI_PRIVATE_KEY_PEM",
    )

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "provider_id": "oracle",
            "capabilities": [
                "OCI_IAM",
                "OCI_COMPUTE",
                "OCI_NETWORKING",
                "OCI_OBJECT_STORAGE",
                "OCI_AUTONOMOUS_DATABASE",
                "OCI_DATABASE",
                "OCI_GENERATIVE_AI",
                "OCI_OBSERVABILITY",
                "ORACLE_FUSION_CLOUD_APPLICATIONS",
            ],
            "auth_method": "OCI API Request Signature Version 1 (RSA-SHA256)",
            "required_environment": list(self.REQUIRED_ENVIRONMENT),
            "private_key_options": list(self.PRIVATE_KEY_OPTIONS),
            "setup_guide": "https://docs.oracle.com/en-us/iaas/Content/API/Concepts/usingapi.htm",
            "live_connection_verified": False,
        }

    def health(self) -> Dict[str, Any]:
        required_present = all(
            os.getenv(key, "").strip()
            for key in self.REQUIRED_ENVIRONMENT
        )
        private_key_present = any(
            os.getenv(key, "").strip()
            for key in self.PRIVATE_KEY_OPTIONS
        )
        configured = required_present and private_key_present

        missing = [
            key for key in self.REQUIRED_ENVIRONMENT
            if not os.getenv(key, "").strip()
        ]
        if not private_key_present:
            missing.append("OCI_PRIVATE_KEY_FILE or OCI_PRIVATE_KEY_PEM")

        report = provider_health(
            provider=self.name,
            category=self.category,
            configured=configured,
            auth_method="OCI API Request Signature Version 1 (RSA-SHA256)",
            required_configuration=[],
            capabilities=[
                "OCI_IAM",
                "OCI_COMPUTE",
                "OCI_NETWORKING",
                "OCI_OBJECT_STORAGE",
                "OCI_DATABASE",
                "OCI_AUTONOMOUS_DATABASE",
                "OCI_GENERATIVE_AI",
            ],
        )
        report["missing_configuration"] = missing
        report["required_configuration"] = list(self.REQUIRED_ENVIRONMENT) + [
            "OCI_PRIVATE_KEY_FILE or OCI_PRIVATE_KEY_PEM"
        ]
        report["status"] = (
            "CONFIGURED_NOT_VERIFIED" if configured else "NEEDS_CONFIGURATION"
        )
        report["authentication"] = (
            "CONFIGURED" if configured else "NOT_CONFIGURED"
        )
        report["connection"] = "NOT_TESTED"
        report["live_connection_verified"] = False
        report["note"] = (
            "OCI credentials appear configured; perform an authenticated OCI API "
            "request before treating the connection as verified."
            if configured else
            "Set the missing server-side OCI environment variables. Never commit "
            "the private key or credentials to the repository."
        )
        return report
