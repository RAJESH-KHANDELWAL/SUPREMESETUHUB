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
    database_name="u664492673_MzL97",  # Verified from wp-config.php; credentials remain in environment variables.
    table_prefix="wp_",
    status="REGISTERED",
    environment="production",
    description=(
        "Second independent domain gate for SUPREMESETUHUB; "
        "database credentials must be configured as private environment variables."
    ),
)


# ==============================================================
# FUTURE WORDPRESS INSTALLATIONS
# ==============================================================
# These identities/domains are reserved in the registry. No WordPress
# installation, database, or live connection is claimed yet.

RAJESH_KHANDELWAL = WordPressSite(
    site_id="rajeshkhandelwal",
    domain="rajeshkhandelwal.com",
    site_url="https://rajeshkhandelwal.com",
    provider=None,
    database_name=None,
    table_prefix="wp_",
    status="PLANNED",
    environment="production",
    description="Reserved future WordPress installation; not installed or connected yet.",
)

DR_RAjesh_KHANDELWAL_IBC_OFFICIAL = WordPressSite(
    site_id="drrajeshkhandelwalibcofficial",
    domain="drrajeshkhandelwalibcofficial.com",
    site_url="https://drrajeshkhandelwalibcofficial.com",
    provider=None,
    database_name=None,
    table_prefix="wp_",
    status="PLANNED",
    environment="production",
    description="Reserved future WordPress installation; not installed or connected yet.",
)


# ==============================================================
# REGISTERED WORDPRESS SITES
# ==============================================================

WORDPRESS_SITES = [
    RAJESH_KHANDELWAL_OFFICIAL,
    DR_RAjesh_KHANDELWAL_IBC,
    RAJESH_KHANDELWAL,
    DR_RAjesh_KHANDELWAL_IBC_OFFICIAL,
]


__all__ = [
    "RAJESH_KHANDELWAL_OFFICIAL",
    "DR_RAjesh_KHANDELWAL_IBC",
    "RAJESH_KHANDELWAL",
    "DR_RAjesh_KHANDELWAL_IBC_OFFICIAL",
    "WORDPRESS_SITES",
]
