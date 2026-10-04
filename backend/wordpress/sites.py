"""
MAIN BASE FOUNDATION
WORDPRESS SITE CONFIGURATION

Central definition of registered WordPress websites.

No passwords or database credentials are stored here.
"""

from __future__ import annotations

from backend.wordpress.registry import (
    WordPressSite,
)


# ==============================================================
# RAJESH KHANDELWAL OFFICIAL
# ==============================================================

RAJESH_KHANDELWAL_OFFICIAL = WordPressSite(
    site_id="rajeshkhandelwalofficial",

    domain="rajeshkhandelwalofficial.com",

    site_url="https://rajeshkhandelwalofficial.com",

    provider="Hostinger",

    database_name="u664492673_hRjtu",

    table_prefix="wp_",

    status="REGISTERED",

    environment="production",

    description=(
        "Primary WordPress website connected "
        "to SUPREMESETUHUB."
    ),
)


# ==============================================================
# REGISTERED WORDPRESS SITES
# ==============================================================

WORDPRESS_SITES = [
    RAJESH_KHANDELWAL_OFFICIAL,
]


__all__ = [
    "RAJESH_KHANDELWAL_OFFICIAL",
    "WORDPRESS_SITES",
]
