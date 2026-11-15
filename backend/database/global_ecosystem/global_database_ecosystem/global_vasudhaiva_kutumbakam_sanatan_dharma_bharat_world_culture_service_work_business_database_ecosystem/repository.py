"""SQLite repository for culture-service-work-business records."""
from __future__ import annotations
import json
from typing import Any
from backend.database.service import DatabaseService
from backend.core.global_ecosystem.global_core_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_core_ecosystem.governance import validate_record
class GlobalCultureServiceWorkBusinessRepository:
    TABLE="culture_service_work_business_records"
    def __init__(self,database:DatabaseService|None=None)->None: self.database=database or DatabaseService()
    def initialize(self)->None:
        self.database.execute(f"""CREATE TABLE IF NOT EXISTS {self.TABLE} (
        record_id TEXT PRIMARY KEY, capability_id TEXT NOT NULL, record_type TEXT NOT NULL,
        title TEXT NOT NULL, description TEXT NOT NULL, organization_name TEXT, location TEXT,
        website_url TEXT, source_url TEXT, status TEXT NOT NULL DEFAULT 'DRAFT',
        metadata_json TEXT NOT NULL DEFAULT '{{}}', created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)""")
        self.database.execute(f"CREATE INDEX IF NOT EXISTS idx_{self.TABLE}_capability ON {self.TABLE}(capability_id,status)")
    def save(self,record:dict[str,Any])->None:
        errors=validate_record(record)
        if errors: raise ValueError("RECORD_VALIDATION_FAILED:"+",".join(errors))
        self.initialize()
        self.database.execute(f"""INSERT INTO {self.TABLE}
        (record_id,capability_id,record_type,title,description,organization_name,location,website_url,source_url,status,metadata_json,updated_at)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,CURRENT_TIMESTAMP)
        ON CONFLICT(record_id) DO UPDATE SET capability_id=excluded.capability_id,record_type=excluded.record_type,
        title=excluded.title,description=excluded.description,organization_name=excluded.organization_name,
        location=excluded.location,website_url=excluded.website_url,source_url=excluded.source_url,
        status=excluded.status,metadata_json=excluded.metadata_json,updated_at=CURRENT_TIMESTAMP""",
        (record["record_id"],record["capability_id"],record["record_type"],record["title"],record["description"],record.get("organization_name"),record.get("location"),record.get("website_url"),record.get("source_url"),str(record.get("status","DRAFT")).upper(),json.dumps(record.get("metadata",{}),ensure_ascii=False)))
    def get(self,record_id:str)->dict[str,Any]|None:
        self.initialize(); row=self.database.fetchone(f"SELECT * FROM {self.TABLE} WHERE record_id=?",(record_id,))
        if row is None:return None
        item=dict(row);item["metadata"]=json.loads(item.pop("metadata_json") or "{}");return item
    def search(self,query:str="",capability_id:str|None=None,limit:int=50)->list[dict[str,Any]]:
        self.initialize();sql=f"SELECT * FROM {self.TABLE} WHERE status='APPROVED'";params:list[Any]=[]
        if query.strip():sql+=" AND (title LIKE ? OR description LIKE ? OR organization_name LIKE ?)";params.extend([f"%{query.strip()}%"]*3)
        if capability_id:sql+=" AND capability_id=?";params.append(capability_id)
        sql+=" ORDER BY updated_at DESC LIMIT ?";params.append(max(1,min(int(limit),100)))
        result=[]
        for row in self.database.fetchall(sql,params):
            item=dict(row);item["metadata"]=json.loads(item.pop("metadata_json") or "{}");result.append(item)
        return result
    def health(self)->dict[str,Any]:
        try:self.initialize();return {"status":"READY","table":self.TABLE}
        except Exception as exc:return {"status":"UNAVAILABLE","error_type":type(exc).__name__}
