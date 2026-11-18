"""Framework-neutral read-only status handlers."""
from ..ecosystem_service import CategoryService
def get_status()->dict:return CategoryService().describe()
def get_health()->dict:return CategoryService().health()
