"""
MAIN BASE FOUNDATION
WORDPRESS PACKAGE

Public interface for the WordPress management layer.
"""

from .controller import WordPressController
from .service import WordPressManagementService


__all__ = [
    "WordPressController",
    "WordPressManagementService",
]
