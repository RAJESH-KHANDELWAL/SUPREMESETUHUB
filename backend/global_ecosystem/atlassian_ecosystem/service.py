"""Atlassian domain service: catalog lookup and safe request-plan construction."""
from collections.abc import Mapping
from typing import Any
from .catalog import ATLASSIAN_PRODUCTS, ATLASSIAN_PROVIDER, get_product, list_capabilities
from .constants import (
    PROVIDER_ID, STATUS_CATALOG_ONLY, SENSITIVE_OPERATIONS, SENSITIVE_PRODUCTS,
)
from .models import AtlassianRequestPlan
from .validation import validate_request

class AtlassianEcosystemService:
    provider_id = PROVIDER_ID

    def catalog(self) -> dict:
        return {
            **dict(ATLASSIAN_PROVIDER),
            "products": [
                {"product_id": item.product_id, "display_name": item.display_name,
                 "description": item.description, "api_family": item.api_family,
                 "requires_admin_consent": item.requires_admin_consent}
                for item in ATLASSIAN_PRODUCTS.values()
            ],
            "capabilities": list(list_capabilities()),
        }

    def plan(
        self, product_id: str, operation: str, resource: str,
        payload: Mapping[str, Any] | None = None,
        metadata: Mapping[str, Any] | None = None,
    ) -> AtlassianRequestPlan:
        product = get_product(product_id)
        body, meta = dict(payload or {}), dict(metadata or {})
        validate_request(operation, resource, body)
        op = operation.strip().lower()
        if product.product_id in SENSITIVE_PRODUCTS and not meta.get("admin_consent", False):
            raise PermissionError("This product requires explicit administrator consent in the authorization layer")
        if op in SENSITIVE_OPERATIONS and not meta.get("explicit_confirmation", False):
            raise PermissionError("Destructive or externally visible operations require explicit confirmation")
        return AtlassianRequestPlan(
            product_id=product.product_id,
            operation=op,
            resource=resource.strip(),
            payload=body,
            metadata={
                **meta,
                "provider_id": PROVIDER_ID,
                "provider_status": STATUS_CATALOG_ONLY,
                "execution_required": True,
                "transport_owned_by": "API",
                "authorization_owned_by": "AUTHORIZATION",
                "persistence_owned_by": "DATABASE",
            },
        )
