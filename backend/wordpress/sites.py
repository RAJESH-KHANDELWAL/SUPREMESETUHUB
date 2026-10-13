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
# DR RAJESH KHANDELWAL IBC
# ==============================================================

DR_RAjesh_KHANDELWAL_IBC = WordPressSite(
    site_id="drrajeshkhandelwalibc",
    domain="drrajeshkhandelwalibc.com",
    site_url="https://drrajeshkhandelwalibc.com",
    provider="Hostinger",
    database_name=None,  # Fill only after verifying the live Hostinger database name.
    table_prefix="wp_",
    status="PENDING_CONNECTION",
    environment="production",
    description=(
        "Second independent domain gate for SUPREMESETUHUB; "
        "database credentials must be configured as private environment variables."
    ),
)


# ==============================================================
# REGISTERED WORDPRESS SITES
# ==============================================================

WORDPRESS_SITES = [
    RAJESH_KHANDELWAL_OFFICIAL,
    DR_RAjesh_KHANDELWAL_IBC,
]


__all__ = [
    "RAJESH_KHANDELWAL_OFFICIAL",
    "DR_RAjesh_KHANDELWAL_IBC",
    "WORDPRESS_SITES",
]
