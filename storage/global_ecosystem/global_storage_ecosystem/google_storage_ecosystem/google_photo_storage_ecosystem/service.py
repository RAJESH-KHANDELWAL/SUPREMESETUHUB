"""Category adapter boundary for GOOGLE_PHOTO_STORAGE_ECOSYSTEM; no live Google API calls yet."""
from .ecosystem_service import CategoryEcosystemService

class GooglePhotoStorageEcosystem(CategoryEcosystemService):
    """Category-specific entry point. Implement only against approved provider APIs."""
    pass
