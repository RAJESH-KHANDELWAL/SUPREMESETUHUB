from __future__ import annotations

import os
import sqlite3
from pathlib import Path
from typing import Any, Iterable, Optional


class DatabaseService:
    """
    CENTRAL SQLITE DATABASE SERVICE

    Responsibilities:
    - Open central SQLite database
    - Create required tables
    - Safely migrate existing tables
    - Add missing columns without deleting existing data
    - Provide execute / fetchone / fetchall helpers
    """

    def __init__(
        self,
        db_path: Optional[str] = None,
    ) -> None:

        self.db_path = (
            db_path
            or os.getenv("SUPREME_DB_PATH")
            or "data/supreme.db"
        )

        self._connection: Optional[sqlite3.Connection] = None

    # ==========================================================
    # CONNECTION
    # ==========================================================

    def connect(self) -> sqlite3.Connection:

        if self._connection is None:

            path = Path(self.db_path)

            if path.parent:
                path.parent.mkdir(
                    parents=True,
                    exist_ok=True,
                )

            self._connection = sqlite3.connect(
                str(path),
                check_same_thread=False,
            )

            self._connection.row_factory = (
                sqlite3.Row
            )

            self._connection.execute(
                "PRAGMA foreign_keys = ON"
            )

        return self._connection

    # ==========================================================
    # CLOSE
    # ==========================================================

    def close(self) -> None:

        if self._connection is not None:

            self._connection.close()

            self._connection = None

    # ==========================================================
    # EXECUTE
    # ==========================================================

    def execute(
        self,
        query: str,
        parameters: Iterable[Any] = (),
    ) -> sqlite3.Cursor:

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute(
            query,
            tuple(parameters),
        )

        connection.commit()

        return cursor

    # ==========================================================
    # FETCH ONE
    # ==========================================================

    def fetchone(
        self,
        query: str,
        parameters: Iterable[Any] = (),
    ) -> Optional[sqlite3.Row]:

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute(
            query,
            tuple(parameters),
        )

        return cursor.fetchone()

    # ==========================================================
    # FETCH ALL
    # ==========================================================

    def fetchall(
        self,
        query: str,
        parameters: Iterable[Any] = (),
    ) -> list[sqlite3.Row]:

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute(
            query,
            tuple(parameters),
        )

        return cursor.fetchall()

    # ==========================================================
    # TABLE EXISTS
    # ==========================================================

    def table_exists(
        self,
        table_name: str,
    ) -> bool:

        row = self.fetchone(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
              AND name = ?
            """,
            (table_name,),
        )

        return row is not None

    # ==========================================================
    # TABLE COLUMNS
    # ==========================================================

    def get_columns(
        self,
        table_name: str,
    ) -> set[str]:

        rows = self.fetchall(
            f'PRAGMA table_info("{table_name}")'
        )

        return {
            str(row["name"])
            for row in rows
        }

    # ==========================================================
    # ADD MISSING COLUMN
    # ==========================================================

    def add_column_if_missing(
        self,
        table_name: str,
        column_name: str,
        column_definition: str,
    ) -> bool:

        if not self.table_exists(
            table_name
        ):
            return False

        columns = self.get_columns(
            table_name
        )

        if column_name in columns:
            return False

        self.execute(
            f'''
            ALTER TABLE "{table_name}"
            ADD COLUMN "{column_name}"
            {column_definition}
            '''
        )

        return True

    # ==========================================================
    # WORDPRESS SITES MIGRATION
    # ==========================================================

    def migrate_wordpress_sites(self) -> None:

        table = "wordpress_sites"

        # ------------------------------------------------------
        # If table does not exist, create the complete version
        # ------------------------------------------------------

        if not self.table_exists(table):

            self.execute(
                """
                CREATE TABLE IF NOT EXISTS wordpress_sites (

                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    site_id TEXT NOT NULL UNIQUE,

                    domain TEXT NOT NULL UNIQUE,

                    site_url TEXT,

                    provider TEXT,

                    hosting_account_id TEXT,

                    database_name TEXT,

                    table_prefix TEXT
                        DEFAULT 'wp_',

                    status TEXT
                        DEFAULT 'REGISTERED',

                    environment TEXT
                        DEFAULT 'production',

                    description TEXT,

                    created_at TEXT
                        DEFAULT CURRENT_TIMESTAMP,

                    updated_at TEXT
                        DEFAULT CURRENT_TIMESTAMP
                )
                """
            )

            return

        # ------------------------------------------------------
        # Existing table:
        # ADD ONLY MISSING COLUMNS
        # ------------------------------------------------------

        required_columns = {

            "site_id":
                "TEXT",

            "domain":
                "TEXT",

            "site_url":
                "TEXT",

            "provider":
                "TEXT",

            "hosting_account_id":
                "TEXT",

            "database_name":
                "TEXT",

            "table_prefix":
                "TEXT DEFAULT 'wp_'",

            "status":
                "TEXT DEFAULT 'REGISTERED'",

            "environment":
                "TEXT DEFAULT 'production'",

            "description":
                "TEXT",

            "created_at":
                "TEXT DEFAULT CURRENT_TIMESTAMP",

            "updated_at":
                "TEXT DEFAULT CURRENT_TIMESTAMP",
        }

        for column_name, definition in (
            required_columns.items()
        ):

            self.add_column_if_missing(
                table,
                column_name,
                definition,
            )

        # ------------------------------------------------------
        # Repair NULL/default values for existing rows
        # ------------------------------------------------------

        self.execute(
            """
            UPDATE wordpress_sites
            SET table_prefix = 'wp_'
            WHERE table_prefix IS NULL
               OR table_prefix = ''
            """
        )

        self.execute(
            """
            UPDATE wordpress_sites
            SET status = 'REGISTERED'
            WHERE status IS NULL
               OR status = ''
            """
        )

        self.execute(
            """
            UPDATE wordpress_sites
            SET environment = 'production'
            WHERE environment IS NULL
               OR environment = ''
            """
        )

    # ==========================================================
    # GLOBAL MIGRATION
    # ==========================================================

    def migrate_existing_database(self) -> None:

        # ------------------------------------------------------
        # WORDPRESS
        # ------------------------------------------------------

        self.migrate_wordpress_sites()

    # ==========================================================
    # INITIALIZE
    # ==========================================================

    def initialize(self) -> None:

        self.connect()

        # ------------------------------------------------------
        # Existing project schema initialization
        # ------------------------------------------------------

        try:

            from backend.database.schema import (
                DatabaseSchema,
            )

            for table_name in (
                DatabaseSchema.list_tables()
            ):

                schema_sql = (
                    DatabaseSchema.get_table_schema(
                        table_name
                    )
                )

                if schema_sql:
                    self.execute(
                        schema_sql
                    )

        except ImportError:
            # Schema module is optional during
            # early bootstrap.
            pass

        # ------------------------------------------------------
        # IMPORTANT:
        # Run migrations AFTER table creation.
        # ------------------------------------------------------

        self.migrate_existing_database()

        # ------------------------------------------------------
        # Final commit
        # ------------------------------------------------------

        self.connect().commit()
