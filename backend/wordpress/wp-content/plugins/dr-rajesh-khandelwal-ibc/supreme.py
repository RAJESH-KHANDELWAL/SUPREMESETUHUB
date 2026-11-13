"""Python-side manifest for SUPREME.

The WordPress plugin runtime executes supreme.php. This file is a companion
manifest for backend-side Python tooling; it is not executed by WordPress.
"""
PLUGIN_SLUG = "supreme"
PLUGIN_NAME = "SUPREME"
DISPLAY_NAME = "SUPREME by SUPREMESETUHUB"
PARENT_HUB = "SUPREMESETUHUB"
IDENTITY_FOLDERS = [
    "dr_rajesh_khandelwal_ibc",
    "dr_rajesh_khandelwal_ibc_official",
    "rajesh_khandelwal",
    "rajesh_khandelwal_official"
]

def plugin_manifest() -> dict:
    return {
        "slug": PLUGIN_SLUG,
        "name": PLUGIN_NAME,
        "display_name": DISPLAY_NAME,
        "parent_hub": PARENT_HUB,
        "identity_folders": list(IDENTITY_FOLDERS),
        "wordpress_entrypoint": "supreme.php",
    }
