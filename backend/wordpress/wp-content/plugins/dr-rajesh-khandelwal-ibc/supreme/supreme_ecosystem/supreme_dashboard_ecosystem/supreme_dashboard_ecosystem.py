"""Backend-side manifest for the SUPREME Dashboard Ecosystem module."""
MODULE_NAME = "SUPREME DASHBOARD ECOSYSTEM"
PARENT_MODULE = "SUPREME ECOSYSTEM"
ROOT_MODULE = "SUPREME"
PARENT_BRAND = "DR RAJESH KHANDELWAL IBC"

def module_manifest() -> dict:
    return {
        "module": MODULE_NAME,
        "parent_module": PARENT_MODULE,
        "root_module": ROOT_MODULE,
        "parent_brand": PARENT_BRAND,
        "wordpress_entrypoint": "supreme_dashboard_ecosystem.php",
    }
