"""Global Adult Content CORE taxonomy and governance metadata."""

from .catalog import get_catalog, get_orientation
from .policy import evaluate_content_metadata
from .service import GlobalAdultContentCoreService

__all__ = [
    "GlobalAdultContentCoreService",
    "evaluate_content_metadata",
    "get_catalog",
    "get_orientation",
]
