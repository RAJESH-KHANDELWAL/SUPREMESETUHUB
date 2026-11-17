"""Global Adult Content CORE taxonomy and governance metadata."""

from .catalog import get_catalog
from .policy import evaluate_content_metadata
from .service import GlobalAdultContentCoreService
from .taxonomy import get_orientation

__all__ = [
    "GlobalAdultContentCoreService",
    "evaluate_content_metadata",
    "get_catalog",
    "get_orientation",
]
