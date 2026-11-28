"""Registration readiness and input validation; never submits or charges."""
from __future__ import annotations
from typing import Any
from ..resource_adapter import BadaBusinessResourceAdapter

class BadaBusinessRegistrationCoreService:
    def __init__(self, adapter: BadaBusinessResourceAdapter | None = None) -> None:
        self.adapter = adapter or BadaBusinessResourceAdapter()
    def validate(self, payload: dict[str, Any]) -> dict[str, Any]:
        errors = self.adapter.validate_registration(payload)
        return {"success": not errors, "status": "VALIDATION_ONLY" if not errors else "INVALID_INPUT", "errors": errors, "registration_submitted": False, "payment_processed": False}
