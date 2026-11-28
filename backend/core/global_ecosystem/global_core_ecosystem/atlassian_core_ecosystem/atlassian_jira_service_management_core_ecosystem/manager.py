"""JiraServiceManagement Core product-family metadata manager."""
from __future__ import annotations
from .service import JiraServiceManagementCoreService
class JiraServiceManagementCoreManager:
 def __init__(self)->None:self._service=JiraServiceManagementCoreService()
 def status(self):return self._service.status()
 def capabilities(self):return self._service.capabilities()
 def authorize_capability(self,capability,context=None):return self._service.authorize_capability(capability,context)
def get_manager()->JiraServiceManagementCoreManager:return JiraServiceManagementCoreManager()
__all__=["JiraServiceManagementCoreManager","get_manager"]
