"""Cloudflare product Core package metadata; no live operations are enabled."""

PRODUCT_ID = __name__.rsplit(".", 1)[-1].removesuffix("_cloudflare_core_ecosystem")
CORE_STATUS = "CORE_CATALOG_ONLY"
LIVE_CONNECTION = False

__all__ = ["PRODUCT_ID", "CORE_STATUS", "LIVE_CONNECTION"]
