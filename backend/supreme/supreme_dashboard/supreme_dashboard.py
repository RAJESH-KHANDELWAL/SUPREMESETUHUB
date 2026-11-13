"""Backend-side manifest for the SUPREME Dashboard module."""
MODULE_NAME = "SUPREME DASHBOARD"
PARENT_MODULE = "SUPREME"
PARENT_BRAND = "DR RAJESH KHANDELWAL IBC"

def module_manifest() -> dict:
    return {
        "module": MODULE_NAME,
        "parent_module": PARENT_MODULE,
        "parent_brand": PARENT_BRAND,
        "wordpress_entrypoint": "supreme_dashboard.php",
    }
