"""Stable metadata and architectural boundaries for the SUPREME API."""
from __future__ import annotations
from typing import Final

API_NAME: Final[str] = "SUPREME API ECOSYSTEM"
API_VERSION: Final[str] = "v1"
API_LAYER_BOUNDARIES: Final[dict[str, str]] = {
    "API": "HTTP entry points, routing, request validation, response schemas, middleware and API documentation",
    "AUTHENTICATION": "Identity verification and credential/session validation; implemented by the separately owned auth layer",
    "AUTHORIZATION": "Permission and policy decisions; implemented by the separately owned authorization/security layer",
    "CORE": "Domain contracts and foundational business rules; not duplicated in the API package",
    "ENGINE": "Execution/orchestration workflows; invoked through stable service interfaces, not copied into API",
    "DATABASE": "Persistence, repositories, schemas and migrations; accessed through explicit interfaces, not owned by API",
}
__all__ = ["API_NAME", "API_VERSION", "API_LAYER_BOUNDARIES"]
