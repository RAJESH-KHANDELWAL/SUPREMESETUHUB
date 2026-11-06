"""AWS Step Functions service ecosystem catalog metadata.

Catalog metadata only; this module does not authenticate or make network requests.
"""
from __future__ import annotations

AWS_STEP_FUNCTIONS_API_ECOSYSTEM = {
    "provider_id": "aws",
    "service_id": "step_functions",
    "name": "AWS Step Functions API ECOSYSTEM",
    "scope": "Workflow orchestration",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "adapter_implemented": False,
    "credential_source": "iam_role_or_managed_secret_store",
}
