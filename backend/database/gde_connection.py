"""MAIN BASE FOUNDATION — dedicated Global Database Ecosystem connection.

This is intentionally separate from both WordPress connections and the
canonical local SQLite database. It never creates databases or tables.
Credentials are read only from GDE_DB_* environment variables.
"""
from __future__ import annotations

import os
from contextlib import contextmanager
from dataclasses import dataclass, field
from threading import RLock
from typing import Any, Iterator

import pymysql
from pymysql.connections import Connection


@dataclass(frozen=True)
class GDEDatabaseConfig:
    """Runtime configuration for the dedicated Global Database Ecosystem DB."""

    host: str
    database: str
    username: str
    password: str = field(repr=False)
    port: int = 3306
    connect_timeout: int = 10
    ssl_ca: str | None = None
    ssl_required: bool = True

    @classmethod
    def from_environment(cls) -> "GDEDatabaseConfig":
        """Load GDE-only credentials; never fall back to WordPress variables."""
        return cls(
            host=os.getenv("GDE_DB_HOST", "").strip(),
            database=os.getenv("GDE_DB_NAME", "").strip(),
            username=os.getenv("GDE_DB_USER", "").strip(),
            password=os.getenv("GDE_DB_PASSWORD", ""),
            port=int(os.getenv("GDE_DB_PORT", "3306")),
            connect_timeout=int(os.getenv("GDE_DB_CONNECT_TIMEOUT", "10")),
            ssl_ca=os.getenv("GDE_DB_SSL_CA", "").strip() or None,
            ssl_required=os.getenv("GDE_DB_SSL_REQUIRED", "true").lower()
            in {"1", "true", "yes", "on"},
        )

    def validate(self) -> None:
        """Fail closed when configuration is incomplete or points at WordPress."""
        missing = [
            name
            for name, value in (
                ("GDE_DB_HOST", self.host),
                ("GDE_DB_NAME", self.database),
                ("GDE_DB_USER", self.username),
                ("GDE_DB_PASSWORD", self.password),
            )
            if not value
        ]
        if missing:
            raise ValueError("Missing GDE database settings: " + ", ".join(missing))
        if self.port < 1 or self.port > 65535:
            raise ValueError("GDE_DB_PORT must be between 1 and 65535")
        if self.connect_timeout < 1:
            raise ValueError("GDE_DB_CONNECT_TIMEOUT must be positive")

        wordpress_databases = {
            os.getenv("WORDPRESS_DB_NAME", "").strip(),
            os.getenv("WORDPRESS_IBC_DB_NAME", "").strip(),
        } - {""}
        if self.database in wordpress_databases:
            raise ValueError(
                "GDE_DB_NAME must be a separate database; WordPress databases "
                "are protected and cannot be selected as the GDE database."
            )
        if self.ssl_required and not self.ssl_ca:
            raise ValueError(
                "GDE_DB_SSL_REQUIRED is enabled; set GDE_DB_SSL_CA to the "
                "database server CA certificate path."
            )


class GDEDatabaseConnection:
    """Dedicated MariaDB/MySQL connection for Global Database Ecosystem."""

    def __init__(self, config: GDEDatabaseConfig | None = None) -> None:
        self.config = config or GDEDatabaseConfig.from_environment()
        self._connection: Connection | None = None
        self._lock = RLock()

    def connect(self) -> Connection:
        """Open the configured GDE database; no schema or data is modified."""
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
        """Run a read-only SELECT 1 health probe."""
        try:
            connection = self.connect()
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1 AS connection_test")
                row = cursor.fetchone()
            return {
                "success": bool(row and row.get("connection_test") == 1),
                "status": "HEALTHY" if row and row.get("connection_test") == 1 else "UNHEALTHY",
                "database": self.config.database,
                "connected": bool(row and row.get("connection_test") == 1),
            }
        except Exception as exc:
            return {
                "success": False,
                "status": "CONNECTION_FAILED",
                "database": self.config.database,
                "connected": False,
                "error_type": type(exc).__name__,
            }

    def information(self) -> dict[str, Any]:
        """Return non-secret identity/version information for the selected DB."""
        connection = self.connect()
        with connection.cursor() as cursor:
            cursor.execute("SELECT DATABASE() AS database_name, VERSION() AS server_version")
            row = cursor.fetchone() or {}
        return {
            "database": row.get("database_name"),
            "server_version": row.get("server_version"),
            "host": self.config.host,
            "port": self.config.port,
        }

    def list_tables(self) -> list[str]:
        """List table names without reading or changing table contents."""
        connection = self.connect()
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES")
            rows = cursor.fetchall()
        return [str(next(iter(row.values()))) for row in rows if row]

    @contextmanager
    def transaction(self) -> Iterator[Connection]:
        """Provide an explicit transaction; callers own authorization and SQL."""
        with self._lock:
            connection = self.connect()
            try:
                yield connection
                connection.commit()
            except Exception:
                connection.rollback()
                raise

    def close(self) -> None:
        """Close the active connection."""
        with self._lock:
            if self._connection is not None:
                try:
                    self._connection.close()
                finally:
                    self._connection = None

    def status(self) -> dict[str, Any]:
        """Expose safe connection metadata, never credentials."""
        return {
            "service": "GDEDatabaseConnection",
            "database": self.config.database,
            "host": self.config.host,
            "port": self.config.port,
            "connected": self._connection is not None,
            "ssl_required": self.config.ssl_required,
            "ssl_ca_configured": bool(self.config.ssl_ca),
        }


__all__ = ["GDEDatabaseConfig", "GDEDatabaseConnection"]
