"""SQLite persistence for business records."""
from __future__ import annotations
import json
from typing import Any
from backend.database.service import DatabaseService
from .model import Business

class BusinessRepository:
    def __init__(self, database: DatabaseService | None = None) -> None:
        self.database = database or DatabaseService()

    def initialize(self) -> None:
        self.database.execute("""
            CREATE TABLE IF NOT EXISTS business_records (
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
        """)

    @staticmethod
    def _decode(row: Any) -> Business | None:
        if row is None:
            return None
        return Business(
            business_id=row["business_id"], owner_id=row["owner_id"], name=row["name"],
            category=row["category"], location=row["location"], website=row["website"],
            public_contact=row["public_contact"], source=row["source"], status=row["status"],
            verified=bool(row["verified"]), metadata=json.loads(row["metadata_json"] or "{}"),
            legal_name=row["legal_name"], business_type=row["business_type"], industry=row["industry"],
            employee_count=row["employee_count"], headquarters=row["headquarters"],
            parent_company_id=row["parent_company_id"], annual_revenue_band=row["annual_revenue_band"],
            operating_regions=json.loads(row["operating_regions_json"] or "[]"),
            departments=json.loads(row["departments_json"] or "[]"), tags=json.loads(row["tags_json"] or "[]"),
            compliance_status=row["compliance_status"], created_at=row["created_at"], updated_at=row["updated_at"],
        )

    def create(self, values: dict[str, Any]) -> Business:
        self.initialize()
        fields = (
            "business_id","owner_id","name","category","location","website","public_contact","source",
            "status","verified","metadata_json","legal_name","business_type","industry","employee_count",
            "headquarters","parent_company_id","annual_revenue_band","operating_regions_json",
            "departments_json","tags_json","compliance_status"
        )
        payload = dict(values)
        for key in ("metadata", "operating_regions", "departments", "tags"):
            payload[key + "_json"] = json.dumps(payload.pop(key, {} if key == "metadata" else []), ensure_ascii=False)
        payload["verified"] = int(bool(payload.get("verified", False)))
        self.database.execute(
            f"INSERT INTO business_records ({','.join(fields)}) VALUES ({','.join('?' for _ in fields)})",
            tuple(payload.get(key) for key in fields),
        )
        return self.get(payload["business_id"])

    def get(self, business_id: str) -> Business | None:
        self.initialize()
        row = self.database.fetchone("SELECT * FROM business_records WHERE business_id = ?", (business_id,))
        return self._decode(row)

    def list(self) -> list[Business]:
        self.initialize()
        return [self._decode(row) for row in self.database.fetchall(
            "SELECT * FROM business_records ORDER BY created_at DESC, business_id"
        )]

    def update_status(self, business_id: str, status: str) -> Business | None:
        self.initialize()
        self.database.execute(
            "UPDATE business_records SET status = ?, updated_at = CURRENT_TIMESTAMP WHERE business_id = ?",
            (status, business_id),
        )
        return self.get(business_id)

    def verify(self, business_id: str) -> Business | None:
        self.initialize()
        self.database.execute(
            "UPDATE business_records SET verified = 1, updated_at = CURRENT_TIMESTAMP WHERE business_id = ?",
            (business_id,),
        )
        return self.get(business_id)

    def delete(self, business_id: str) -> bool:
        self.initialize()
        cursor = self.database.execute("DELETE FROM business_records WHERE business_id = ?", (business_id,))
        return cursor.rowcount > 0
