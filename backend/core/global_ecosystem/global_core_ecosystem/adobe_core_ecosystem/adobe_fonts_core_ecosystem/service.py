"""Read-only Core status surface; no provider API calls."""


def adobe_fonts_core_status() -> dict[str, object]:
    return {"provider":"adobe","product_key":"adobe_fonts","product_name":"Adobe Fonts","package_status":"SCAFFOLDED","live_connection_verified":False,"credentials_configured":False}
