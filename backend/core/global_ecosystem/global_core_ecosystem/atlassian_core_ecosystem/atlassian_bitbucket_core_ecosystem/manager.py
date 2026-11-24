"""Bitbucket Core product-family metadata manager."""
from __future__ import annotations
from .service import BitbucketCoreService
class BitbucketCoreManager:
 def __init__(self)->None:self._service=BitbucketCoreService()
 def status(self):return self._service.status()
 def capabilities(self):return self._service.capabilities()
 def authorize_capability(self,capability,context=None):return self._service.authorize_capability(capability,context)
def get_manager()->BitbucketCoreManager:return BitbucketCoreManager()
__all__=["BitbucketCoreManager","get_manager"]
