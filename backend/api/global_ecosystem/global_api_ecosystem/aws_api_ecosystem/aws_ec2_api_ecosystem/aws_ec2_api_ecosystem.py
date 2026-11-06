"""Amazon EC2 service ecosystem catalog metadata.

Catalog metadata only; this module does not authenticate or make network requests.
"""
from __future__ import annotations

AWS_EC2_API_ECOSYSTEM = {
    "provider_id": "aws",
    "service_id": "ec2",
    "name": "Amazon EC2 API ECOSYSTEM",
    "scope": "Virtual compute instances",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "adapter_implemented": False,
    "credential_source": "iam_role_or_managed_secret_store",
}
