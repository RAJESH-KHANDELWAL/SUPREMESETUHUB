"""Persistent role service backed by the canonical SUPREME database."""

from __future__ import annotations

from backend.database.service import DatabaseService
from backend.roles.model import Role


class RoleService:
    """Create and manage persisted organizational role assignments."""

    def __init__(self, database: DatabaseService | None = None):
        self.database = database or DatabaseService()

    def initialize(self):
        self.database.initialize()
        self.database.execute(
            """
            CREATE TABLE IF NOT EXISTS roles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role_id TEXT UNIQUE NOT NULL,
                role_name TEXT NOT NULL,
                organization_id TEXT NOT NULL DEFAULT '',
                holder_id TEXT NOT NULL DEFAULT '',
                role_category TEXT NOT NULL DEFAULT 'GENERAL',
                authority_level INTEGER NOT NULL DEFAULT 1,
                scope TEXT NOT NULL DEFAULT 'ORGANIZATION',
                appointment_type TEXT NOT NULL DEFAULT 'STANDARD',
                description TEXT,
                status TEXT NOT NULL DEFAULT 'ACTIVE',
                level INTEGER DEFAULT 1,
                created_at TEXT,
                updated_at TEXT
            )
            """
        )

        # Additive migration only: preserve existing rows and legacy columns.
        required_columns = {
            "organization_id": "TEXT NOT NULL DEFAULT ''",
            "holder_id": "TEXT NOT NULL DEFAULT ''",
            "role_category": "TEXT NOT NULL DEFAULT 'GENERAL'",
            "authority_level": "INTEGER NOT NULL DEFAULT 1",
            "scope": "TEXT NOT NULL DEFAULT 'ORGANIZATION'",
            "appointment_type": "TEXT NOT NULL DEFAULT 'STANDARD'",
            "description": "TEXT",
            "status": "TEXT NOT NULL DEFAULT 'ACTIVE'",
            "level": "INTEGER DEFAULT 1",
            "created_at": "TEXT",
            "updated_at": "TEXT",
        }
        for name, definition in required_columns.items():
            added = self.database.add_column_if_missing("roles", name, definition)
            # On legacy schemas, preserve the previous level value when it
            # becomes the new authority_level field.
            if name == "authority_level" and added and "level" in self.database.get_columns("roles"):
                self.database.execute(
                    "UPDATE roles SET authority_level = level WHERE level IS NOT NULL"
                )

        return {"roles": "Initialized", "status": "READY"}

    def create_role(
        self,
        role_id,
        role_name,
        description=None,
        level=1,
        status="ACTIVE",
        organization_id="",
        holder_id="",
        role_category="GENERAL",
        authority_level=None,
        scope="ORGANIZATION",
        appointment_type="STANDARD",
    ):
        """Build a role object; legacy level maps to authority_level."""
        return Role(
            role_id=role_id,
            role_name=role_name,
            organization_id=organization_id,
            holder_id=holder_id,
            role_category=role_category,
            authority_level=level if authority_level is None else authority_level,
            scope=scope,
            appointment_type=appointment_type,
            status=status,
            description=description,
        )

    def save_role(self, role):
        authority_level = getattr(role, "authority_level", getattr(role, "level", 1))
        self.database.execute(
            """
            INSERT INTO roles (
                role_id, role_name, organization_id, holder_id, role_category,
                authority_level, scope, appointment_type, description, status,
                level, created_at, updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
            ON CONFLICT(role_id) DO UPDATE SET
                role_name = excluded.role_name,
                organization_id = excluded.organization_id,
                holder_id = excluded.holder_id,
                role_category = excluded.role_category,
                authority_level = excluded.authority_level,
                scope = excluded.scope,
                appointment_type = excluded.appointment_type,
                description = excluded.description,
                status = excluded.status,
                level = excluded.level,
                updated_at = CURRENT_TIMESTAMP
            """,
            (
                role.role_id,
                role.role_name,
                role.organization_id,
                role.holder_id,
                role.role_category,
                authority_level,
                role.scope,
                role.appointment_type,
                role.description,
                role.status,
                authority_level,
            ),
        )
        return role

    @staticmethod
    def _from_row(row):
        if row is None:
            return None
        return Role(
            role_id=row["role_id"],
            role_name=row["role_name"],
            organization_id=row["organization_id"],
            holder_id=row["holder_id"],
            role_category=row["role_category"],
            authority_level=row["authority_level"],
            scope=row["scope"],
            appointment_type=row["appointment_type"],
            status=row["status"],
            description=row["description"],
        )

    def get_role(self, role_id):
        row = self.database.fetchone(
            "SELECT * FROM roles WHERE role_id = ?",
            (role_id,),
        )
        return self._from_row(row)

    def update_role(
        self,
        role_id,
        role_name=None,
        description=None,
        level=None,
        status=None,
        organization_id=None,
        holder_id=None,
        role_category=None,
        authority_level=None,
        scope=None,
        appointment_type=None,
    ):
        supplied = {
            "role_name": role_name,
            "description": description,
            "status": status,
            "organization_id": organization_id,
            "holder_id": holder_id,
            "role_category": role_category,
            "authority_level": authority_level if authority_level is not None else level,
            "scope": scope,
            "appointment_type": appointment_type,
        }
        updates = {key: value for key, value in supplied.items() if value is not None}
        if not updates:
            return {"success": False, "error": "NO_FIELDS_TO_UPDATE", "role_id": role_id}

        updates["updated_at"] = None
        assignments = [
            f'"{key}" = CURRENT_TIMESTAMP' if key == "updated_at" else f'"{key}" = ?'
            for key in updates
        ]
        values = [value for key, value in updates.items() if key != "updated_at"]
        values.append(role_id)
        cursor = self.database.execute(
            f'UPDATE roles SET {", ".join(assignments)} WHERE role_id = ?',
            values,
        )
        return {"success": cursor.rowcount > 0, "role_id": role_id}

    def delete_role(self, role_id):
        cursor = self.database.execute(
            "DELETE FROM roles WHERE role_id = ?",
            (role_id,),
        )
        return {"success": cursor.rowcount > 0, "role_id": role_id}

    def get_all_roles(self):
        rows = self.database.fetchall(
            "SELECT * FROM roles ORDER BY role_name"
        )
        return [self._from_row(row) for row in rows]
