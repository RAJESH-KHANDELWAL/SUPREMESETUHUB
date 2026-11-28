"""Application security facade and operational policy registry.

This facade does not replace authentication, database, or infrastructure
implementations. Security controls are reported only when they are actually
configured and can be checked.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from backend.infrastructure.security.service import (
    SecurityService as SecurityInfrastructureService,
)

from backend.security.connection import SecurityConnection
from backend.security.model import SecurityCheck, SecurityHealth, SecurityInfo


class SecurityService:
    """Coordinate security policy records, adapters, and health diagnostics."""

    def __init__(
        self,
        infrastructure: SecurityInfrastructureService | None = None,
        connection: SecurityConnection | None = None,
    ) -> None:
        self.infrastructure = infrastructure
        self.connection = connection or SecurityConnection()
        self._initialized = False

    def initialize(self) -> dict[str, Any]:
        """Initialize policy metadata storage and report its actual state."""
        try:
            if self.infrastructure is None:
                self.infrastructure = SecurityInfrastructureService()
            self._initialized = True
            return {
                "success": True,
                "security": "SUPREMESETUHUB",
                "status": "INITIALIZED",
                "backing_service": "backend.infrastructure.security.SecurityService",
                "enforcement": "REQUIRES_PER_CONTROL_CONFIGURATION_AND_TESTING",
            }
        except Exception:
            self._initialized = False
            return {
                "success": False,
                "security": "SUPREMESETUHUB",
                "status": "UNAVAILABLE",
                "enforcement": "FAIL_CLOSED",
            }

    def create_policy(
        self,
        name: str,
        security_type: str,
        *,
        resource_type: str = "",
        resource_id: str = "",
        provider: str = "",
        status: str = "PLANNED",
        enabled: bool = False,
        description: str = "",
    ) -> SecurityInfo:
        if not self._initialized:
            result = self.initialize()
            if not result["success"]:
                raise RuntimeError("SECURITY_STORAGE_UNAVAILABLE")
        if not name.strip() or not security_type.strip():
            raise ValueError("POLICY_NAME_AND_TYPE_REQUIRED")
        assert self.infrastructure is not None
        record = self.infrastructure.create(
            name=name.strip(),
            security_type=security_type.strip().upper(),
            resource_type=resource_type.strip(),
            resource_id=resource_id.strip(),
            provider=provider.strip(),
            status=status.strip().upper(),
            enabled=enabled,
            description=description.strip(),
        )
        return SecurityInfo.from_record(record.__dict__)

    def get_policy(self, security_id: str) -> SecurityInfo | None:
        infrastructure = self._get_infrastructure()
        record = infrastructure.get(security_id)
        return SecurityInfo.from_record(record.__dict__) if record else None

    def list_policies(self) -> list[SecurityInfo]:
        records = self._get_infrastructure().list_all()
        return [SecurityInfo.from_record(record.__dict__) for record in records]

    def update_policy_status(self, security_id: str, status: str) -> SecurityInfo | None:
        if not status.strip():
            raise ValueError("POLICY_STATUS_REQUIRED")
        record = self._get_infrastructure().update_status(security_id, status.strip().upper())
        return SecurityInfo.from_record(record.__dict__) if record else None

    def set_policy_enabled(self, security_id: str, enabled: bool) -> SecurityInfo | None:
        record = self._get_infrastructure().update_enabled(security_id, bool(enabled))
        return SecurityInfo.from_record(record.__dict__) if record else None

    def delete_policy(self, security_id: str) -> bool:
        return self._get_infrastructure().delete(security_id)

    def register_adapter(self, name: str, adapter: Any) -> None:
        self.connection.register(name, adapter)

    def unregister_adapter(self, name: str) -> bool:
        return self.connection.unregister(name)

    def diagnostics(self) -> dict[str, Any]:
        checks: list[SecurityCheck] = []
        checks.append(SecurityCheck(
            "policy_storage",
            "READY" if self._initialized else "NOT_INITIALIZED",
            "Policy metadata storage initialization only; not a security enforcement control.",
        ))
        registry = self.connection.connect()
        checks.append(SecurityCheck(
            "external_adapters",
            registry["status"],
            f'{registry["healthy_adapters"]}/{registry["registered_adapters"]} registered adapters healthy.',
        ))
        status = "READY" if self._initialized and registry["status"] == "CONNECTED" else "CONFIGURATION_REQUIRED"
        health = SecurityHealth(status, tuple(checks), datetime.now(timezone.utc))
        return {
            "success": True,
            "security": "SUPREMESETUHUB",
            **health.as_dict(),
            "adapter_registry": registry,
            "disclaimer": "Diagnostics are not a penetration test, audit, or certification.",
        }

    def initialize_status(self) -> dict[str, Any]:
        return self.diagnostics()

    def _get_infrastructure(self) -> SecurityInfrastructureService:
        if not self._initialized:
            result = self.initialize()
            if not result["success"] or self.infrastructure is None:
                raise RuntimeError("SECURITY_STORAGE_UNAVAILABLE")
        assert self.infrastructure is not None
        return self.infrastructure


__all__ = ["SecurityService"]
