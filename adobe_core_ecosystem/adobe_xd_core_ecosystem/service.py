"""Read-only Core status surface; no provider API calls."""


def adobe_xd_core_status() -> dict[str, object]:
    return {"provider":"adobe","product_key":"adobe_xd","product_name":"Adobe XD","package_status":"SCAFFOLDED","live_connection_verified":False,"credentials_configured":False}
