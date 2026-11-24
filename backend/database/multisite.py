"""
CENTRAL MULTI-SITE / MULTI-DOMAIN DATA LAYER

One platform can manage:
- Multiple domains
- Multiple websites
- Multiple hosting accounts
- Multiple applications

GLOBAL data can be shared across all sites.
SITE data remains isolated to its own site/domain.
"""


class MultiSiteManager:

    GLOBAL_SCOPE = "GLOBAL"

    def __init__(self, database):
        self.database = database

    def create_site(
        self,
        name,
        domain,
        hosting_provider=None,
        platform=None,
    ):
        """
        Register a website/domain in the central system.
        """

        return self.database.execute(
            """
            INSERT INTO sites
            (
                name,
                domain,
                hosting_provider,
                platform,
                scope,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                name,
                domain,
                hosting_provider,
                platform,
                "SITE",
                "active",
            ),
        )

    def get_site(self, domain):
        """
        Get one registered site by domain.
        """

        return self.database.fetch_one(
            """
            SELECT *
            FROM sites
            WHERE domain = ?
            """,
            (domain,),
        )

    def list_sites(self):
        """
        Return all registered domains/sites.
        """

        return self.database.fetch_all(
            """
            SELECT *
            FROM sites
            ORDER BY id
            """
        )

    def update_site(self, domain, **fields):
        """
        Update site metadata.
        """

        allowed = {
            "name",
            "hosting_provider",
            "platform",
            "status",
        }

        updates = []
        values = []

        for key, value in fields.items():
            if key in allowed:
                updates.append(f"{key} = ?")
                values.append(value)

        if not updates:
            return None

        values.append(domain)

        return self.database.execute(
            f"""
            UPDATE sites
            SET {", ".join(updates)}
            WHERE domain = ?
            """,
            tuple(values),
        )

    def delete_site(self, domain):
        """
        Remove site registration.

        This does NOT delete the actual live website.
        """

        return self.database.execute(
            """
            DELETE FROM sites
            WHERE domain = ?
            """,
            (domain,),
        )
