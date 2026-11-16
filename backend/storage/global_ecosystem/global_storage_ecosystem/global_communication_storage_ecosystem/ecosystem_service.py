"""Root storage taxonomy service."""
from .ecosystem_registry import CATEGORY_PACKAGES, validate_category_packages
def ecosystem_status():
    return {"ecosystem":"GLOBAL_COMMUNICATION","category_count":len(CATEGORY_PACKAGES),"missing_packages":validate_category_packages(),"storage_operations_enabled":False}
