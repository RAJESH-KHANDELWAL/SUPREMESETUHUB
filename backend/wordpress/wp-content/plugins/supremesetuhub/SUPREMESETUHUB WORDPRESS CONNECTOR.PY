"""Python companion for the SUPREMESETUHUB WordPress connector.

The Python backend may use this manifest to identify the WordPress REST
connector. WordPress itself executes the PHP connector file.
"""
from __future__ import annotations

HUB = "SUPREMESETUHUB"
CONNECTOR = "WordPress"
STATUS_ENDPOINT = "/wp-json/supremesetuhub/v1/connector-status"

def connector_manifest() -> dict:
    return {
        "hub": HUB,
        "connector": CONNECTOR,
        "php_runtime_file": "SUPREMESETUHUB WORDPRESS CONNECTOR.PHP",
        "status_endpoint": STATUS_ENDPOINT,
        "wordpress_runtime": "PHP",
    }
