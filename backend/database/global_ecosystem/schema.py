"""Global Ecosystem schema facade over the single central database schema.

This module defines no second database and duplicates no table definitions.
All Global Ecosystem data uses the canonical backend.database.schema module.
"""
from __future__ import annotations

from backend.database.schema import DatabaseSchema as CentralDatabaseSchema


class GlobalEcosystemSchema:
    """Expose the canonical schema to Global Ecosystem components."""

    DATABASE_NAME = "SUPREMESETUHUB"
    DATABASE_TOPOLOGY = "ONE_PHYSICAL_DATABASE_FOUR_LOGICAL_IDENTITY_GATES"
    IDENTITY_GATES = (
        "RAJESHKHANDELWALOFFICIAL",
        "RAJESHKHANDELWAL",
        "DRRAJESHKHANDELWALIBCOFFICIAL",
        "DRRAJESHKHANDELWALIBC",
    )
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


__all__ = ["GlobalEcosystemSchema"]
