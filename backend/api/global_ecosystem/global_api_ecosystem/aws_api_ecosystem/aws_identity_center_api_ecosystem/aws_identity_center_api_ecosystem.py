"""AWS IAM Identity Center service ecosystem catalog metadata.

Catalog metadata only; this module does not authenticate or make network requests.
"""
from __future__ import annotations

AWS_IDENTITY_CENTER_API_ECOSYSTEM = {
    "provider_id": "aws",
    "service_id": "identity_center",
    "name": "AWS IAM Identity Center API ECOSYSTEM",
    "scope": "Workforce identity and SSO",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "adapter_implemented": False,
    "credential_source": "iam_role_or_managed_secret_store",
}
