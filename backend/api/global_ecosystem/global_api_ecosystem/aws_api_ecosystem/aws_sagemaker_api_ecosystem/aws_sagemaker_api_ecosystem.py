"""Amazon SageMaker AI service ecosystem catalog metadata.

Catalog metadata only; this module does not authenticate or make network requests.
"""
from __future__ import annotations

AWS_SAGEMAKER_API_ECOSYSTEM = {
    "provider_id": "aws",
    "service_id": "sagemaker",
    "name": "Amazon SageMaker AI API ECOSYSTEM",
    "scope": "Machine learning development and hosting",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "adapter_implemented": False,
    "credential_source": "iam_role_or_managed_secret_store",
}
