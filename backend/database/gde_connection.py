"""SUPREMESETUHUB central MariaDB/MySQL connection.

The primary identity and four identity gates share one central database.
Credentials are read only from SUPREMESETUHUB_DB_* environment variables. This
module never creates databases or tables; schema changes require migrations.
"""
from __future__ import annotations

import os
from contextlib import contextmanager
from dataclasses import dataclass, field
from threading import RLock
from typing import Any, Iterator

import pymysql
from pymysql.connections import Connection

PRIMARY_IDENTITY = "SUPREMESETUHUB"
IDENTITY_GATES = (
    "RAJESHKHANDELWALOFFICIAL",
    "RAJESHKHANDELWAL",
    "DRRAJESHKHANDELWALIBCOFFICIAL",
    "DRRAJESHKHANDELWALIBC",
)
IDENTITIES = (PRIMARY_IDENTITY, *IDENTITY_GATES)


@dataclass(frozen=True)
class SupremeDatabaseConfig:
    """Runtime configuration for the single central SUPREMESETUHUB database."""

    host: str
    database: str
    username: str
    password: str = field(repr=False)
    port: int = 3306
    connect_timeout: int = 10
    ssl_ca: str | None = None
    ssl_required: bool = False

    @classmethod
    def from_environment(cls) -> "SupremeDatabaseConfig":
        return cls(
            host=os.getenv("SUPREMESETUHUB_DB_HOST", "").strip(),
            database=os.getenv("SUPREMESETUHUB_DB_NAME", "u664492673_SUPREMESETUHUB").strip(),
            username=os.getenv("SUPREMESETUHUB_DB_USER", "u664492673_SUPREMESETUHUB").strip(),
            password=os.getenv("SUPREMESETUHUB_DB_PASSWORD", ""),
            port=int(os.getenv("SUPREMESETUHUB_DB_PORT", "3306")),
            connect_timeout=int(os.getenv("SUPREMESETUHUB_DB_CONNECT_TIMEOUT", "10")),
            ssl_ca=os.getenv("SUPREMESETUHUB_DB_SSL_CA", "").strip() or None,
            ssl_required=os.getenv("SUPREMESETUHUB_DB_SSL_REQUIRED", "false").lower()
            in {"1", "true", "yes", "on"},
        )

    def validate(self) -> None:
        missing = [
            name for name, value in (
                ("SUPREMESETUHUB_DB_HOST", self.host),
                ("SUPREMESETUHUB_DB_NAME", self.database),
                ("SUPREMESETUHUB_DB_USER", self.username),
                ("SUPREMESETUHUB_DB_PASSWORD", self.password),
            ) if not value
        ]
        if missing:
            raise ValueError("Missing central database settings: " + ", ".join(missing))
        if self.port < 1 or self.port > 65535:
            raise ValueError("SUPREMESETUHUB_DB_PORT must be between 1 and 65535")
        if self.connect_timeout < 1:
            raise ValueError("SUPREMESETUHUB_DB_CONNECT_TIMEOUT must be positive")
        wordpress_database = os.getenv("WORDPRESS_DB_NAME", "").strip()
        if wordpress_database and self.database.casefold() == wordpress_database.casefold():
            raise ValueError(
                "The central SUPREMESETUHUB_DB_NAME must not be the primary WordPress database."
            )
        if self.ssl_required and not self.ssl_ca:
            raise ValueError("SUPREMESETUHUB_DB_SSL_REQUIRED is enabled; set SUPREMESETUHUB_DB_SSL_CA.")

# Backwards-compatible name for existing imports; it now targets the one
# central SUPREMESETUHUB database, not a separate GDE database.
GDEDatabaseConfig = SupremeDatabaseConfig


class GDEDatabaseConnection:
    """Compatibility connection class backed by the central SUPREME database."""

    def __init__(self, config: SupremeDatabaseConfig | None = None) -> None:
        self.config = config or SupremeDatabaseConfig.from_environment()
        self._connection: Connection | None = None
        self._lock = RLock()

    def connect(self) -> Connection:
        with self._lock:
            if self._connection is not None:
                try:
                    self._connection.ping(reconnect=False)
                    return self._connection
                except Exception:
                    self._connection = None

            self.config.validate()
            options: dict[str, Any] = {
                "host": self.config.host,
                "user": self.config.username,
                "password": self.config.password,
                "database": self.config.database,
                "port": self.config.port,
                "connect_timeout": self.config.connect_timeout,
                "read_timeout": self.config.connect_timeout,
                "write_timeout": self.config.connect_timeout,
                "charset": "utf8mb4",
                "cursorclass": pymysql.cursors.DictCursor,
                "autocommit": False,
            }
            if self.config.ssl_ca:
                options.update(
                    ssl_ca=self.config.ssl_ca,
                    ssl_verify_cert=True,
                    ssl_verify_identity=True,
                )
            self._connection = pymysql.connect(**options)
            return self._connection

    def health(self) -> dict[str, Any]:
        try:
            connection = self.connect()
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1 AS connection_test")
                row = cursor.fetchone()
            ok = bool(row and row.get("connection_test") == 1)
            return {
                "success": ok,
                "status": "HEALTHY" if ok else "UNHEALTHY",
                "primary_identity": PRIMARY_IDENTITY,
                "identities": list(IDENTITIES),
                "database": self.config.database,
                "connected": ok,
            }
        except Exception as exc:
            return {
                "success": False,
                "status": "CONNECTION_FAILED",
                "primary_identity": PRIMARY_IDENTITY,
                "database": self.config.database,
                "connected": False,
                "error_type": type(exc).__name__,
            }

    def information(self) -> dict[str, Any]:
        connection = self.connect()
        with connection.cursor() as cursor:
            cursor.execute("SELECT DATABASE() AS database_name, VERSION() AS server_version")
            row = cursor.fetchone() or {}
        return {
            "database": row.get("database_name"),
            "server_version": row.get("server_version"),
            "host": self.config.host,
            "port": self.config.port,
            "primary_identity": PRIMARY_IDENTITY,
            "identity_gates": list(IDENTITY_GATES),
        }

    def list_tables(self) -> list[str]:
        connection = self.connect()
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES")
            rows = cursor.fetchall()
        return [str(next(iter(row.values()))) for row in rows if row]

    @contextmanager
    def transaction(self) -> Iterator[Connection]:
        with self._lock:
            connection = self.connect()
            try:
                yield connection
                connection.commit()
            except Exception:
                connection.rollback()
                raise

    def close(self) -> None:
        with self._lock:
            if self._connection is not None:
                try:
                    self._connection.close()
                finally:
                    self._connection = None

    def status(self) -> dict[str, Any]:
        return {
            "service": "SupremeDatabaseConnection",
            "primary_identity": PRIMARY_IDENTITY,
            "identities": list(IDENTITIES),
            "database": self.config.database,
            "host": self.config.host,
            "port": self.config.port,
            "connected": self._connection is not None,
            "ssl_required": self.config.ssl_required,
            "ssl_ca_configured": bool(self.config.ssl_ca),
        }


SupremeDatabaseConnection = GDEDatabaseConnection
__all__ = [
    "PRIMARY_IDENTITY", "IDENTITY_GATES", "IDENTITIES",
    "SupremeDatabaseConfig", "SupremeDatabaseConnection",
    "GDEDatabaseConfig", "GDEDatabaseConnection",
]
