"""SUPREMESETUHUB central WordPress hub manifest."""
from __future__ import annotations

HUB_NAME = "SUPREMESETUHUB"
HUB_LABEL = "👑 SUPREMESETUHUB 👑"
HUB_BRAND = "👑 DR RAJESH KHANDELWAL IBC 👑"
WORDPRESS_ENTRYPOINT = "supremesetuhub.php"
WORDPRESS_MENU = {
    "type": "top_level",
    "slug": "supremesetuhub",
    "label": HUB_LABEL,
    "capability": "manage_options",
    "icon": "custom-crown-svg-base64",
    "version": "1.3.3",
    "integrated_connector": "supremesetuhub_api_catalog_connector.php",
    "legacy_standalone_connector": False,
    "dashboard_slug": "supremesetuhub-dashboard",
    "dashboard_label": "👑 Dashboard 👑",
    "connector_menu_slug": "supremesetuhub-connector",
    "connector_menu_label": "API & Catalog Connector",
}
COMPANION_PLUGIN = {
    "name": "DR RAJESH KHANDELWAL IBC",
    "entrypoint": "dr-rajesh-khandelwal-ibc.php",
    "menu_slug": "dr-rajesh-khandelwal-ibc-dashboard",
}
PLUGINS = {
    "supreme": "SUPREME by SUPREMESETUHUB",
    "supreme_ecosystem": "SUPREME ECOSYSTEM by SUPREMESETUHUB",
}


def hub_manifest() -> dict:
    return {
        "hub": HUB_NAME,
        "label": HUB_LABEL,
        "brand": HUB_BRAND,
        "wordpress_entrypoint": WORDPRESS_ENTRYPOINT,
        "wordpress_menu": WORDPRESS_MENU,
        "companion_plugin": COMPANION_PLUGIN,
        "plugins": PLUGINS,
    }
