from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend.api.crm import get_crm_service, router
from backend.crm.repository import CRMRepository
from backend.crm.service import CRMService
from backend.database.service import DatabaseService
from backend.security.dependencies import get_current_user


def test_crm_api_scopes_records_and_keeps_sync_preview_read_only(tmp_path):
    database = DatabaseService(db_path=str(tmp_path / "api-crm.db"))
    service = CRMService(CRMRepository(database))
    app = FastAPI()
    app.include_router(router)
    app.dependency_overrides[get_current_user] = lambda: {
        "authenticated": True, "user_id": "user-1", "username": "u1", "role": "USER"
    }
    app.dependency_overrides[get_crm_service] = lambda: service
    client = TestClient(app)
    try:
        created = client.post("/api/v1/crm/contacts", json={
            "full_name": "Asha", "email": "asha@example.com"
        })
        assert created.status_code == 201
        contact_id = created.json()["data"]["contact_id"]
        assert client.get("/api/v1/crm/contacts").json()["count"] == 1
        preview = client.post("/api/v1/crm/integrations/sync-preview", json={
            "provider": "GOOGLE_SHEETS", "records": [{"Name": "Asha"}]
        })
        assert preview.status_code == 200
        assert preview.json()["records_written"] == 0
        assert preview.json()["write_enabled"] is False
        assert client.get(f"/api/v1/crm/contacts/{contact_id}").status_code == 200
    finally:
        database.close()
