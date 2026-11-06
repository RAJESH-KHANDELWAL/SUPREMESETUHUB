"""AWS CodePipeline service ecosystem catalog metadata.

Catalog metadata only; this module does not authenticate or make network requests.
"""
from __future__ import annotations

AWS_CODEPIPELINE_API_ECOSYSTEM = {
    "provider_id": "aws",
    "service_id": "codepipeline",
    "name": "AWS CodePipeline API ECOSYSTEM",
    "scope": "Continuous delivery pipelines",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "adapter_implemented": False,
    "credential_source": "iam_role_or_managed_secret_store",
}
