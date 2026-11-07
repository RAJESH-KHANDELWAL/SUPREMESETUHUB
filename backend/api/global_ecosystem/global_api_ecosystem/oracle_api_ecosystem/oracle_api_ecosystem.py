"""Oracle provider API ecosystem catalog.

This module describes Oracle API families and integration requirements.
It is catalog metadata only: it does not authenticate, make network calls,
or claim that an Oracle tenancy is connected.
"""
from __future__ import annotations

from typing import Any


PROVIDER_ID = "oracle"
PROVIDER_NAME = "ORACLE API ECOSYSTEM"
PROVIDER_VENDOR = "Oracle"

PROVIDER_API_ECOSYSTEM = {
    "provider_id": PROVIDER_ID,
    "name": PROVIDER_NAME,
    "vendor": PROVIDER_VENDOR,
    "provider_type": "enterprise_cloud_and_software_provider",
    "status": "CATALOG_ONLY",
    "implementation_status": "CATALOG_ONLY_UNTIL_ADAPTER_AND_TESTS_PASS",
    "live_connection_verified": False,
    "provider_catalog_path": (
        "backend/api/global_ecosystem/global_api_ecosystem/"
        "oracle_api_ecosystem"
    ),
    "shared_category_ecosystems": {
        "AI": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem",
        "CLOUD": "backend/api/global_ecosystem/global_api_ecosystem/global_cloud_api_ecosystem",
        "DATABASE": "backend/api/global_ecosystem/global_api_ecosystem/global_database_api_ecosystem",
        "BUSINESS": "backend/api/global_ecosystem/global_api_ecosystem/global_business_api_ecosystem",
        "VPS": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
    },
    "authentication": {
        "method": "OCI_REQUEST_SIGNATURE_VERSION_1",
        "algorithm": "RSA-SHA256",
        "credential_material": [
            "tenancy_ocid",
            "user_ocid",
            "api_key_fingerprint",
            "private_key_pem",
        ],
        "private_key_storage": "environment_or_managed_secret_store",
        "secrets_in_repository": False,
        "request_requirements": [
            "HTTPS",
            "TLS_1_2_OR_HIGHER",
            "signed_authorization_header",
            "date_or_x_date",
        ],
        "documentation": [
            "https://docs.oracle.com/en-us/iaas/Content/API/Concepts/usingapi.htm",
            "https://docs.oracle.com/en-us/iaas/Content/API/Concepts/signingrequests.htm",
            "https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm",
        ],
    },
    "endpoint_strategy": {
        "base_url": "https://<service>.<region>.oci.oraclecloud.com",
        "region": "configured_per_tenancy_or_request",
        "api_version": "service_specific",
        "do_not_assume_single_global_endpoint": True,
    },
    "service_families": [
        "AI_AND_MACHINE_LEARNING",
        "CLOUD_INFRASTRUCTURE",
        "COMPUTE",
        "NETWORKING",
        "OBJECT_STORAGE",
        "IDENTITY_AND_ACCESS_MANAGEMENT",
        "DATABASE",
        "AUTONOMOUS_DATABASE",
        "OBSERVABILITY_AND_MONITORING",
        "DEVELOPER_AND_APPLICATION_SERVICES",
        "ENTERPRISE_BUSINESS_APPLICATIONS",
    ],
    "integration_requirements": [
        "official_service_api_reference_review",
        "regional_endpoint_resolution",
        "OCI_request_signing_implementation",
        "least_privilege_iam_policy",
        "secret_manager_configuration",
        "timeouts_retries_and_rate_limit_handling",
        "unit_tests_with_mocked_responses",
        "opt_in_live_integration_tests",
    ],
}


ORACLE_API_ECOSYSTEM: dict[str, Any] = PROVIDER_API_ECOSYSTEM


def get_oracle_api_ecosystem() -> dict[str, Any]:
    """Return a copy of Oracle provider catalog metadata."""
    from copy import deepcopy

    return deepcopy(PROVIDER_API_ECOSYSTEM)


__all__ = [
    "ORACLE_API_ECOSYSTEM",
    "PROVIDER_API_ECOSYSTEM",
    "PROVIDER_ID",
    "PROVIDER_NAME",
    "PROVIDER_VENDOR",
    "get_oracle_api_ecosystem",
]
