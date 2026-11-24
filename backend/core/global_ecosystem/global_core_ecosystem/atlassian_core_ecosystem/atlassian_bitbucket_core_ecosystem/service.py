"""Family-specific Atlassian Core service entry point."""
from ..module_service import AtlassianProductCoreService

class BitbucketCoreService(AtlassianProductCoreService):
    ECOSYSTEM_ID = "ATLASSIAN-BITBUCKET-CORE-ECOSYSTEM"
