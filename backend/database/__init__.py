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
from .gde_connection import GDEDatabaseConfig, GDEDatabaseConnection
from .wordpress_registry import WordPressDatabaseRegistry
from .cultural_knowledge_repository import CulturalKnowledgeRepository


__all__ = [
    "DatabaseConnection",
    "DatabaseController",
    "DatabaseInfo",
    "DatabaseTableInfo",
    "DatabaseSchemaInfo",
    "DatabaseService",
    "GDEDatabaseConfig",
    "GDEDatabaseConnection",
    "WordPressDatabaseRegistry",
    "WordPressDatabaseConnection",
    "CulturalKnowledgeRepository",
]
