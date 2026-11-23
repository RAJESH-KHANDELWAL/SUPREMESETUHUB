"""Provider-neutral shape for Cloudflare product Core metadata."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CloudflareProductCoreContract:
    product_id: str
    capabilities: tuple[str, ...]
    live_connection: bool = False

    def supports(self, capability: str) -> bool:
        return capability in self.capabilities


__all__ = ["CloudflareProductCoreContract"]
