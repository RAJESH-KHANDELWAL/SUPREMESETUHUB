"""Python configuration facade for global_ecosystem/config.php."""
from __future__ import annotations

from typing import Any

from backend.database.config import (
    DATABASE_TOPOLOGY,
    main_foundation_config,
)


def global_ecosystem_config() -> dict[str, Any]:
    """Return GE metadata while reusing the central database configuration."""
    main = main_foundation_config()
    return {
        "id": "GLOBAL_ECOSYSTEM",
        "layer": "global_ecosystem",
        "parent": "SUPREMESETUHUB",
        "database_topology": DATABASE_TOPOLOGY,
        "primary_identity": main["primary_identity"],
        "identities": main["identities"],
        "identity_gates": main["identity_gates"],
        "database": main["database"],
        "databases": main["databases"],
        "wordpress_database": main["wordpress_database"],
    }


__all__ = ["global_ecosystem_config"]
