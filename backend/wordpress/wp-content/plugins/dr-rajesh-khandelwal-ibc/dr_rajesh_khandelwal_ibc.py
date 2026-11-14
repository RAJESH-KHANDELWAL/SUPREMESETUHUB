"""DR RAJESH KHANDELWAL IBC WordPress plugin manifest."""
from __future__ import annotations

PLUGIN_NAME = "DR RAJESH KHANDELWAL IBC"
PLUGIN_LABEL = "👑 DR RAJESH KHANDELWAL IBC 👑"
WORDPRESS_ENTRYPOINT = "dr-rajesh-khandelwal-ibc.php"
WORDPRESS_MENU = {
    "type": "top_level",
    "slug": "dr-rajesh-khandelwal-ibc-dashboard",
    "label": PLUGIN_LABEL,
    "capability": "manage_options",
    "icon": "custom-crown-svg",
}
SUBMENUS = {
    "supreme_dashboard": {
        "slug": "supreme-dashboard",
        "label": "👑 SUPREME DASHBOARD 👑",
    },
    "supreme_ecosystem_dashboard": {
        "slug": "supreme-ecosystem-dashboard",
        "label": "👑 SUPREME ECOSYSTEM DASHBOARD 👑",
    },
    "four_brand_identities": {
        "slug": "dr-rajesh-khandelwal-ibc-identities",
        "label": "👑 FOUR BRAND IDENTITIES 👑",
    },
    "database_ftp": {
        "slug": "dr-rajesh-khandelwal-ibc-infrastructure",
        "label": "Database & FTP",
    },
    "plugins": {
        "slug": "dr-rajesh-khandelwal-ibc-plugins",
        "label": "🧩 Plugins",
    },
}


def plugin_manifest() -> dict:
    return {
        "plugin": PLUGIN_NAME,
        "label": PLUGIN_LABEL,
        "wordpress_entrypoint": WORDPRESS_ENTRYPOINT,
        "wordpress_menu": WORDPRESS_MENU,
        "submenus": SUBMENUS,
    }
