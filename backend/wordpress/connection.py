"""
Secure direct MySQL/MariaDB connector for the existing live WordPress sites.

WordPress/PHP stays on its current hosting. This module opens a separate
backend-to-database connection and performs read-only health/schema checks.
It never imports a SQL dump or changes WordPress content.
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass
from typing import Any, Optional

import mysql.connector


_ALLOWED_ENV_PREFIXES = {"WORDPRESS", "WORDPRESS_IBC"}
_SAFE_TABLE_PREFIX = re.compile(r"^[A-Za-z0-9_]{1,64}$")


@dataclass(frozen=True)
class WordPressConnectionConfig:
    """Private runtime configuration for one allow-listed WordPress site."""

    site_id: str
    domain: str
    database_host: str
    database_name: str
    database_user: str
    database_password: str
    database_port: int = 3306
    table_prefix: str = "wp_"
    ssl_enabled: bool = True
    connect_timeout: int = 10

    @classmethod
    def from_environment(
        cls,
        site_id: str,
        domain: str,
        prefix: str = "WORDPRESS",
    ) -> "WordPressConnectionConfig":
        if prefix not in _ALLOWED_ENV_PREFIXES:
            raise ValueError("WORDPRESS_ENVIRONMENT_PREFIX_NOT_ALLOWED")

        def clean(name: str) -> str:
            return os.getenv(name, "").strip()

        host = clean(f"{prefix}_DB_HOST")
        name = clean(f"{prefix}_DB_NAME")
        user = clean(f"{prefix}_DB_USER")
        # Do not strip the password: spaces can be part of a valid secret.
        password = os.getenv(f"{prefix}_DB_PASSWORD", "")
        port_text = clean(f"{prefix}_DB_PORT") or "3306"
        table_prefix = clean(f"{prefix}_TABLE_PREFIX") or "wp_"

        required = {
            f"{prefix}_DB_HOST": host,
            f"{prefix}_DB_NAME": name,
            f"{prefix}_DB_USER": user,
            f"{prefix}_DB_PASSWORD": password,
        }
        missing = [key for key, value in required.items() if not value]
        if missing:
            raise RuntimeError(
                "MISSING_WORDPRESS_DATABASE_SETTINGS: " + ", ".join(missing)
            )

        try:
            port = int(port_text)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{prefix}_DB_PORT_MUST_BE_INTEGER") from exc
        if not 1 <= port <= 65535:
            raise ValueError(f"{prefix}_DB_PORT_OUT_OF_RANGE")

        if not _SAFE_TABLE_PREFIX.fullmatch(table_prefix):
            raise ValueError(f"{prefix}_TABLE_PREFIX_INVALID")

        ssl_text = clean(f"{prefix}_DB_SSL_ENABLED").lower()
        ssl_enabled = ssl_text not in {"0", "false", "no", "off"}

        return cls(
            site_id=site_id,
            domain=domain,
            database_host=host,
            database_name=name,
            database_user=user,
            database_password=password,
            database_port=port,
            table_prefix=table_prefix,
            ssl_enabled=ssl_enabled,
        )


class WordPressDatabaseConnection:
    """A single live database connection for one registered WordPress site."""

    def __init__(self, config: WordPressConnectionConfig) -> None:
        self.config = config
        self.connection: Optional[Any] = None

    def connect(self):
        """Open or recover the configured connection."""
        if self.connection is not None:
            try:
                if self.connection.is_connected():
                    self.connection.ping(reconnect=True, attempts=1, delay=0)
                    return self.connection
            except Exception:
                try:
                    self.connection.close()
                except Exception:
                    pass
                self.connection = None

        self.connection = mysql.connector.connect(
            host=self.config.database_host,
            port=self.config.database_port,
            database=self.config.database_name,
            user=self.config.database_user,
            password=self.config.database_password,
            connection_timeout=self.config.connect_timeout,
            ssl_disabled=not self.config.ssl_enabled,
            charset="utf8mb4",
            use_unicode=True,
            autocommit=True,
        )
        return self.connection

    def disconnect(self) -> None:
        """Close the connection and clear the local handle."""
        if self.connection is not None:
            try:
                self.connection.close()
            except Exception:
                # Cleanup must not mask the original connection/health error.
                pass
            finally:
                self.connection = None

    def health(self) -> dict:
        """Run a harmless connectivity probe without exposing credentials/errors."""
        cursor = None
        try:
            connection = self.connect()
            cursor = connection.cursor()
            cursor.execute("SELECT 1")
            row = cursor.fetchone()
            return {
                "success": bool(row and row[0] == 1),
                "status": "CONNECTED" if row and row[0] == 1 else "HEALTH_CHECK_FAILED",
                "site_id": self.config.site_id,
                "domain": self.config.domain,
                "database": self.config.database_name,
                "table_prefix": self.config.table_prefix,
                "tls_requested": self.config.ssl_enabled,
            }
        except Exception as exc:
            # Do not return exception text: some drivers include host/user details.
            return {
                "success": False,
                "status": "CONNECTION_FAILED",
                "site_id": self.config.site_id,
                "domain": self.config.domain,
                "error_type": type(exc).__name__,
            }
        finally:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception:
                    pass

    def check_wordpress_tables(self) -> dict:
        """Read-only verification of the four core WordPress tables."""
        cursor = None
        required_suffixes = ("options", "posts", "users", "usermeta")
        found: list[str] = []
        missing: list[str] = []
        try:
            connection = self.connect()
            cursor = connection.cursor()
            for suffix in required_suffixes:
                table_name = f"{self.config.table_prefix}{suffix}"
                cursor.execute(
                    """
                    SELECT COUNT(*)
                    FROM information_schema.tables
                    WHERE table_schema = %s AND table_name = %s
                    """,
                    (self.config.database_name, table_name),
                )
                row = cursor.fetchone()
                if row and int(row[0]) > 0:
                    found.append(table_name)
                else:
                    missing.append(table_name)

            return {
                "success": not missing,
                "status": "WORDPRESS_TABLES_VERIFIED" if not missing else "WORDPRESS_TABLES_MISSING",
                "site_id": self.config.site_id,
                "domain": self.config.domain,
                "database": self.config.database_name,
                "table_prefix": self.config.table_prefix,
                "found_tables": found,
                "missing_tables": missing,
            }
        except Exception as exc:
            return {
                "success": False,
                "status": "TABLE_CHECK_FAILED",
                "site_id": self.config.site_id,
                "domain": self.config.domain,
                "error_type": type(exc).__name__,
                "found_tables": found,
                "missing_tables": missing,
            }
        finally:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception:
                    pass

    def status(self) -> dict:
        """Return connection state without credentials."""
        connected = False
        if self.connection is not None:
            try:
                connected = bool(self.connection.is_connected())
            except Exception:
                connected = False
        return {
            "service": "WordPressDatabaseConnection",
            "site_id": self.config.site_id,
            "domain": self.config.domain,
            "database": self.config.database_name,
            "table_prefix": self.config.table_prefix,
            "connected": connected,
        }


__all__ = ["WordPressConnectionConfig", "WordPressDatabaseConnection"]
