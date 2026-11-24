"""Category adapter boundary for GOOGLE_PHOTOS_STORAGE_ECOSYSTEM; no live Google API calls yet."""
from .ecosystem_service import CategoryEcosystemService

class GooglePhotosStorageEcosystem(CategoryEcosystemService):
    """Category-specific entry point. Implement only against approved provider APIs."""
    pass
