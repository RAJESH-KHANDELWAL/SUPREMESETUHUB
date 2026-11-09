"""Execution engine for Bada Business program operations.

ENGINE owns operation dispatch and injected execution handlers. It does not
own canonical program facts, business eligibility rules, HTTP transport,
registration, billing, or provider credentials.
"""
from __future__ import annotations

from typing import Any, Callable

from backend.bada_business_ecosystem.platform_resources.catalog import (
    get_program as get_canonical_program,
    list_programs as list_canonical_programs,
)

SUPPORTED_OPERATIONS = frozenset({
    "GET_PROGRAM",
    "LIST_PROGRAMS",
    "PREPARE_PROGRAM",
    "EXECUTE_PROGRAM",
})


class ProgramEngineError(RuntimeError):
    """Base error for program engine operations."""


class ProgramEngineNotConfigured(ProgramEngineError):
    """Raised when an execution handler has not been injected."""


class ProgramEngineValidationError(ValueError):
    """Raised when an operation payload is invalid."""


class BadaBusinessProgramEngine:
    provider = "BADA_BUSINESS"
    layer = "ENGINE"

    def __init__(
        self,
        handlers: dict[str, Callable[[dict[str, Any]], Any]] | None = None,
    ):
        self._handlers = {
            str(key).strip().upper(): value
            for key, value in (handlers or {}).items()
        }

    def health(self) -> dict[str, Any]:
        return {
            "provider": self.provider,
            "layer": self.layer,
            "status": "READY",
            "canonical_catalog_available": True,
            "configured_operations": sorted(
                name for name, handler in self._handlers.items()
                if callable(handler)
            ),
            "live_provider_connection_verified": False,
        }

    @staticmethod
    def _program_id(payload: dict[str, Any]) -> str:
        value = payload.get("program_id")
        if not isinstance(value, str) or not value.strip():
            raise ProgramEngineValidationError("program_id is required")
        return value.strip().lower()

    @staticmethod
    def _safe_program(program: dict[str, Any]) -> dict[str, Any]:
        # Return a shallow copy so callers cannot mutate canonical catalog state.
        return dict(program)

    def describe(self) -> dict[str, Any]:
        return {
            "engine": "BADA_BUSINESS_PROGRAM_ENGINE",
            "layer": self.layer,
            "operations": sorted(SUPPORTED_OPERATIONS),
            "execution_mode": "INJECTED_HANDLER",
            "catalog_source": "backend.bada_business_ecosystem.platform_resources.catalog",
        }

    def execute(
        self,
        operation: str,
        payload: dict[str, Any] | None = None,
        *,
        dry_run: bool = False,
    ) -> dict[str, Any]:
        if not isinstance(operation, str) or not operation.strip():
            raise ProgramEngineValidationError("operation is required")
        action = operation.strip().upper()
        if action not in SUPPORTED_OPERATIONS:
            raise ProgramEngineValidationError(f"Unsupported operation: {action}")
        data = dict(payload or {})
        if not isinstance(payload, (dict, type(None))):
            raise ProgramEngineValidationError("payload must be a mapping")

        if action == "LIST_PROGRAMS":
            programs = list_canonical_programs()
            return {
                "success": True,
                "operation": action,
                "source": "canonical_catalog",
                "count": len(programs),
                "data": [self._safe_program(item) for item in programs],
                "executed": False,
            }

        program_id = self._program_id(data)
        program = get_canonical_program(program_id)
        if program is None:
            raise ProgramEngineValidationError(
                f"Unknown Bada Business program_id: {program_id}"
            )

        if action == "GET_PROGRAM":
            return {
                "success": True,
                "operation": action,
                "source": "canonical_catalog",
                "data": self._safe_program(program),
                "executed": False,
            }

        if action == "PREPARE_PROGRAM":
            return {
                "success": True,
                "operation": action,
                "program_id": program_id,
                "program": self._safe_program(program),
                "dry_run": True,
                "executed": False,
                "requires_core_approval": True,
                "note": "Preparation only; no enrollment, payment, or provider side effect.",
            }

        # EXECUTE_PROGRAM is intentionally handler-gated and opt-in.
        if dry_run:
            return {
                "success": True,
                "operation": action,
                "program_id": program_id,
                "dry_run": True,
                "executed": False,
                "handler_required": True,
            }

        handler = self._handlers.get(action)
        if not callable(handler):
            raise ProgramEngineNotConfigured(
                "EXECUTE_PROGRAM handler is not configured"
            )
        result = handler({
            **data,
            "program_id": program_id,
            "program": self._safe_program(program),
        })
        return {
            "success": True,
            "operation": action,
            "program_id": program_id,
            "executed": True,
            "provider_connection_verified": False,
            "result": result,
        }


# Compatibility name retained for existing imports.
ProviderEngine = BadaBusinessProgramEngine
