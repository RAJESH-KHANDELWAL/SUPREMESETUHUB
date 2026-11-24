"""Read-only capability registry helpers."""
from __future__ import annotations
from ..catalog import CAPABILITIES

class CapabilityRegistry:
    def list(self):
        return {name: dict(metadata) for name, metadata in CAPABILITIES.items()}

    def get(self, capability: str):
        if not isinstance(capability, str):
            return None
        item = CAPABILITIES.get(capability.strip().lower())
        return dict(item) if item is not None else None

    def supports(self, capability: str) -> bool:
        return self.get(capability) is not None
