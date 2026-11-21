"""Side-effect-free metadata result contract."""
from typing import Any, TypedDict
class CoreResult(TypedDict):
    ecosystem_id: str
    status: str
    connected: bool
    data: dict[str, Any]
def result(ecosystem_id: str, data: dict[str, Any], status: str = "CATALOG_ONLY") -> CoreResult:
    return {"ecosystem_id": ecosystem_id, "status": status, "connected": False, "data": data}
__all__ = ["CoreResult", "result"]
