"""Authenticated people-facing CRM API; all records are scoped to the signed-in user."""
from __future__ import annotations

from typing import Any, Literal

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field

from backend.crm.service import CRMService
from backend.security.dependencies import get_current_user
from backend.supreme.supreme_ecosystem.crm import CRMEcosystem

router = APIRouter(prefix="/api/v1/crm", tags=["CRM"], dependencies=[Depends(get_current_user)])
_service: CRMService | None = None
_ecosystem = CRMEcosystem()


def get_crm_service() -> CRMService:
    global _service
    if _service is None:
        _service = CRMService()
    return _service


def _actor(user: dict[str, Any]) -> str:
    return str(user.get("user_id") or user.get("username") or "")


class ContactCreate(BaseModel):
    full_name: str = Field(min_length=1, max_length=200)
    email: str = Field(default="", max_length=320)
    phone: str = Field(default="", max_length=64)
    whatsapp_phone: str = Field(default="", max_length=64)
    organization: str = Field(default="", max_length=200)
    address: str = Field(default="", max_length=1000)
    city: str = Field(default="", max_length=120)
    pincode: str = Field(default="", max_length=20)
    designation: str = Field(default="", max_length=160)
    verification_status: Literal["UNVERIFIED", "PENDING", "VERIFIED", "INVALID", "DO_NOT_USE"] = "UNVERIFIED"
    verification_evidence: str = Field(default="", max_length=1000)
    verified_at: str | None = Field(default=None, max_length=80)
    source: Literal["MANUAL", "GOOGLE_CONTACTS", "GOOGLE_SHEETS", "IMPORT"] = "MANUAL"
    external_id: str = Field(default="", max_length=500)
    notes: str = Field(default="", max_length=4000)
    tags: list[str] = Field(default_factory=list, max_length=30)
    consent_to_contact: bool = False
    contact_status: Literal["ACTIVE", "DO_NOT_CONTACT", "ARCHIVED"] = "ACTIVE"
    category: str = Field(default="UNCATEGORIZED", max_length=80)
    follow_up_at: str | None = Field(default=None, max_length=80)


class ContactUpdate(BaseModel):
    full_name: str | None = Field(default=None, min_length=1, max_length=200)
    email: str | None = Field(default=None, max_length=320)
    phone: str | None = Field(default=None, max_length=64)
    whatsapp_phone: str | None = Field(default=None, max_length=64)
    organization: str | None = Field(default=None, max_length=200)
    address: str | None = Field(default=None, max_length=1000)
    city: str | None = Field(default=None, max_length=120)
    pincode: str | None = Field(default=None, max_length=20)
    designation: str | None = Field(default=None, max_length=160)
    verification_status: Literal["UNVERIFIED", "PENDING", "VERIFIED", "INVALID", "DO_NOT_USE"] | None = None
    verification_evidence: str | None = Field(default=None, max_length=1000)
    verified_at: str | None = Field(default=None, max_length=80)
    notes: str | None = Field(default=None, max_length=4000)
    tags: list[str] | None = Field(default=None, max_length=30)
    consent_to_contact: bool | None = None
    contact_status: Literal["ACTIVE", "DO_NOT_CONTACT", "ARCHIVED"] | None = None
    category: str | None = Field(default=None, max_length=80)
    follow_up_at: str | None = Field(default=None, max_length=80)


class ContactActivityCreate(BaseModel):
    contact_id: str = Field(min_length=1, max_length=200)
    activity_type: Literal["CALL", "MEETING", "EMAIL", "WHATSAPP", "NOTE", "TASK", "STATUS_CHANGE", "OTHER"] = "NOTE"
    summary: str = Field(min_length=1, max_length=200)
    details: str = Field(default="", max_length=4000)
    outcome: str = Field(default="", max_length=1000)
    next_follow_up_at: str | None = Field(default=None, max_length=80)


class DailyItemCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    details: str = Field(default="", max_length=4000)
    contact_id: str | None = Field(default=None, max_length=200)
    item_type: Literal["TASK", "CALL", "MEETING", "FOLLOW_UP", "NOTE", "PERSONAL"] = "TASK"
    due_at: str | None = Field(default=None, max_length=80)


class DailyItemUpdate(BaseModel):
    status: Literal["OPEN", "IN_PROGRESS", "DONE", "CANCELLED"]


class ImportPreviewRequest(BaseModel):
    provider: Literal["GOOGLE_SHEETS", "GOOGLE_CONTACTS"]
    records: list[dict[str, Any]] = Field(max_length=500)


class MessageDraftRequest(BaseModel):
    purpose: str = Field(min_length=1, max_length=500)
    tone: Literal["friendly", "formal"] = "friendly"


class CRMImportRequest(BaseModel):
    provider: Literal["GOOGLE_SHEETS", "GOOGLE_CONTACTS"]
    records: list[dict[str, Any]] = Field(max_length=500)
    column_map: dict[str, str] = Field(default_factory=dict)
    confirm_import: bool = False


@router.get("/status")
def crm_status(user: dict[str, Any] = Depends(get_current_user)) -> dict[str, Any]:
    return {
        "success": True,
        "module": "CRM",
        "ecosystem": _ecosystem.status(),
        "permissions": {
            "scope": "SIGNED_IN_USER_RECORDS_ONLY",
            "role": user.get("role", "USER"),
            "can_manage_contacts": True,
            "can_request_ai_suggestions": True,
            "ai_external_provider_connected": False,
            "human_approval_required_for_outreach_and_sync": True,
        },
    }


