"""Oracle provider API ecosystem catalog and integration contract.

Catalog and configuration metadata only. Live OCI calls are implemented separately
and must be explicitly tested before this provider can be marked connected.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any


PROVIDER_ID = "oracle"
PROVIDER_NAME = "ORACLE API ECOSYSTEM"
PROVIDER_VENDOR = "Oracle"
PROVIDER_CATALOG_PATH = (
    "backend/api/global_ecosystem/global_api_ecosystem/"
    "oracle_api_ecosystem"
)

CATEGORY_CATALOG_PATHS = {
    "AI": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/oracle_ai_api_ecosystem",
    "CLOUD": "backend/api/global_ecosystem/global_api_ecosystem/global_cloud_api_ecosystem/oracle_cloud_api_ecosystem",
    "DATABASE": "backend/api/global_ecosystem/global_api_ecosystem/global_database_api_ecosystem/oracle_database_api_ecosystem",
    "BUSINESS": "backend/api/global_ecosystem/global_api_ecosystem/global_business_api_ecosystem/oracle_business_api_ecosystem",
    "VPS": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem/oracle_vps_api_ecosystem",
}

PROVIDER_API_ECOSYSTEM: dict[str, Any] = {
    "provider_id": PROVIDER_ID,
    "name": PROVIDER_NAME,
    "vendor": PROVIDER_VENDOR,
    "provider_type": "enterprise_cloud_database_and_software_provider",
    "status": "CONFIGURATION_READINESS_SCAFFOLD",
    "implementation_status": "READINESS_ADAPTER_PRESENT_LIVE_API_UNVERIFIED",
    "live_connection_verified": False,
    "provider_catalog_path": PROVIDER_CATALOG_PATH,
    "category_catalog_paths": CATEGORY_CATALOG_PATHS,
    "authentication": {
        "method": "OCI_REQUEST_SIGNATURE_VERSION_1",
        "algorithm": "RSA-SHA256",
        "credential_environment": [
            "OCI_TENANCY_OCID",
            "OCI_USER_OCID",
            "OCI_FINGERPRINT",
            "OCI_REGION",
            "OCI_PRIVATE_KEY_FILE or OCI_PRIVATE_KEY_PEM",
        ],
        "private_key_storage": "environment_or_managed_secret_store",
        "secrets_in_repository": False,
        "request_requirements": [
            "HTTPS",
            "TLS_1_2_OR_HIGHER",
            "signed_authorization_header",
            "date_or_x_date",
            "service_and_region_specific_endpoint",
        ],
        "documentation": [
            "https://docs.oracle.com/en-us/iaas/Content/API/Concepts/usingapi.htm",
            "https://docs.oracle.com/en-us/iaas/Content/API/Concepts/signingrequests.htm",
            "https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm",
        ],
    },
    "endpoint_strategy": {
        "region": "OCI_REGION",
        "endpoint_resolution": "service_and_region_specific",
        "api_version": "service_specific",
        "do_not_assume_single_global_endpoint": True,
    },
    "service_families": {
        "AI": [
            "OCI_GENERATIVE_AI",
            "OCI_AI_SERVICES",
            "OCI_DATA_SCIENCE",
        ],
        "CLOUD": [
            "OCI_COMPUTE",
            "OCI_NETWORKING",
            "OCI_OBJECT_STORAGE",
            "OCI_IAM",
            "OCI_OBSERVABILITY",
        ],
        "DATABASE": [
            "ORACLE_AUTONOMOUS_DATABASE",
            "ORACLE_BASE_DATABASE_SERVICE",
            "ORACLE_MYSQL_HEATWAVE",
            "ORACLE_DATABASE_TOOLS",
        ],
        "BUSINESS": [
            "ORACLE_FUSION_CLOUD_APPLICATIONS",
            "ORACLE_ENTERPRISE_APPLICATION_REST_APIS",
        ],
        "VPS": [
            "OCI_COMPUTE_INSTANCES",
            "OCI_BLOCK_VOLUMES",
            "OCI_VIRTUAL_CLOUD_NETWORKS",
        ],
    },
    "integration_requirements": [
        "official_service_api_reference_review",
        "region_aware_endpoint_resolution",
        "OCI_request_signature_v1_implementation",
        "least_privilege_iam_policy",
        "private_key_secret_management",
        "timeouts_retries_and_rate_limit_handling",
        "unit_tests_with_mocked_responses",
        "opt_in_live_integration_tests",
    ],
    "safety": {
        "never_log_private_keys_or_authorization_headers": True,
        "never_commit_credentials": True,
        "health_check_is_configuration_only": True,
        "live_connection_requires_successful_authenticated_api_test": True,
    },
}

ORACLE_API_ECOSYSTEM: dict[str, Any] = PROVIDER_API_ECOSYSTEM


def get_oracle_api_ecosystem() -> dict[str, Any]:
    """Return an isolated copy of Oracle provider ecosystem metadata."""
    return deepcopy(PROVIDER_API_ECOSYSTEM)


__all__ = [
    "CATEGORY_CATALOG_PATHS",
    "ORACLE_API_ECOSYSTEM",
    "PROVIDER_API_ECOSYSTEM",
    "PROVIDER_CATALOG_PATH",
    "PROVIDER_ID",
    "PROVIDER_NAME",
    "PROVIDER_VENDOR",
    "get_oracle_api_ecosystem",
]
