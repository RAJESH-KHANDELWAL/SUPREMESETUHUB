"""Python database facade for global_database_ecosystem/database.php."""
from __future__ import annotations

from backend.database.database import main_database_connection


def global_database_ecosystem_database():
    """Return the same central connection used by the main and GE layers."""
    return main_database_connection()


__all__ = ["global_database_ecosystem_database"]
