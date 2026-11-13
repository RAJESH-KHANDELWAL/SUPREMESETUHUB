"""Python companion manifest for the SUPREMESETUHUB WordPress connector.

WordPress executes the PHP connector. This module is intended for the Python
backend and does not run inside WordPress.
"""
HUB_NAME = "SUPREMESETUHUB"
CONNECTOR_NAME = "WordPress"
STATUS_ENDPOINT = "/wp-json/supremesetuhub/v1/connector-status"

def connector_manifest() -> dict:
    return {
        "hub": HUB_NAME,
        "connector": CONNECTOR_NAME,
        "php_runtime_file": "supremesetuhub_wordpress_connector.php",
        "status_endpoint": STATUS_ENDPOINT,
        "wordpress_runtime": "PHP",
    }
