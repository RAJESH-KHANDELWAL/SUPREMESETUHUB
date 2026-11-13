"""Python configuration counterpart to backend/database/config.php.

Configuration only: importing this module never opens a connection, creates a
database, or runs a migration. The central system has one physical database
and four logical identity gates. WordPress remains a separate database.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any

from backend.database.gde_connection import (
    PRIMARY_IDENTITY,
    IDENTITY_GATES,
    IDENTITIES,
    SupremeDatabaseConfig,
)

SYSTEM_ID = "SUPREMESETUHUB"
DATABASE_TOPOLOGY = "ONE_PHYSICAL_DATABASE_FOUR_LOGICAL_IDENTITY_GATES"


@dataclass(frozen=True)
class WordPressDatabaseConfig:
    """Separate least-privilege connection settings for an existing WordPress DB."""

    host: str
    name: str
    username: str
    password: str = field(repr=False)
    primary_username: str
    port: int = 3306
    table_prefix: str = "wp_"
    connect_timeout: int = 10
    ssl_required: bool = False
    ssl_ca: str | None = None

    @classmethod
    def from_environment(cls) -> "WordPressDatabaseConfig":
        return cls(
            host=os.getenv("WORDPRESS_DB_HOST", "").strip(),
            name=os.getenv("WORDPRESS_DB_NAME", "").strip(),
            username=os.getenv("WORDPRESS_READONLY_DB_USER", "").strip(),
            password=os.getenv("WORDPRESS_READONLY_DB_PASSWORD", ""),
            primary_username=os.getenv("WORDPRESS_PRIMARY_DB_USER", "").strip(),
            port=int(os.getenv("WORDPRESS_DB_PORT", "3306")),
            table_prefix=os.getenv("WORDPRESS_TABLE_PREFIX", "wp_").strip() or "wp_",
            connect_timeout=int(os.getenv("WORDPRESS_DB_CONNECT_TIMEOUT", "10")),
            ssl_required=os.getenv("WORDPRESS_DB_SSL_ENABLED", "false").strip().lower()
            in {"1", "true", "yes", "on"},
            ssl_ca=os.getenv("WORDPRESS_DB_SSL_CA", "").strip() or None,
        )

    def missing_settings(self) -> list[str]:
        missing = [
            key for key, value in (
                ("WORDPRESS_DB_HOST", self.host),
                ("WORDPRESS_DB_NAME", self.name),
                ("WORDPRESS_READONLY_DB_USER", self.username),
                ("WORDPRESS_READONLY_DB_PASSWORD", self.password),
                ("WORDPRESS_PRIMARY_DB_USER", self.primary_username),
            ) if not value
        ]
        if self.username and self.primary_username and self.username == self.primary_username:
            missing.append("WORDPRESS_READONLY_DB_USER_MUST_DIFFER_FROM_PRIMARY")
        if not 1 <= self.port <= 65535:
            missing.append("WORDPRESS_DB_PORT_INVALID")
        if self.connect_timeout < 1:
            missing.append("WORDPRESS_DB_CONNECT_TIMEOUT_INVALID")
        if self.ssl_required and not self.ssl_ca:
            missing.append("WORDPRESS_DB_SSL_CA")
        return missing

    @property
    def configured(self) -> bool:
        return not self.missing_settings()

    def validate(self) -> None:
        missing = self.missing_settings()
        if missing:
            raise ValueError("Missing or invalid WordPress DB settings: " + ", ".join(missing))


def main_foundation_config() -> dict[str, Any]:
    """Return the Python equivalent of supreme_main_foundation_config()."""
    central = SupremeDatabaseConfig.from_environment()
    central_config = {
        "identity": PRIMARY_IDENTITY,
        "driver": "mysql",
        "host": central.host,
        "name": central.database,
        "username": central.username,
        "password": central.password,
        "port": central.port,
        "charset": "utf8mb4",
        "connect_timeout": central.connect_timeout,
    }
    gates = {
        identity: {
            "identity": identity,
            "gate_type": "LOGICAL_IDENTITY_GATE",
            "storage_database": SYSTEM_ID,
            "scope_column": "identity_code",
            "scope_value": identity,
            "separate_physical_database": False,
        }
        for identity in IDENTITY_GATES
    }
    wordpress = WordPressDatabaseConfig.from_environment()
    wp_config = {
        "identity": "WORDPRESS",
        "driver": "mysql",
        "host": wordpress.host,
        "name": wordpress.name,
        "username": wordpress.username,
        "primary_username": wordpress.primary_username,
        "port": wordpress.port,
        "charset": "utf8mb4",
        "table_prefix": wordpress.table_prefix,
        "connect_timeout": wordpress.connect_timeout,
        "ssl_required": wordpress.ssl_required,
        "ssl_ca": wordpress.ssl_ca,
        "configured": wordpress.configured,
        "missing_settings": wordpress.missing_settings(),
    }
    return {
        "system": SYSTEM_ID,
        "architecture": DATABASE_TOPOLOGY,
        "primary_identity": PRIMARY_IDENTITY,
        "identities": list(IDENTITIES),
        "identity_gates": gates,
        "database": central_config,
        "databases": {identity: dict(central_config) for identity in IDENTITIES},
        "wordpress_database": wp_config,
        "gates": [
            "GITHUB", "WEBSITE", "WORDPRESS", "AI", "API",
            "APP", "BUSINESS", "ADMIN", "GLOBAL", "SUPREME",
        ],
    }


def database_config(prefix: str = "GDE_DB_") -> dict[str, Any]:
    """Build a strict prefixed MySQL config, matching the PHP helper's contract."""
    if not prefix or not prefix.endswith("_"):
        raise ValueError("Database environment prefix must end with an underscore.")
    values = {
        "host": os.getenv(prefix + "HOST", "").strip(),
        "database": os.getenv(prefix + "NAME", "").strip(),
        "username": os.getenv(prefix + "USER", "").strip(),
        "password": os.getenv(prefix + "PASSWORD", ""),
        "port": int(os.getenv(prefix + "PORT", "3306")),
        "connect_timeout": int(os.getenv(prefix + "CONNECT_TIMEOUT", "10")),
        "ssl_required": os.getenv(prefix + "SSL_REQUIRED", "true").strip().lower()
        in {"1", "true", "yes", "on"},
        "ssl_ca": os.getenv(prefix + "SSL_CA", "").strip() or None,
    }
    missing = [
        prefix + suffix for key, suffix in (
            ("host", "HOST"), ("database", "NAME"),
            ("username", "USER"), ("password", "PASSWORD"),
        ) if not values[key]
    ]
    if missing:
        raise ValueError("Missing database settings: " + ", ".join(missing))
    if not 1 <= values["port"] <= 65535:
        raise ValueError(prefix + "PORT must be between 1 and 65535")
    if values["connect_timeout"] < 1:
        raise ValueError(prefix + "CONNECT_TIMEOUT must be positive")
    if prefix == "GDE_DB_":
        wp_name = os.getenv("WORDPRESS_DB_NAME", "").strip()
        if wp_name and values["database"].casefold() == wp_name.casefold():
            raise ValueError("GDE_DB_NAME must not point to the WordPress database.")
    if values["ssl_required"] and not values["ssl_ca"]:
        raise ValueError(prefix + "SSL_CA is required while SSL_REQUIRED is enabled.")
    return values


__all__ = [
    "SYSTEM_ID", "DATABASE_TOPOLOGY", "PRIMARY_IDENTITY", "IDENTITY_GATES",
    "IDENTITIES", "SupremeDatabaseConfig", "WordPressDatabaseConfig",
    "main_foundation_config", "database_config",
]
