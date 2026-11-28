"""Static product Core configuration; runtime credentials belong in secret management."""

from . import CORE_STATUS, LIVE_CONNECTION, PRODUCT_ID

CONFIG = {
    "provider": "cloudflare",
    "product_id": PRODUCT_ID,
    "status": CORE_STATUS,
    "live_connection": LIVE_CONNECTION,
}

__all__ = ["CONFIG"]
