"""MAIN BASE FOUNDATION database package.

Public interface for the database layer.
"""

from .connection import DatabaseConnection
from .controller import DatabaseController
from .model import (
    DatabaseInfo,
    DatabaseTableInfo,
    DatabaseSchemaInfo,
)
from .service import DatabaseService
from .wordpress_registry import WordPressDatabaseRegistry
from .wordpress_connection import WordPressDatabaseConnection


__all__ = [
    "DatabaseConnection",
    "DatabaseController",
    "DatabaseInfo",
    "DatabaseTableInfo",
    "DatabaseSchemaInfo",
    "DatabaseService",
    "WordPressDatabaseRegistry",
    "WordPressDatabaseConnection",
]
