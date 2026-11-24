"""Thin adapter over the shared read-only Meta domain runtime."""
from ..domain_runtime import MetaCoreDomainManager
class MetaInstagramCreatorAndProfessionalCoreManager(MetaCoreDomainManager):
    def __init__(self):
        super().__init__("INSTAGRAM_CREATOR_AND_PROFESSIONAL")
