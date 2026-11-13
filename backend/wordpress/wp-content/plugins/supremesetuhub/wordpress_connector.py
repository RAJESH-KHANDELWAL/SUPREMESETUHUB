"""Python-side connector manifest for SUPREMESETUHUB.

WordPress runs the PHP connector. This Python file is for the Python backend
that may communicate with the central WordPress hub through its REST API.
"""
from __future__ import annotations

from typing import Any

HUB_NAME = "SUPREMESETUHUB"
HUB_BRAND = "👑 DR RAJESH KHANDELWAL IBC 👑"
STATUS_ENDPOINT = "/wp-json/supremesetuhub/v1/connector-status"

COMPANION_PLUGINS = {
    "supreme": {
        "brand": "SUPREME by SUPREMESETUHUB",
        "plugin_file": "supreme/supreme.php",
    },
    "supreme_ecosystem": {
        "brand": "SUPREME ECOSYSTEM by SUPREMESETUHUB",
        "plugin_file": "supreme-ecosystem/supreme-ecosystem.php",
    },
}

def connector_manifest() -> dict[str, Any]:
    return {
        "hub": HUB_NAME,
        "brand": HUB_BRAND,
        "status_endpoint": STATUS_ENDPOINT,
        "companion_plugins": COMPANION_PLUGINS,
    }
