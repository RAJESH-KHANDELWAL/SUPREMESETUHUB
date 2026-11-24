"""GDE schema facade using the one canonical SUPREMESETUHUB database schema.

GDE is a logical ecosystem layer, not a separate physical database. This file
re-exports canonical schema and identity-gate metadata without duplicating DDL.
"""
from __future__ import annotations

from backend.database.schema import DatabaseSchema as CentralDatabaseSchema
from backend.database.global_ecosystem.schema import GlobalEcosystemSchema


class GlobalDatabaseEcosystemSchema:
    """Canonical schema contract for the Global Database Ecosystem."""

    DATABASE_NAME = GlobalEcosystemSchema.DATABASE_NAME
    DATABASE_TOPOLOGY = GlobalEcosystemSchema.DATABASE_TOPOLOGY
    IDENTITY_GATES = GlobalEcosystemSchema.IDENTITY_GATES
    TABLES = CentralDatabaseSchema.TABLES

    @classmethod
    def list_tables(cls) -> list[str]:
        return CentralDatabaseSchema.list_tables()

    @classmethod
    def get_table_schema(cls, table_name: str) -> str | None:
        return CentralDatabaseSchema.get_table_schema(table_name)

    @classmethod
    def list_identity_records(cls) -> list[tuple[str, str, str, str]]:
        return CentralDatabaseSchema.list_identity_records()


__all__ = ["GlobalDatabaseEcosystemSchema"]
