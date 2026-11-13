"""SUPREME WordPress connector companion for SUPREMESETUHUB.

This Python module is intended for the SUPREME Python backend. The WordPress
runtime connector is the separate supremesetuhub_wordpress_connector.php file.
"""
from __future__ import annotations

from typing import Any

HUB_NAME = "SUPREMESETUHUB"
SUPREME_BRAND = "SUPREME by SUPREMESETUHUB"
WORDPRESS_STATUS_ENDPOINT = "/wp-json/supremesetuhub/v1/connector-status"

def supreme_wordpress_connector_manifest() -> dict[str, Any]:
    return {
        "hub": HUB_NAME,
        "plugin_brand": SUPREME_BRAND,
        "connector_name": "SUPREME WordPress Connector",
        "wordpress_runtime_connector": "supremesetuhub_wordpress_connector.php",
        "status_endpoint": WORDPRESS_STATUS_ENDPOINT,
        "python_role": "SUPREME backend connector companion",
    }
