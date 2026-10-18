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


def test_quality_and_daily_workflow_api(tmp_path):
    database = DatabaseService(db_path=str(tmp_path / "quality-api-crm.db"))
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
            "full_name": "Asha", "phone": "9876543210", "email": "bad-email",
            "whatsapp_phone": "", "address": "", "city": ""
        })
        assert created.status_code == 201
        contact_id = created.json()["data"]["contact_id"]
        quality = client.get(f"/api/v1/crm/contacts/{contact_id}/quality")
        assert quality.status_code == 200
        assert quality.json()["data"]["quality_label"] == "REVIEW_REQUIRED"
        queue = client.get("/api/v1/crm/quality/review-queue")
        assert queue.status_code == 200
        assert queue.json()["flagged_count"] == 1

        task = client.post("/api/v1/crm/daily/items", json={
            "title": "Review Asha contact", "item_type": "TASK", "contact_id": contact_id
        })
        assert task.status_code == 201
        item_id = task.json()["data"]["item_id"]
        done = client.patch(f"/api/v1/crm/daily/items/{item_id}", json={"status": "DONE"})
        assert done.status_code == 200
        assert done.json()["data"]["status"] == "DONE"
        assert client.get("/api/v1/crm/daily/briefing").json()["summary"]["done"] == 1
    finally:
        database.close()


def test_contact_activity_timeline_api(tmp_path):
    database = DatabaseService(db_path=str(tmp_path / "activity-api-crm.db"))
    service = CRMService(CRMRepository(database))
    app = FastAPI()
    app.include_router(router)
    app.dependency_overrides[get_current_user] = lambda: {
        "authenticated": True, "user_id": "user-1", "username": "u1", "role": "USER"
    }
    app.dependency_overrides[get_crm_service] = lambda: service
    client = TestClient(app)
    try:
        contact = client.post("/api/v1/crm/contacts", json={
            "full_name": "Asha", "phone": "9876543210"
        }).json()["data"]
        logged = client.post("/api/v1/crm/activities", json={
            "contact_id": contact["contact_id"], "activity_type": "WHATSAPP",
            "summary": "Sent a consented reply draft after human review",
            "outcome": "Waiting for response"
        })
        assert logged.status_code == 201
        timeline = client.get(f"/api/v1/crm/contacts/{contact['contact_id']}/timeline")
        assert timeline.status_code == 200
        assert timeline.json()["data"][0]["activity_type"] == "WHATSAPP"
    finally:
        database.close()