@router.get("/contacts")
def list_contacts(
    category: str | None = None,
    contact_status: str | None = None,
    limit: int = Query(default=100, ge=1, le=500),
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    records = service.list_contacts(_actor(user), category=category, contact_status=contact_status, limit=limit)
    return {"success": True, "count": len(records), "data": records}


@router.post("/contacts", status_code=201)
def create_contact(
    request: ContactCreate,
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    try:
        record = service.create_contact(_actor(user), _actor(user), request.model_dump())
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    return {"success": True, "data": record}


@router.get("/contacts/{contact_id}")
def get_contact(
    contact_id: str,
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    record = service.get_contact(_actor(user), contact_id)
    if record is None:
        raise HTTPException(status_code=404, detail="CRM_CONTACT_NOT_FOUND")
    return {"success": True, "data": record}


@router.patch("/contacts/{contact_id}")
def update_contact(
    contact_id: str,
    request: ContactUpdate,
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    try:
        record = service.update_contact(_actor(user), _actor(user), contact_id, request.model_dump(exclude_unset=True))
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    if record is None:
        raise HTTPException(status_code=404, detail="CRM_CONTACT_NOT_FOUND")
    return {"success": True, "data": record}


@router.delete("/contacts/{contact_id}")
def delete_contact(
    contact_id: str,
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    if not service.delete_contact(_actor(user), _actor(user), contact_id):
        raise HTTPException(status_code=404, detail="CRM_CONTACT_NOT_FOUND")
    return {"success": True, "deleted": True}


@router.post("/activities", status_code=201)
def log_contact_activity(
    request: ContactActivityCreate,
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    try:
        activity = service.log_activity(_actor(user), _actor(user), request.model_dump())
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    return {"success": True, "data": activity}


@router.get("/contacts/{contact_id}/timeline")
def contact_timeline(
    contact_id: str,
    limit: int = Query(default=100, ge=1, le=500),
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    timeline = service.contact_timeline(_actor(user), contact_id, limit=limit)
    if timeline is None:
        raise HTTPException(status_code=404, detail="CRM_CONTACT_NOT_FOUND")
    return {"success": True, "count": len(timeline), "data": timeline}


@router.get("/quality/review-queue")
def quality_review_queue(
    limit: int = Query(default=200, ge=1, le=500),
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    return service.quality_review_queue(_actor(user), limit=limit)


@router.get("/contacts/{contact_id}/quality")
def contact_quality(
    contact_id: str,
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    result = service.assess_contact(_actor(user), contact_id)
    if result is None:
        raise HTTPException(status_code=404, detail="CRM_CONTACT_NOT_FOUND")
    return {"success": True, "data": result}


@router.get("/daily/briefing")
def daily_briefing(
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    return service.daily_briefing(_actor(user))


@router.get("/daily/items")
def list_daily_items(
    status: Literal["OPEN", "IN_PROGRESS", "DONE", "CANCELLED"] | None = None,
    limit: int = Query(default=200, ge=1, le=500),
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    items = service.repository.list_daily_items(_actor(user), status=status, limit=limit)
    return {"success": True, "count": len(items), "data": items}


@router.post("/daily/items", status_code=201)
def create_daily_item(
    request: DailyItemCreate,
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    try:
        item = service.create_daily_item(_actor(user), _actor(user), request.model_dump())
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    return {"success": True, "data": item}


@router.patch("/daily/items/{item_id}")
def update_daily_item(
    item_id: str,
    request: DailyItemUpdate,
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    try:
        item = service.update_daily_item(_actor(user), _actor(user), item_id, request.status)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    if item is None:
        raise HTTPException(status_code=404, detail="CRM_DAILY_ITEM_NOT_FOUND")
    return {"success": True, "data": item}


@router.get("/ai/duplicates")
def ai_duplicate_suggestions(
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    return {"success": True, "method": "RULES_BASED_MATCHING", "auto_merge": False,
            "human_review_required": True, "data": service.duplicate_candidates(_actor(user))}


@router.get("/ai/categories")
def ai_category_suggestions(
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    return {"success": True, "method": "TRANSPARENT_RULES", "auto_apply": False,
            "human_approval_required": True, "data": service.category_suggestions(_actor(user))}


@router.get("/ai/follow-ups")
def ai_follow_up_suggestions(
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    return {"success": True, "auto_message_sent": False, "data": service.follow_up_suggestions(_actor(user))}


@router.get("/reports/summary")
def report_summary(
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    return service.report(_actor(user))


@router.post("/contacts/{contact_id}/message-draft")
def create_message_draft(
    contact_id: str,
    request: MessageDraftRequest,
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    try:
        draft = service.draft_message(_actor(user), contact_id, request.purpose, request.tone)
    except PermissionError as exc:
        raise HTTPException(status_code=403, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    if draft is None:
        raise HTTPException(status_code=404, detail="CRM_CONTACT_NOT_FOUND")
    return {"success": True, "data": draft}


@router.post("/imports/preview")
def preview_import(
    request: CRMImportRequest,
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    try:
        return {"success": True, **service.preview_import(
            _actor(user), request.provider, request.records, request.column_map or None
        )}
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.post("/imports/commit")
def commit_import(
    request: CRMImportRequest,
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    try:
        return service.commit_import(
            _actor(user), _actor(user), request.provider, request.records,
            request.column_map or None, request.confirm_import,
        )
    except PermissionError as exc:
        raise HTTPException(status_code=403, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.get("/audit")
def list_audit_events(
    limit: int = Query(default=100, ge=1, le=500),
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(get_crm_service),
) -> dict[str, Any]:
    role = str(user.get("role", "USER")).upper()
    if role not in {"OWNER", "ADMIN"}:
        raise HTTPException(status_code=403, detail="CRM_AUDIT_ADMIN_REQUIRED")
    return {"success": True, "data": service.repository.list_audit_events(_actor(user), limit=limit)}


@router.post("/integrations/sync-preview")
def sync_preview(
    request: ImportPreviewRequest,
    user: dict[str, Any] = Depends(get_current_user),
) -> dict[str, Any]:
    from backend.crm.integrations import GoogleCRMIntegration
    try:
        return {"success": True, **GoogleCRMIntegration().preview_sync(request.provider, request.records)}
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
