"""Amazon VPC service ecosystem catalog metadata.

Catalog metadata only; this module does not authenticate or make network requests.
"""
from __future__ import annotations

AWS_VPC_API_ECOSYSTEM = {
    "provider_id": "aws",
    "service_id": "vpc",
    "name": "Amazon VPC API ECOSYSTEM",
    "scope": "Virtual networking",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "adapter_implemented": False,
    "credential_source": "iam_role_or_managed_secret_store",
}
