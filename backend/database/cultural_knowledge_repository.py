"""SQLite persistence adapter for approved cultural knowledge records."""
from __future__ import annotations
import json
from typing import Any
from backend.database.service import DatabaseService

class CulturalKnowledgeRepository:
    TABLE = "cultural_knowledge_records"

    def __init__(self, database: DatabaseService | None = None) -> None:
        self.database = database or DatabaseService()

    def initialize(self) -> None:
        self.database.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.TABLE} (
                record_id TEXT PRIMARY KEY,
                domain_id TEXT NOT NULL,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                source_url TEXT,
                source_kind TEXT NOT NULL,
                confidence TEXT NOT NULL,
                publication_status TEXT NOT NULL DEFAULT 'DRAFT',
                metadata_json TEXT NOT NULL DEFAULT '{{}}',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.database.execute(
            f"CREATE INDEX IF NOT EXISTS idx_{self.TABLE}_domain_status "
            f"ON {self.TABLE}(domain_id, publication_status)"
        )

    def save(self, record: dict[str, Any]) -> None:
        required = ("record_id", "domain_id", "title", "content", "source_kind", "confidence")
        missing = [key for key in required if not str(record.get(key, "")).strip()]
        if missing:
            raise ValueError("CULTURAL_RECORD_FIELDS_REQUIRED:" + ",".join(missing))
        self.initialize()
        self.database.execute(
            f"""INSERT INTO {self.TABLE}
            (record_id,domain_id,title,content,source_url,source_kind,confidence,publication_status,metadata_json,updated_at)
            VALUES (?,?,?,?,?,?,?,?,?,CURRENT_TIMESTAMP)
            ON CONFLICT(record_id) DO UPDATE SET
            domain_id=excluded.domain_id,title=excluded.title,content=excluded.content,
            source_url=excluded.source_url,source_kind=excluded.source_kind,
            confidence=excluded.confidence,publication_status=excluded.publication_status,
            metadata_json=excluded.metadata_json,updated_at=CURRENT_TIMESTAMP""",
            (record["record_id"], record["domain_id"], record["title"], record["content"],
             record.get("source_url"), record["source_kind"], record["confidence"],
             record.get("publication_status", "DRAFT"),
             json.dumps(record.get("metadata", {}), ensure_ascii=False)),
        )

    def get(self, record_id: str) -> dict[str, Any] | None:
        self.initialize()
        row = self.database.fetchone(
            f"SELECT * FROM {self.TABLE} WHERE record_id=?", (record_id,))
        if row is None:
            return None
        item = dict(row)
        item["metadata"] = json.loads(item.pop("metadata_json") or "{}")
        return item

    def search(self, query: str, domain_id: str | None = None, limit: int = 30) -> list[dict[str, Any]]:
        self.initialize()
        if not str(query).strip():
            return []
        limit = max(1, min(int(limit), 100))
        sql = f"""SELECT * FROM {self.TABLE}
                  WHERE publication_status='APPROVED'
                  AND (title LIKE ? OR content LIKE ?)"""
        params: list[Any] = [f"%{query}%", f"%{query}%"]
        if domain_id:
            sql += " AND domain_id=?"
            params.append(domain_id)
        sql += " ORDER BY updated_at DESC LIMIT ?"
        params.append(limit)
        rows = self.database.fetchall(sql, params)
        results = []
        for row in rows:
            item = dict(row)
            item["metadata"] = json.loads(item.pop("metadata_json") or "{}")
            results.append(item)
        return results
