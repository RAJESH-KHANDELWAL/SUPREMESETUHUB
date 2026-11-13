"""Python configuration facade for global_database_ecosystem/config.php."""
from __future__ import annotations

from typing import Any

from backend.database.config import (
    DATABASE_TOPOLOGY,
    main_foundation_config,
)


def global_database_ecosystem_config() -> dict[str, Any]:
    """Return GDE metadata over the same single central database."""
    main = main_foundation_config()
    return {
        "id": "GLOBAL_DATABASE_ECOSYSTEM",
        "layer": "global_database_ecosystem",
        "parent": "GLOBAL_ECOSYSTEM",
        "database_topology": DATABASE_TOPOLOGY,
        "provider": "HOSTINGER_MYSQL_MARIADB",
        "primary_identity": main["primary_identity"],
        "identities": main["identities"],
        "identity_gates": main["identity_gates"],
        "database": main["database"],
        "databases": main["databases"],
        "wordpress_database": main["wordpress_database"],
        "schema_management": "explicit_migrations_only",
    }


__all__ = ["global_database_ecosystem_config"]
