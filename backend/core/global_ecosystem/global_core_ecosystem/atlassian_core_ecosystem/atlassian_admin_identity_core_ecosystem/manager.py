"""AdminIdentity Core product-family metadata manager."""
from __future__ import annotations
from .service import AdminIdentityCoreService
class AdminIdentityCoreManager:
 def __init__(self)->None:self._service=AdminIdentityCoreService()
 def status(self):return self._service.status()
 def capabilities(self):return self._service.capabilities()
 def authorize_capability(self,capability,context=None):return self._service.authorize_capability(capability,context)
def get_manager()->AdminIdentityCoreManager:return AdminIdentityCoreManager()
__all__=["AdminIdentityCoreManager","get_manager"]
