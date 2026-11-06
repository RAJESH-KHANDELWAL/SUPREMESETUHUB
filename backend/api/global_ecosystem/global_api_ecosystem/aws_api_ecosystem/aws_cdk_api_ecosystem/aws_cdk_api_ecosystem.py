"""AWS Cloud Development Kit service ecosystem catalog metadata.

Catalog metadata only; this module does not authenticate or make network requests.
"""
from __future__ import annotations

AWS_CDK_API_ECOSYSTEM = {
    "provider_id": "aws",
    "service_id": "cdk",
    "name": "AWS Cloud Development Kit API ECOSYSTEM",
    "scope": "Infrastructure as code SDK",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "adapter_implemented": False,
    "credential_source": "iam_role_or_managed_secret_store",
}
