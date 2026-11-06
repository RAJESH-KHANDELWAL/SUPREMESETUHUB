"""Amazon SNS service ecosystem catalog metadata.

Catalog metadata only; this module does not authenticate or make network requests.
"""
from __future__ import annotations

AWS_SNS_API_ECOSYSTEM = {
    "provider_id": "aws",
    "service_id": "sns",
    "name": "Amazon SNS API ECOSYSTEM",
    "scope": "Pub/sub messaging and notifications",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "adapter_implemented": False,
    "credential_source": "iam_role_or_managed_secret_store",
}
