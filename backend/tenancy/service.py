"""Central multi-tenant data spaces and per-website access gates.

All tenant data is stored in the existing central DatabaseService database.
Isolation is logical and enforced by tenant_id + site_id + membership gate.
This module does not create, merge, or modify the two WordPress databases.
"""
from __future__ import annotations

import json
import secrets
from typing import Any, Optional

from backend.database.service import DatabaseService


SUPPORTED_SITES = {
    "rajeshkhandelwalofficial": "rajeshkhandelwalofficial.com",
    "drrajeshkhandelwalibc": "drrajeshkhandelwalibc.com",
}
SUPPORTED_GATE_COUNTS = {1, 2, 4}


class TenantNotFoundError(ValueError):
    pass


class TenantAccessError(PermissionError):
    pass


class TenantValidationError(ValueError):
    pass


class TenantService:
    """Manage tenants, per-site gate policies, memberships and isolated records."""

    def __init__(self, database: Optional[DatabaseService] = None) -> None:
        self.database = database or DatabaseService()
        self.initialize()

    def initialize(self) -> None:
        self.database.initialize()
        self.database.execute(
            """
            CREATE TABLE IF NOT EXISTS tenants (
                tenant_id TEXT PRIMARY KEY,
                tenant_name TEXT NOT NULL,
                tenant_type TEXT NOT NULL DEFAULT 'BUSINESS',
                owner_user_id TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'ACTIVE',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        self.database.execute(
            """
            CREATE TABLE IF NOT EXISTS tenant_site_bindings (
                tenant_id TEXT NOT NULL,
                site_id TEXT NOT NULL,
                gate_count INTEGER NOT NULL CHECK (gate_count IN (1, 2, 4)),
                status TEXT NOT NULL DEFAULT 'ACTIVE',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (tenant_id, site_id),
                FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id) ON DELETE CASCADE
            )
            """
        )
        self.database.execute(
            """
            CREATE TABLE IF NOT EXISTS tenant_memberships (
                tenant_id TEXT NOT NULL,
                site_id TEXT NOT NULL,
                user_id TEXT NOT NULL,
                gate_level INTEGER NOT NULL CHECK (gate_level BETWEEN 1 AND 4),
                member_role TEXT NOT NULL DEFAULT 'MEMBER',
                status TEXT NOT NULL DEFAULT 'ACTIVE',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (tenant_id, site_id, user_id),
                FOREIGN KEY (tenant_id, site_id)
                    REFERENCES tenant_site_bindings(tenant_id, site_id) ON DELETE CASCADE
            )
            """
        )
        self.database.execute(
            """
            CREATE TABLE IF NOT EXISTS tenant_records (
                record_id TEXT PRIMARY KEY,
                tenant_id TEXT NOT NULL,
                site_id TEXT NOT NULL,
                domain_key TEXT NOT NULL,
                record_type TEXT NOT NULL,
                min_gate INTEGER NOT NULL CHECK (min_gate BETWEEN 1 AND 4),
                payload_json TEXT NOT NULL,
                created_by TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'ACTIVE',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (tenant_id, site_id)
                    REFERENCES tenant_site_bindings(tenant_id, site_id) ON DELETE CASCADE
            )
            """
        )
        self.database.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_tenant_memberships_user_site
            ON tenant_memberships(user_id, site_id, status)
            """
        )
        self.database.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_tenant_records_scope
            ON tenant_records(tenant_id, site_id, domain_key, min_gate, status)
            """
        )

    @staticmethod
    def validate_site(site_id: str) -> str:
        if site_id not in SUPPORTED_SITES:
            raise TenantValidationError("WORDPRESS_SITE_NOT_REGISTERED")
        return site_id

    @staticmethod
    def validate_gate_count(gate_count: int) -> int:
        if gate_count not in SUPPORTED_GATE_COUNTS:
            raise TenantValidationError("GATE_COUNT_MUST_BE_1_2_OR_4")
        return gate_count

    def create_tenant(
        self,
        tenant_name: str,
        owner_user_id: str,
        site_bindings: list[dict[str, Any]],
        tenant_type: str = "BUSINESS",
    ) -> dict:
        name = tenant_name.strip()
        owner = owner_user_id.strip()
        if not name or not owner:
            raise TenantValidationError("TENANT_NAME_AND_OWNER_REQUIRED")
        if not site_bindings:
            raise TenantValidationError("AT_LEAST_ONE_WEBSITE_BINDING_REQUIRED")

        normalized: list[tuple[str, int]] = []
        seen: set[str] = set()
        for binding in site_bindings:
            site_id = self.validate_site(str(binding.get("site_id", "")))
            gate_count = self.validate_gate_count(int(binding.get("gate_count", 1)))
            if site_id in seen:
                raise TenantValidationError("DUPLICATE_WEBSITE_BINDING")
            seen.add(site_id)
            normalized.append((site_id, gate_count))

        user = self.database.fetchone(
            "SELECT user_id FROM users WHERE user_id = ?",
            (owner,),
        )
        if user is None:
            raise TenantValidationError("TENANT_OWNER_NOT_FOUND")

        tenant_id = "TNT-" + secrets.token_hex(10).upper()
        self.database.begin()
        try:
            self.database.execute(
                """
                INSERT INTO tenants (tenant_id, tenant_name, tenant_type, owner_user_id)
                VALUES (?, ?, ?, ?)
                """,
                (tenant_id, name, tenant_type.strip().upper() or "BUSINESS", owner),
            )
            for site_id, gate_count in normalized:
                self.database.execute(
                    """
                    INSERT INTO tenant_site_bindings (tenant_id, site_id, gate_count)
                    VALUES (?, ?, ?)
                    """,
                    (tenant_id, site_id, gate_count),
                )
                self.database.execute(
                    """
                    INSERT INTO tenant_memberships
                    (tenant_id, site_id, user_id, gate_level, member_role)
                    VALUES (?, ?, ?, ?, 'OWNER')
                    """,
                    (tenant_id, site_id, owner, gate_count),
                )
            self.database.commit()
        except Exception:
            self.database.rollback()
            raise
        return self.get_tenant(tenant_id)

    def get_tenant(self, tenant_id: str) -> Optional[dict]:
        row = self.database.fetchone(
            """
            SELECT tenant_id, tenant_name, tenant_type, owner_user_id, status, created_at
            FROM tenants WHERE tenant_id = ?
            """,
            (tenant_id,),
        )
        if row is None:
            return None
        bindings = self.database.fetchall(
            """
            SELECT site_id, gate_count, status
            FROM tenant_site_bindings
            WHERE tenant_id = ? ORDER BY site_id
            """,
            (tenant_id,),
        )
        return {
            "tenant_id": row["tenant_id"],
            "tenant_name": row["tenant_name"],
            "tenant_type": row["tenant_type"],
            "owner_user_id": row["owner_user_id"],
            "status": row["status"],
            "created_at": row["created_at"],
            "site_bindings": [dict(item) for item in bindings],
        }

    def list_tenants_for_user(self, user_id: str) -> list[dict]:
        rows = self.database.fetchall(
            """
            SELECT t.tenant_id, t.tenant_name, t.tenant_type, t.owner_user_id,
                   t.status, m.site_id, b.gate_count, m.gate_level, m.member_role
            FROM tenant_memberships m
            JOIN tenants t ON t.tenant_id = m.tenant_id
            JOIN tenant_site_bindings b
              ON b.tenant_id = m.tenant_id AND b.site_id = m.site_id
            WHERE m.user_id = ? AND m.status = 'ACTIVE'
              AND t.status = 'ACTIVE' AND b.status = 'ACTIVE'
            ORDER BY t.tenant_name, m.site_id
            """,
            (user_id,),
        )
        return [dict(row) for row in rows]

    def list_site_spaces(self, user_id: str, site_id: str) -> list[dict]:
        self.validate_site(site_id)
        rows = self.database.fetchall(
            """
            SELECT t.tenant_id, t.tenant_name, t.tenant_type,
                   b.site_id, b.gate_count, m.gate_level, m.member_role
            FROM tenant_memberships m
            JOIN tenants t ON t.tenant_id = m.tenant_id
            JOIN tenant_site_bindings b
              ON b.tenant_id = m.tenant_id AND b.site_id = m.site_id
            WHERE m.user_id = ? AND m.site_id = ?
              AND m.status = 'ACTIVE' AND t.status = 'ACTIVE' AND b.status = 'ACTIVE'
            ORDER BY t.tenant_name
            """,
            (user_id, site_id),
        )
        return [dict(row) for row in rows]

    def get_membership(self, tenant_id: str, site_id: str, user_id: str) -> Optional[dict]:
        self.validate_site(site_id)
        row = self.database.fetchone(
            """
            SELECT m.tenant_id, m.site_id, m.user_id, m.gate_level,
                   m.member_role, m.status, b.gate_count
            FROM tenant_memberships m
            JOIN tenant_site_bindings b
              ON b.tenant_id = m.tenant_id AND b.site_id = m.site_id
            JOIN tenants t ON t.tenant_id = m.tenant_id
            WHERE m.tenant_id = ? AND m.site_id = ? AND m.user_id = ?
              AND m.status = 'ACTIVE' AND b.status = 'ACTIVE' AND t.status = 'ACTIVE'
            """,
            (tenant_id, site_id, user_id),
        )
        return dict(row) if row else None

    def add_member(
        self, tenant_id: str, site_id: str, user_id: str, gate_level: int
    ) -> dict:
        self.validate_site(site_id)
        user_id = user_id.strip()
        if not user_id:
            raise TenantValidationError("MEMBER_USER_ID_REQUIRED")
        binding = self.database.fetchone(
            """
            SELECT gate_count FROM tenant_site_bindings
            WHERE tenant_id = ? AND site_id = ? AND status = 'ACTIVE'
            """,
            (tenant_id, site_id),
        )
        if binding is None:
            raise TenantNotFoundError("TENANT_SITE_BINDING_NOT_FOUND")
        if not isinstance(gate_level, int) or not 1 <= gate_level <= int(binding["gate_count"]):
            raise TenantValidationError("MEMBER_GATE_LEVEL_EXCEEDS_SITE_GATE_COUNT")
        user = self.database.fetchone("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
        if user is None:
            raise TenantValidationError("MEMBER_USER_NOT_FOUND")
        self.database.execute(
            """
            INSERT INTO tenant_memberships
                (tenant_id, site_id, user_id, gate_level, member_role, status)
            VALUES (?, ?, ?, ?, 'MEMBER', 'ACTIVE')
            ON CONFLICT(tenant_id, site_id, user_id)
            DO UPDATE SET gate_level = excluded.gate_level,
                          status = 'ACTIVE',
                          updated_at = CURRENT_TIMESTAMP
            """,
            (tenant_id, site_id, user_id, gate_level),
        )
        return self.get_membership(tenant_id, site_id, user_id) or {}

    def list_members(self, tenant_id: str, site_id: str) -> list[dict]:
        self.validate_site(site_id)
        rows = self.database.fetchall(
            """
            SELECT user_id, gate_level, member_role, status, created_at
            FROM tenant_memberships
            WHERE tenant_id = ? AND site_id = ? AND status = 'ACTIVE'
            ORDER BY gate_level DESC, created_at
            """,
            (tenant_id, site_id),
        )
        return [dict(row) for row in rows]

    def create_record(
        self,
        tenant_id: str,
        site_id: str,
        domain_key: str,
        record_type: str,
        min_gate: int,
        payload: dict[str, Any],
        created_by: str,
    ) -> dict:
        self.validate_site(site_id)
        binding = self.database.fetchone(
            """
            SELECT gate_count FROM tenant_site_bindings
            WHERE tenant_id = ? AND site_id = ? AND status = 'ACTIVE'
            """,
            (tenant_id, site_id),
        )
        if binding is None:
            raise TenantNotFoundError("TENANT_SITE_BINDING_NOT_FOUND")
        if not isinstance(min_gate, int) or not 1 <= min_gate <= int(binding["gate_count"]):
            raise TenantValidationError("RECORD_GATE_LEVEL_EXCEEDS_SITE_GATE_COUNT")
        key = domain_key.strip().lower()
        kind = record_type.strip().lower()
        if not key or not kind:
            raise TenantValidationError("DOMAIN_KEY_AND_RECORD_TYPE_REQUIRED")
        record_id = "REC-" + secrets.token_hex(12).upper()
        payload_json = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
        self.database.execute(
            """
            INSERT INTO tenant_records
            (record_id, tenant_id, site_id, domain_key, record_type,
             min_gate, payload_json, created_by)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (record_id, tenant_id, site_id, key, kind, min_gate, payload_json, created_by),
        )
        return {
            "record_id": record_id,
            "tenant_id": tenant_id,
            "site_id": site_id,
            "domain_key": key,
            "record_type": kind,
            "min_gate": min_gate,
            "payload": payload,
            "created_by": created_by,
        }

    def list_records(
        self,
        tenant_id: str,
        site_id: str,
        gate_level: int,
        domain_key: Optional[str] = None,
        record_type: Optional[str] = None,
    ) -> list[dict]:
        self.validate_site(site_id)
        clauses = [
            "tenant_id = ?", "site_id = ?", "min_gate <= ?", "status = 'ACTIVE'"
        ]
        params: list[Any] = [tenant_id, site_id, gate_level]
        if domain_key:
            clauses.append("domain_key = ?")
            params.append(domain_key.strip().lower())
        if record_type:
            clauses.append("record_type = ?")
            params.append(record_type.strip().lower())
        rows = self.database.fetchall(
            f"""
            SELECT record_id, tenant_id, site_id, domain_key, record_type,
                   min_gate, payload_json, created_by, created_at
            FROM tenant_records
            WHERE {' AND '.join(clauses)}
            ORDER BY created_at DESC
            """,
            params,
        )
        records = []
        for row in rows:
            try:
                payload = json.loads(row["payload_json"])
            except (TypeError, ValueError):
                payload = {}
            records.append({
                "record_id": row["record_id"],
                "tenant_id": row["tenant_id"],
                "site_id": row["site_id"],
                "domain_key": row["domain_key"],
                "record_type": row["record_type"],
                "min_gate": row["min_gate"],
                "payload": payload,
                "created_by": row["created_by"],
                "created_at": row["created_at"],
            })
        return records


__all__ = [
    "TenantService", "TenantNotFoundError", "TenantAccessError",
    "TenantValidationError", "SUPPORTED_SITES", "SUPPORTED_GATE_COUNTS",
]
