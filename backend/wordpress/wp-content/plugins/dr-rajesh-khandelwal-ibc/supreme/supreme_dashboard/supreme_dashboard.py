"""Backend-side manifest for the SUPREME Dashboard module."""
MODULE_NAME = "SUPREME DASHBOARD"
PARENT_MODULE = "SUPREME"
PARENT_BRAND = "DR RAJESH KHANDELWAL IBC"
WORDPRESS_ENTRYPOINT = "supreme_dashboard.php"
WORDPRESS_PARENT_MENU = "dr-rajesh-khandelwal-ibc"
WORDPRESS_MENU_SLUG = "supreme-dashboard"
WORDPRESS_MENU_LABEL = "👑 SUPREME DASHBOARD 👑"


def module_manifest() -> dict:
    return {
        "module": MODULE_NAME,
        "parent_module": PARENT_MODULE,
        "parent_brand": PARENT_BRAND,
        "wordpress_entrypoint": WORDPRESS_ENTRYPOINT,
        "wordpress_parent_menu": WORDPRESS_PARENT_MENU,
        "wordpress_menu_slug": WORDPRESS_MENU_SLUG,
        "wordpress_menu_label": WORDPRESS_MENU_LABEL,
    }
