"""AWS KMS service ecosystem catalog metadata.

Catalog metadata only; this module does not authenticate or make network requests.
"""
from __future__ import annotations

AWS_KMS_API_ECOSYSTEM = {
    "provider_id": "aws",
    "service_id": "kms",
    "name": "AWS KMS API ECOSYSTEM",
    "scope": "Key management",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "adapter_implemented": False,
    "credential_source": "iam_role_or_managed_secret_store",
}
