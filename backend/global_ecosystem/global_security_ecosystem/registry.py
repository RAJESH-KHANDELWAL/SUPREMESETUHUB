"""Thread-safe in-memory security asset registry for development."""
from threading import RLock
from .models import SecurityAsset
class SecurityAssetRegistry:
    def __init__(self):
        self._assets = {}
        self._lock = RLock()
    def register(self, asset: SecurityAsset, *, replace=False):
        with self._lock:
            if asset.asset_id in self._assets and not replace:
                raise ValueError(f"asset already exists: {asset.asset_id}")
            self._assets[asset.asset_id] = asset
    def get(self, asset_id):
        with self._lock:
            return self._assets.get(asset_id)
    def list_all(self):
        with self._lock:
            return tuple(self._assets[k] for k in sorted(self._assets))
