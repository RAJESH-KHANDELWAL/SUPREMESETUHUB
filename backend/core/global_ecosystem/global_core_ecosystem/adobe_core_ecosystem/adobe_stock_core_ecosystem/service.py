"""Read-only Core status surface; no provider API calls."""


def adobe_stock_core_status() -> dict[str, object]:
    return {"provider":"adobe","product_key":"adobe_stock","product_name":"Adobe Stock","package_status":"SCAFFOLDED","live_connection_verified":False,"credentials_configured":False}
