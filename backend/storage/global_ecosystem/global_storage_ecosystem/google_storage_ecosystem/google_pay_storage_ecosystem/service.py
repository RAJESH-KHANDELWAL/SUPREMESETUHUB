"""Category adapter boundary for GOOGLE_PAY_STORAGE_ECOSYSTEM; no live Google API calls yet."""
from .ecosystem_service import CategoryEcosystemService

class GooglePayStorageEcosystem(CategoryEcosystemService):
    """Category-specific entry point. Implement only against approved provider APIs."""
    pass
