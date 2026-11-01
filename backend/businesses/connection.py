"""SQLite repository for persistent Business domain records.

This repository uses the shared DatabaseService and owns only the
business_profiles table. It deliberately does not reuse the legacy generic
'business' table, whose schema is too small for the Business domain model.
"""
from __future__ import annotations

import json
from typing import Any

from backend.database.service import DatabaseService


class BusinessRepository:
    """Persist and retrieve Business records using the central SQLite service."""

    TABLE = "business_profiles"

    def __init__(self, database_service: DatabaseService | None = None) -> None:
        self.database = database_service or DatabaseService()
        self.initialize()

    def initialize(self) -> None:
        self.database.execute(
            """
            CREATE TABLE IF NOT EXISTS business_profiles (
                business_id TEXT PRIMARY KEY,
                owner_id TEXT NOT NULL,
                name TEXT NOT NULL,
                category TEXT NOT NULL DEFAULT '',
                location TEXT NOT NULL DEFAULT '',
                website TEXT NOT NULL DEFAULT '',
                public_contact TEXT NOT NULL DEFAULT '',
                source TEXT NOT NULL DEFAULT '',
                status TEXT NOT NULL DEFAULT 'ACTIVE',
                verified INTEGER NOT NULL DEFAULT 0,
                metadata_json TEXT NOT NULL DEFAULT '{}',
                legal_name TEXT NOT NULL DEFAULT '',
                business_type TEXT NOT NULL DEFAULT 'SMALL_BUSINESS',
                industry TEXT NOT NULL DEFAULT '',
                employee_count INTEGER,
                headquarters TEXT NOT NULL DEFAULT '',
                parent_company_id TEXT NOT NULL DEFAULT '',
                annual_revenue_band TEXT NOT NULL DEFAULT '',
                operating_regions_json TEXT NOT NULL DEFAULT '[]',
                departments_json TEXT NOT NULL DEFAULT '[]',
                tags_json TEXT NOT NULL DEFAULT '[]',
                compliance_status TEXT NOT NULL DEFAULT 'UNSPECIFIED',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        self.database.execute(
            "CREATE INDEX IF NOT EXISTS idx_business_profiles_owner ON business_profiles(owner_id)"
        )

    @staticmethod
    def _json(value: Any, fallback: Any) -> str:
        return json.dumps(fallback if value is None else value, ensure_ascii=False)

    @staticmethod
    def _decode_json(value: str | None, fallback: Any) -> Any:
        if not value:
            return fallback
        try:
            return json.loads(value)
        except (TypeError, json.JSONDecodeError):
            return fallback

    def _to_values(self, record: Any) -> tuple[Any, ...]:
        data = record.to_dict()
        return (
            data["business_id"], data["owner_id"], data["name"], data["category"],
            data["location"], data["website"], data["public_contact"], data["source"],
            data["status"], int(bool(data["verified"])), self._json(data["metadata"], {}),
            data["legal_name"], data["business_type"], data["industry"], data["employee_count"],
            data["headquarters"], data["parent_company_id"], data["annual_revenue_band"],
            self._json(data["operating_regions"], []), self._json(data["departments"], []),
            self._json(data["tags"], []), data["compliance_status"],
        )

    def create(self, record: Any) -> Any:
        columns = (
            "business_id, owner_id, name, category, location, website, public_contact, source, "
            "status, verified, metadata_json, legal_name, business_type, industry, employee_count, "
            "headquarters, parent_company_id, annual_revenue_band, operating_regions_json, "
            "departments_json, tags_json, compliance_status"
        )
        placeholders = ", ".join("?" for _ in range(22))
        self.database.execute(
            f"INSERT INTO business_profiles ({columns}) VALUES ({placeholders})",
            self._to_values(record),
        )
        return record

    def _row_to_record(self, row: Any) -> Any:
        from backend.businesses.model import Business

        return Business(
            business_id=row["business_id"], owner_id=row["owner_id"], name=row["name"],
            category=row["category"], location=row["location"], website=row["website"],
            public_contact=row["public_contact"], source=row["source"], status=row["status"],
            verified=bool(row["verified"]), metadata=self._decode_json(row["metadata_json"], {}),
            legal_name=row["legal_name"], business_type=row["business_type"],
            industry=row["industry"], employee_count=row["employee_count"],
            headquarters=row["headquarters"], parent_company_id=row["parent_company_id"],
            annual_revenue_band=row["annual_revenue_band"],
            operating_regions=self._decode_json(row["operating_regions_json"], []),
            departments=self._decode_json(row["departments_json"], []),
            tags=self._decode_json(row["tags_json"], []),
            compliance_status=row["compliance_status"],
        )

    def get(self, business_id: str) -> Any | None:
        row = self.database.fetchone(
            "SELECT * FROM business_profiles WHERE business_id = ?", (business_id,)
        )
        return self._row_to_record(row) if row is not None else None

    def list(self) -> list[Any]:
        rows = self.database.fetchall(
            "SELECT * FROM business_profiles ORDER BY created_at, business_id"
        )
        return [self._row_to_record(row) for row in rows]

    def update(self, record: Any) -> Any:
        values = self._to_values(record)
        assignments = (
            "owner_id=?, name=?, category=?, location=?, website=?, public_contact=?, source=?, "
            "status=?, verified=?, metadata_json=?, legal_name=?, business_type=?, industry=?, "
            "employee_count=?, headquarters=?, parent_company_id=?, annual_revenue_band=?, "
            "operating_regions_json=?, departments_json=?, tags_json=?, compliance_status=?, "
            "updated_at=CURRENT_TIMESTAMP"
        )
        self.database.execute(
            f"UPDATE business_profiles SET {assignments} WHERE business_id=?",
            values[1:] + (values[0],),
        )
        return self.get(record.business_id)

    def delete(self, business_id: str) -> bool:
        cursor = self.database.execute(
            "DELETE FROM business_profiles WHERE business_id = ?", (business_id,)
        )
        return cursor.rowcount > 0
