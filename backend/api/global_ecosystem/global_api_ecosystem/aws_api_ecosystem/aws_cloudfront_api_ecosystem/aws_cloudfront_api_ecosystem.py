"""Amazon CloudFront service ecosystem catalog metadata.

Catalog metadata only; this module does not authenticate or make network requests.
"""
from __future__ import annotations

AWS_CLOUDFRONT_API_ECOSYSTEM = {
    "provider_id": "aws",
    "service_id": "cloudfront",
    "name": "Amazon CloudFront API ECOSYSTEM",
    "scope": "Content delivery network",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "adapter_implemented": False,
    "credential_source": "iam_role_or_managed_secret_store",
}
