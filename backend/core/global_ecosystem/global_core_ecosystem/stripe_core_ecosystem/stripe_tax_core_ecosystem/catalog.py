"""Tax Core child catalog for Stripe."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

STRIPE_TAX_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": "STRIPE-TAX-CORE-ECOSYSTEM",
    "name": "STRIPE TAX CORE ECOSYSTEM",
    "provider": "stripe",
    "ecosystem_type": "PROVIDER_CORE_SERVICE",
    "parent_id": "STRIPE-CORE-ECOSYSTEM",
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_tax_api_ecosystem",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_tax_core_ecosystem",
    "capabilities": ["TAX_CALCULATION_BOUNDARY", "TAX_CONFIGURATION_METADATA"],
    "status": "CORE_CATALOG_ONLY",
    "connected": False,
    "security_boundary": {
        "credentials_owned_by": "API_RUNTIME_OR_MANAGED_SECRET_STORE",
        "payment_data_persisted_in_core": False,
        "tenant_isolation_required": True,
        "audit_required": True,
    },
}

def get_catalog() -> dict[str, Any]:
    """Return a defensive copy of this Stripe Core child registration."""
    return deepcopy(STRIPE_TAX_CORE_ECOSYSTEM)

__all__ = ["STRIPE_TAX_CORE_ECOSYSTEM", "get_catalog"]
