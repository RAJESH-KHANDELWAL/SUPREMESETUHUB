"""Policy boundaries for transport CORE metadata discovery."""
from __future__ import annotations

class TransportCorePolicyError(PermissionError):
    """Raised when a request crosses the transport CORE metadata boundary."""

class TransportCorePolicy:
    OPERATIONAL_CAPABILITIES = frozenset({
        "LIVE_VEHICLE_DISPATCH", "LIVE_TRAIN_CONTROL", "AIR_TRAFFIC_CONTROL",
        "LIVE_BOOKING", "PAYMENT_CAPTURE", "LIVE_FLEET_TRACKING",
        "EMERGENCY_RESPONSE_CONTROL",
    })

    @classmethod
    def require_catalog_capability(cls, capability: str, registered: set[str]) -> None:
        key = capability.strip().upper()
        if not key:
            raise TransportCorePolicyError("CAPABILITY_REQUIRED")
        if key in cls.OPERATIONAL_CAPABILITIES:
            raise TransportCorePolicyError("OPERATIONAL_ACTIONS_NOT_AVAILABLE_IN_CORE")
        if key not in registered:
            raise TransportCorePolicyError("CAPABILITY_NOT_REGISTERED")
