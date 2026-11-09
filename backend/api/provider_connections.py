"""Authenticated live-verification endpoints for configured API providers."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException

from backend.integration.registry import IntegrationRegistry

router = APIRouter(prefix="/api/v1/integrations/providers", tags=["Provider Connections"])
registry = IntegrationRegistry()


@router.get("/{provider}/status")
def provider_configuration_status(provider: str):
    """Return secret-safe configuration readiness for one provider."""
    adapter = registry.get(provider)
    if adapter is None:
        raise HTTPException(status_code=404, detail="INTEGRATION_PROVIDER_NOT_FOUND")
    return adapter.health()


@router.post("/{provider}/verify")
def verify_provider_connection(provider: str):
    """Perform a real provider API check using deployment-managed credentials.

    This route never accepts secrets from the browser and never returns access
    tokens. Verification is request-scoped; it does not persist credentials.
    """
    adapter = registry.get(provider)
    if adapter is None:
        raise HTTPException(status_code=404, detail="INTEGRATION_PROVIDER_NOT_FOUND")
    verifier = getattr(adapter, "verify_connection", None)
    if not callable(verifier):
        raise HTTPException(status_code=501, detail="LIVE_VERIFICATION_NOT_IMPLEMENTED_FOR_PROVIDER")
    return verifier()


__all__ = ["router"]
