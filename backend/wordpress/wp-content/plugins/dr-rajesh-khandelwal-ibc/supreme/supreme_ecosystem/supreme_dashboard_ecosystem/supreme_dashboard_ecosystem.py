"""Backend-side manifest for the SUPREME Dashboard Ecosystem module."""
MODULE_NAME = "SUPREME ECOSYSTEM DASHBOARD"
PARENT_MODULE = "SUPREME ECOSYSTEM"
ROOT_MODULE = "SUPREME"
PARENT_BRAND = "DR RAJESH KHANDELWAL IBC"
WORDPRESS_ENTRYPOINT = "supreme_dashboard_ecosystem.php"
WORDPRESS_PARENT_MENU = "dr-rajesh-khandelwal-ibc-dashboard"
WORDPRESS_MENU_SLUG = "supreme-ecosystem-dashboard"
WORDPRESS_MENU_LABEL = "👑 SUPREME ECOSYSTEM DASHBOARD 👑"


def module_manifest() -> dict:
    return {
        "module": MODULE_NAME,
        "parent_module": PARENT_MODULE,
        "root_module": ROOT_MODULE,
        "parent_brand": PARENT_BRAND,
        "wordpress_entrypoint": WORDPRESS_ENTRYPOINT,
        "wordpress_parent_menu": WORDPRESS_PARENT_MENU,
        "wordpress_menu_slug": WORDPRESS_MENU_SLUG,
        "wordpress_menu_label": WORDPRESS_MENU_LABEL,
    }
