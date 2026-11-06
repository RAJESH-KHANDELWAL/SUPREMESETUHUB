"""AWS Billing and Cost Management service ecosystem catalog metadata.

Catalog metadata only; this module does not authenticate or make network requests.
"""
from __future__ import annotations

AWS_BILLING_COST_API_ECOSYSTEM = {
    "provider_id": "aws",
    "service_id": "billing_cost",
    "name": "AWS Billing and Cost Management API ECOSYSTEM",
    "scope": "Billing, budgets and cost visibility",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "adapter_implemented": False,
    "credential_source": "iam_role_or_managed_secret_store",
}
