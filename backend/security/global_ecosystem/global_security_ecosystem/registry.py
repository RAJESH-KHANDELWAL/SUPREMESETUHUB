"""Thread-safe in-memory SECURITY asset registry; not durable storage."""
from threading import RLock
from .models import SecurityAsset

class SecurityAssetRegistry:
    def __init__(self):
        self._items: dict[str, SecurityAsset] = {}
        self._lock = RLock()

    def register(self, asset: SecurityAsset, *, replace: bool = False):
        if not isinstance(asset, SecurityAsset):
            raise TypeError("asset must be a SECURITY-owned SecurityAsset")
        with self._lock:
            if asset.security_id in self._items and not replace:
                raise ValueError(f"Security asset already registered: {asset.security_id}")
            self._items[asset.security_id] = asset
        return asset

    def get(self, security_id: str):
        key = str(security_id or "").strip()
        if not key:
            raise ValueError("security_id is required")
        with self._lock:
            return self._items.get(key)

    def list(self):
        with self._lock:
            return tuple(self._items[key] for key in sorted(self._items))

    def unregister(self, security_id: str):
        key = str(security_id or "").strip()
        if not key:
            raise ValueError("security_id is required")
        with self._lock:
            return self._items.pop(key, None) is not None

    def status(self):
        with self._lock:
            return {"registered_assets": len(self._items), "registry_type": "IN_MEMORY_RUNTIME_REGISTRY", "durable_persistence": False}

__all__ = ["SecurityAssetRegistry"]
