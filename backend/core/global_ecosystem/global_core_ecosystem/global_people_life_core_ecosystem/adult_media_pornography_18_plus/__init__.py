"""Adult Media Pornography 18 Plus domain package; CORE metadata only."""
DOMAIN_ID = "ADULT_MEDIA_PORNOGRAPHY_18_PLUS"
STATUS = "CORE_CATALOG_ONLY"
AGE_RESTRICTED = True

from .taxonomy import (
    AdultContentClassificationError,
    get_classification_catalog,
    validate_classification_metadata,
)

__all__ = [
    "DOMAIN_ID",
    "STATUS",
    "AGE_RESTRICTED",
    "AdultContentClassificationError",
    "get_classification_catalog",
    "validate_classification_metadata",
]
