"""Cohere domain service: discovery and safe request-plan creation only."""
from collections.abc import Mapping
from typing import Any
from .catalog import COHERE_CAPABILITIES, COHERE_PRODUCTS, COHERE_PROVIDER, get_product, list_capabilities
from .constants import PROVIDER_ID, STATUS_CATALOG_ONLY, SENSITIVE_OPERATIONS
from .models import CohereRequestPlan
from .validation import validate_request

class CohereEcosystemService:
    provider_id = PROVIDER_ID

    def catalog(self) -> dict:
        return {
            **dict(COHERE_PROVIDER),
            "products": [
                {"product_id": item.product_id, "display_name": item.display_name,
                 "description": item.description, "api_family": item.api_family,
                 "supported_use_cases": list(item.supported_use_cases)}
                for item in COHERE_PRODUCTS.values()
            ],
            "capabilities": list(list_capabilities()),
        }

    def plan(
        self, product_id: str, operation: str,
        payload: Mapping[str, Any] | None = None,
        metadata: Mapping[str, Any] | None = None,
    ) -> CohereRequestPlan:
        product = get_product(product_id)
        body, meta = dict(payload or {}), dict(metadata or {})
        op = operation.strip().lower() if isinstance(operation, str) else ""
        validate_request(product.product_id, op, body)
        if op in SENSITIVE_OPERATIONS and not meta.get("explicit_confirmation", False):
            raise PermissionError("This operation requires explicit confirmation")
        return CohereRequestPlan(
            product_id=product.product_id,
            operation=op,
            payload=body,
            metadata={
                **meta,
                "provider_id": PROVIDER_ID,
                "provider_status": STATUS_CATALOG_ONLY,
                "execution_required": True,
                "transport_owned_by": "API",
                "runtime_owned_by": "AI",
                "orchestration_owned_by": "ENGINE",
                "persistence_owned_by": "DATABASE",
            },
        )
