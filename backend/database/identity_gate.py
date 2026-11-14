"""Identity gate registry and access-policy service for SUPREMESETUHUB.

One physical central database; one primary identity plus four logical brand
identities. This module resolves identities and enforces identity-scoped access.
It does not authenticate passwords or issue sessions; callers must supply a
principal_id already authenticated by the application's trusted auth layer.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from backend.database.gde_connection import (
    GDEDatabaseConnection,
    IDENTITIES,
    IDENTITY_GATES,
    PRIMARY_IDENTITY,
)


@dataclass(frozen=True)
class Identity:
    code: str
    display_name: str
    gate_type: str
    storage_database: str
    is_active: bool


class IdentityGateError(PermissionError):
    """Raised when an identity is unknown, disabled, or outside a user's scope."""


class IdentityGateService:
    """Resolve registered identity gates and authorize scoped operations."""

    def __init__(self, database: GDEDatabaseConnection) -> None:
        self.database = database

    @staticmethod
    def normalize(identity_code: str) -> str:
        if not isinstance(identity_code, str):
            raise IdentityGateError("Identity code must be a string.")
        normalized = identity_code.strip().upper()
        if normalized not in IDENTITIES:
            raise IdentityGateError("Unknown SUPREMESETUHUB identity.")
        return normalized

    def list_identities(self, *, include_inactive: bool = False) -> list[Identity]:
        sql = (
            "SELECT identity_code, display_name, gate_type, storage_database, is_active "
            "FROM ss_identity_gates"
        )
        if not include_inactive:
            sql += " WHERE is_active = 1"
        sql += " ORDER BY CASE WHEN gate_type = 'MAIN' THEN 0 ELSE 1 END, identity_code"
        connection = self.database.connect()
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
        return [
            Identity(
                code=str(row["identity_code"]),
                display_name=str(row["display_name"]),
                gate_type=str(row["gate_type"]),
                storage_database=str(row["storage_database"]),
                is_active=bool(row["is_active"]),
            )
            for row in rows
        ]

    def resolve(self, identity_code: str) -> Identity:
        code = self.normalize(identity_code)
        connection = self.database.connect()
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT identity_code, display_name, gate_type, storage_database, is_active "
                "FROM ss_identity_gates WHERE identity_code = %s LIMIT 1",
                (code,),
            )
            row = cursor.fetchone()
        if not row or not bool(row["is_active"]):
            raise IdentityGateError("Identity is not registered or is inactive.")
        if str(row["storage_database"]) != PRIMARY_IDENTITY:
            raise IdentityGateError("Identity points outside the configured central database.")
        return Identity(
            code=str(row["identity_code"]),
            display_name=str(row["display_name"]),
            gate_type=str(row["gate_type"]),
            storage_database=str(row["storage_database"]),
            is_active=bool(row["is_active"]),
        )

    def authorize(
        self,
        *,
        principal_id: str,
        identity_code: str,
        permission_code: str,
    ) -> Identity:
        """Check an authenticated principal's grant for one identity/permission."""
        principal = principal_id.strip()
        permission = permission_code.strip().upper()
        if not principal or not permission:
            raise IdentityGateError("Authenticated principal and permission are required.")
        identity = self.resolve(identity_code)
        connection = self.database.connect()
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT 1 FROM ss_identity_principal_roles r "
                "JOIN ss_identity_role_permissions rp ON rp.role_code = r.role_code "
                "WHERE r.principal_id = %s AND r.identity_code = %s "
                "AND rp.permission_code = %s AND r.is_active = 1 LIMIT 1",
                (principal, identity.code, permission),
            )
            granted = cursor.fetchone()
        if not granted:
            raise IdentityGateError("Principal is not authorized for this identity operation.")
        return identity

    @staticmethod
    def scope_filter(identity_code: str, *, column: str = "identity_code") -> tuple[str, tuple[str]]:
        """Return a parameterized SQL predicate; column must be a trusted code constant."""
        code = IdentityGateService.normalize(identity_code)
        if not column.replace("_", "").isalnum():
            raise ValueError("Unsafe SQL column identifier.")
        return f"{column} = %s", (code,)


__all__ = [
    "Identity", "IdentityGateError", "IdentityGateService",
    "PRIMARY_IDENTITY", "IDENTITY_GATES",
]
