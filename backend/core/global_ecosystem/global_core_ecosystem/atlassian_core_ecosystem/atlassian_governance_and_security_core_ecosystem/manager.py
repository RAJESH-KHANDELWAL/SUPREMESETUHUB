"""Manager for Atlassian Governance and Security Core domain."""
from __future__ import annotations
from . import DOMAIN_ID
from ...domain_runtime import AtlassianCoreDomainManager
class AtlassianDomainManager(AtlassianCoreDomainManager):
 DOMAIN_ID=DOMAIN_ID
def get_manager()->AtlassianDomainManager: return AtlassianDomainManager()
__all__=["AtlassianDomainManager","get_manager"]
