import hmac
import os
from typing import Any, Dict


class SupremeControlService:
    """Secure command bridge for the SUPREME admin owner."""

    _COMMANDS = {
        "platform.status",
        "modules.list",
        "ai.status",
    }

    @staticmethod
    def _configured_token() -> str:
        return os.getenv("SUPREME_CONTROL_TOKEN", "").strip()

    @classmethod
    def validate_token(cls, token: str | None) -> bool:
        configured = cls._configured_token()
        if not configured or not token:
            return False
        return hmac.compare_digest(token, configured)

    @classmethod
    def get_status(cls, controller: Any) -> Dict[str, Any]:
        """Return truthful, non-secret status for the SUPREME control plane."""
        owner_exists = False
        controller_ready = False
        error_code = None
        try:
            if hasattr(controller, "status"):
                controller_status = controller.status()
                controller_ready = bool(
                    isinstance(controller_status, dict)
                    and controller_status.get("initialized")
                )
                owner_exists = bool(
                    isinstance(controller_status, dict)
                    and controller_status.get("owner_exists")
                )
            else:
                owner_exists = bool(controller.exists())
                controller_ready = True
        except Exception:
            error_code = "SUPREME_CONTROLLER_UNAVAILABLE"

        ready = controller_ready and owner_exists
        return {
            "system": "SUPREME",
            "status": "READY" if ready else "DEGRADED",
            "controller": "SUPREME",
            "owner_exists": owner_exists,
            "controller_ready": controller_ready,
            "control_token_configured": bool(cls._configured_token()),
            "supported_commands": sorted(cls._COMMANDS),
            "unavailable_reason": error_code or (
                None if ready else "SUPREME_OWNER_OR_CONTROLLER_NOT_READY"
            ),
        }

    @classmethod
    def execute_command(cls, controller: Any, command: str, payload: Dict[str, Any] | None = None) -> Dict[str, Any]:
        selected = (command or "").strip()
        payload = payload or {}

        if selected not in cls._COMMANDS:
            raise ValueError(f"Unsupported command: {selected}")

        if selected == "platform.status":
            return cls.get_status(controller)

        if selected == "modules.list":
            return {
                "command": selected,
                "status": "ok",
                "modules": [
                    "identity",
                    "auth",
                    "users",
                    "business",
                    "projects",
                    "storage",
                    "security",
                    "ai",
                    "dashboard",
                    "supreme",
                ],
            }

        if selected == "ai.status":
            return {
                "command": selected,
                "status": "ok",
                "module": "ai",
                "provider": "MAIN-BASE-FOUNDATION",
                "description": "AI services are controlled through the platform core",
            }

        raise ValueError(f"Command not implemented: {selected}")


__all__ = ["SupremeControlService"]
