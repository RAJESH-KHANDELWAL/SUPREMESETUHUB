"""Python companion manifest for the SUPREMESETUHUB WordPress connector.

Runs only in the Python backend environment; WordPress does not execute .py.
"""
from __future__ import annotations

def wordpress_connector_manifest() -> dict:
    return {
        "system": "SUPREMESETUHUB",
        "connector": "WordPress",
        "runtime_file": "supremesetuhub_wordpress_connector.php",
        "status_endpoint": "/wp-json/supremesetuhub/v1/connector-status",
        "wordpress_executes": "PHP",
        "python_role": "Backend companion manifest",
    }
