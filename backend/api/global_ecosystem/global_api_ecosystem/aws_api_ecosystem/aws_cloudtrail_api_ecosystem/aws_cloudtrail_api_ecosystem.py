"""AWS CloudTrail service ecosystem catalog metadata.

Catalog metadata only; this module does not authenticate or make network requests.
"""
from __future__ import annotations

AWS_CLOUDTRAIL_API_ECOSYSTEM = {
    "provider_id": "aws",
    "service_id": "cloudtrail",
    "name": "AWS CloudTrail API ECOSYSTEM",
    "scope": "Audit and account activity",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "adapter_implemented": False,
    "credential_source": "iam_role_or_managed_secret_store",
}
