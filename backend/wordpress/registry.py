"""
MAIN BASE FOUNDATION
WORDPRESS REGISTRY

Central registry for connected WordPress websites.

Responsibilities:
- register WordPress sites
- store safe site metadata
- persist registry data in the central database
- identify each WordPress installation
- manage multiple connected sites
- keep site configuration separate
  from database credentials

IMPORTANT:
Database passwords are NOT stored here.

Credentials remain in environment variables
or deployment secrets.

Central database:
    SUPREME_DB_PATH
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Optional

from backend.database.service import DatabaseService


@dataclass
class WordPressSite:
    """Safe metadata for one connected WordPress site."""

    site_id: str
    domain: str

    site_url: Optional[str] = None

    provider: Optional[str] = None

    hosting_account_id: Optional[str] = None

    database_name: Optional[str] = None

    table_prefix: str = "wp_"

    status: str = "REGISTERED"

    environment: str = "production"

    description: Optional[str] = None

    def to_dict(self) -> dict:
        """Return safe site metadata."""

        return asdict(self)


class WordPressRegistry:
    """
    Central persistent registry of WordPress websites.

    Registry metadata is stored in the central Supreme
    database through DatabaseService.

    Database passwords and API secrets are never stored here.
    """

    TABLE = "wordpress_sites"

    def __init__(
        self,
        database_service: Optional[
            DatabaseService
        ] = None,
    ) -> None:

        self.database = (
            database_service
            or DatabaseService()
        )

        self.database.initialize()

        self._ensure_table()

    # ==============================================================
    # DATABASE TABLE
    # ==============================================================

    def _ensure_table(self) -> None:
        """
        Ensure the WordPress registry table exists.

        This is intentionally compatible with the existing
        central database architecture.
        """

        self.database.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.TABLE} (

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

    # ==============================================================
    # NORMALIZE DOMAIN
    # ==============================================================

    @staticmethod
    def _normalize_domain(
        domain: str,
    ) -> str:
        """Normalize a domain for comparison."""

        return (
            domain
            .lower()
            .strip()
            .replace(
                "https://",
                "",
            )
            .replace(
                "http://",
                "",
            )
            .rstrip("/")
        )

    # ==============================================================
    # REGISTER
    # ==============================================================

    def register(
        self,
        site: WordPressSite,
    ) -> WordPressSite:
        """Register a WordPress website."""

        if not site.site_id:
            raise ValueError(
                "site_id is required."
            )

        if not site.domain:
            raise ValueError(
                "domain is required."
            )

        existing_by_id = self.get(
            site.site_id
        )

        if existing_by_id is not None:
            raise ValueError(
                f"WordPress site already registered: "
                f"{site.site_id}"
            )

        existing_by_domain = (
            self.find_by_domain(
                site.domain
            )
        )

        if existing_by_domain is not None:
            raise ValueError(
                f"WordPress domain already registered: "
                f"{site.domain}"
            )

        normalized_domain = (
            self._normalize_domain(
                site.domain
            )
        )

        self.database.execute(
            f"""
            INSERT INTO {self.TABLE} (

                site_id,
                domain,
                site_url,
                provider,
                hosting_account_id,
                database_name,
                table_prefix,
                status,
                environment,
                description

            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                site.site_id,
                normalized_domain,
                site.site_url,
                site.provider,
                site.hosting_account_id,
                site.database_name,
                site.table_prefix,
                site.status,
                site.environment,
                site.description,
            ),
        )

        result = self.get(
            site.site_id
        )

        if result is None:
            raise RuntimeError(
                "WordPress site was registered "
                "but could not be retrieved."
            )

        return result

    # ==============================================================
    # UPDATE
    # ==============================================================

    def update(
        self,
        site: WordPressSite,
    ) -> WordPressSite:
        """Update an existing WordPress site."""

        existing = self.get(
            site.site_id
        )

        if existing is None:
            raise ValueError(
                f"WordPress site not registered: "
                f"{site.site_id}"
            )

        normalized_domain = (
            self._normalize_domain(
                site.domain
            )
        )

        domain_owner = (
            self.find_by_domain(
                normalized_domain
            )
        )

        if (
            domain_owner is not None
            and domain_owner.site_id
            != site.site_id
        ):
            raise ValueError(
                f"WordPress domain already belongs "
                f"to another site: {site.domain}"
            )

        self.database.execute(
            f"""
            UPDATE {self.TABLE}

            SET
                domain = ?,
                site_url = ?,
                provider = ?,
                hosting_account_id = ?,
                database_name = ?,
                table_prefix = ?,
                status = ?,
                environment = ?,
                description = ?,
                updated_at = CURRENT_TIMESTAMP

            WHERE site_id = ?
            """,
            (
                normalized_domain,
                site.site_url,
                site.provider,
                site.hosting_account_id,
                site.database_name,
                site.table_prefix,
                site.status,
                site.environment,
                site.description,
                site.site_id,
            ),
        )

        result = self.get(
            site.site_id
        )

        if result is None:
            raise RuntimeError(
                "WordPress site update failed."
            )

        return result

    # ==============================================================
    # GET
    # ==============================================================

    def get(
        self,
        site_id: str,
    ) -> Optional[WordPressSite]:
        """Return one registered WordPress site."""

        row = self.database.fetchone(
            f"""
            SELECT
                site_id,
                domain,
                site_url,
                provider,
                hosting_account_id,
                database_name,
                table_prefix,
                status,
                environment,
                description

            FROM {self.TABLE}

            WHERE site_id = ?
            """,
            (
                site_id,
            ),
        )

        if row is None:
            return None

        return self._row_to_site(
            row
        )

    # ==============================================================
    # FIND BY DOMAIN
    # ==============================================================

    def find_by_domain(
        self,
        domain: str,
    ) -> Optional[WordPressSite]:
        """Find a WordPress site by domain."""

        normalized = (
            self._normalize_domain(
                domain
            )
        )

        row = self.database.fetchone(
            f"""
            SELECT
                site_id,
                domain,
                site_url,
                provider,
                hosting_account_id,
                database_name,
                table_prefix,
                status,
                environment,
                description

            FROM {self.TABLE}

            WHERE domain = ?
            """,
            (
                normalized,
            ),
        )

        if row is None:
            return None

        return self._row_to_site(
            row
        )

    # ==============================================================
    # LIST
    # ==============================================================

    def list_sites(
        self,
    ) -> list[WordPressSite]:
        """Return all registered WordPress sites."""

        rows = self.database.fetchall(
            f"""
            SELECT
                site_id,
                domain,
                site_url,
                provider,
                hosting_account_id,
                database_name,
                table_prefix,
                status,
                environment,
                description

            FROM {self.TABLE}

            ORDER BY id ASC
            """
        )

        return [
            self._row_to_site(row)
            for row in rows
        ]

    # ==============================================================
    # REMOVE
    # ==============================================================

    def unregister(
        self,
        site_id: str,
    ) -> bool:
        """Remove a WordPress site from the registry."""

        existing = self.get(
            site_id
        )

        if existing is None:
            return False

        self.database.execute(
            f"""
            DELETE FROM {self.TABLE}

            WHERE site_id = ?
            """,
            (
                site_id,
            ),
        )

        return True

    # ==============================================================
    # STATUS
    # ==============================================================

    def set_status(
        self,
        site_id: str,
        status: str,
    ) -> WordPressSite:
        """Update the logical status of a site."""

        site = self.get(
            site_id
        )

        if site is None:
            raise ValueError(
                f"WordPress site not registered: "
                f"{site_id}"
            )

        self.database.execute(
            f"""
            UPDATE {self.TABLE}

            SET
                status = ?,
                updated_at = CURRENT_TIMESTAMP

            WHERE site_id = ?
            """,
            (
                status,
                site_id,
            ),
        )

        result = self.get(
            site_id
        )

        if result is None:
            raise RuntimeError(
                "WordPress site status update failed."
            )

        return result

    # ==============================================================
    # EXPORT
    # ==============================================================

    def export(
        self,
    ) -> list[dict]:
        """
        Export safe registry data.

        No database passwords or secrets
        are included.
        """

        return [
            site.to_dict()
            for site in self.list_sites()
        ]

    # ==============================================================
    # COUNT
    # ==============================================================

    def count(self) -> int:
        """Return number of registered WordPress sites."""

        row = self.database.fetchone(
            f"""
            SELECT COUNT(*) AS total

            FROM {self.TABLE}
            """
        )

        if row is None:
            return 0

        return int(
            row["total"]
        )

    # ==============================================================
    # HEALTH SUMMARY
    # ==============================================================

    def summary(self) -> dict:
        """Return registry summary."""

        sites = self.list_sites()

        connected = sum(
            1
            for site in sites
            if site.status == "CONNECTED"
        )

        return {
            "registry": "WordPressRegistry",

            "total_sites": len(
                sites
            ),

            "connected_sites": connected,

            "registered_sites": (
                len(sites) - connected
            ),

            "sites": [
                site.to_dict()
                for site in sites
            ],
        }

    # ==============================================================
    # ROW CONVERSION
    # ==============================================================

    @staticmethod
    def _row_to_site(
        row: Any,
    ) -> WordPressSite:
        """Convert a database row into WordPressSite."""

        return WordPressSite(
            site_id=row["site_id"],
            domain=row["domain"],
            site_url=row["site_url"],
            provider=row["provider"],
            hosting_account_id=(
                row["hosting_account_id"]
            ),
            database_name=(
                row["database_name"]
            ),
            table_prefix=(
                row["table_prefix"]
                or "wp_"
            ),
            status=(
                row["status"]
                or "REGISTERED"
            ),
            environment=(
                row["environment"]
                or "production"
            ),
            description=(
                row["description"]
            ),
        )


__all__ = [
    "WordPressSite",
    "WordPressRegistry",
]
