"""Thin adapter over the shared read-only Meta domain runtime."""
from ..domain_runtime import MetaCoreDomainManager
class MetaAppReviewPermissionComplianceCoreManager(MetaCoreDomainManager):
    def __init__(self):
        super().__init__("APP_REVIEW_PERMISSION_COMPLIANCE")
