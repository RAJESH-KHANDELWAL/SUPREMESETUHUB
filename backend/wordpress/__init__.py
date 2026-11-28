"""
MAIN BASE FOUNDATION
WORDPRESS MODULE

Public interface for the WordPress platform layer.

Architecture:

WORDPRESS CONTROLLER
        ↓
WORDPRESS SERVICE
        ↓
WORDPRESS REGISTRY
        ↓
WORDPRESS CONNECTION
        ↓
LIVE WORDPRESS DATABASE
"""

from .connection import (
    WordPressConnectionConfig,
    WordPressDatabaseConnection,
)

from .controller import (
    WordPressController,
)

from .registry import (
    WordPressRegistry,
    WordPressSite,
)

from .service import (
    WordPressService,
)


__all__ = [
    # Connection
    "WordPressConnectionConfig",
    "WordPressDatabaseConnection",

    # Registry
    "WordPressRegistry",
    "WordPressSite",

    # Service
    "WordPressService",

    # Controller
    "WordPressController",
]
