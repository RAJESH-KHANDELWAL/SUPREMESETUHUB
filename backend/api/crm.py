"""Authenticated people-facing CRM API; all records are scoped to the signed-in user."""
from __future__ import annotations

from typing import Any, Literal

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field

from backend.crm.service import CRMService
from backend.security.dependencies import get_current_user
from backend.supreme.supreme_ecosystem.crm import CRMEcosystem

router = APIRouter(prefix="/api/v1/crm", tags=["CRM"], dependencies=[Depends(get_current_user)])
_service = CRMService()
_ecosystem = CRMEcosystem()


def get_crm_service() -> CRMService:
    return _service


def _actor(user: dict[str, Any]) -> str:
    return str(user.get("user_id") or user.get("username") or "")


def _service_for_request() -> CRMService:
    return get_crm_service()


class ContactCreate(BaseModel):
    full_name: str = Field(min_length=1, max_length=200)
    email: str = Field(default="", max_length=320)
    phone: str = Field(default="", max_length=64)
    organization: str = Field(default="", max_length=200)
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
    organization: str | None = Field(default=None, max_length=200)
    notes: str | None = Field(default=None, max_length=4000)
    tags: list[str] | None = Field(default=None, max_length=30)
    consent_to_contact: bool | None = None
    contact_status: Literal["ACTIVE", "DO_NOT_CONTACT", "ARCHIVED"] | None = None
    category: str | None = Field(default=None, max_length=80)
    follow_up_at: str | None = Field(default=None, max_length=80)


class ImportPreviewRequest(BaseModel):
    provider: Literal["GOOGLE_SHEETS", "GOOGLE_CONTACTS"]
    records: list[dict[str, Any]] = Field(max_length=500)


class MessageDraftRequest(BaseModel):
    purpose: str = Field(min_length=1, max_length=500)
    tone: Literal["friendly", "formal"] = "friendly"


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
    service: CRMService = Depends(_service_for_request),
) -> dict[str, Any]:
    records = service.list_contacts(_actor(user), category=category, contact_status=contact_status, limit=limit)
    return {"success": True, "count": len(records), "data": records}


@router.post("/contacts", status_code=201)
def create_contact(
    request: ContactCreate,
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(_service_for_request),
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
    service: CRMService = Depends(_service_for_request),
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
    service: CRMService = Depends(_service_for_request),
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
    service: CRMService = Depends(_service_for_request),
) -> dict[str, Any]:
    if not service.delete_contact(_actor(user), _actor(user), contact_id):
        raise HTTPException(status_code=404, detail="CRM_CONTACT_NOT_FOUND")
    return {"success": True, "deleted": True}


@router.get("/ai/duplicates")
def ai_duplicate_suggestions(
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(_service_for_request),
) -> dict[str, Any]:
    return {"success": True, "method": "RULES_BASED_MATCHING", "auto_merge": False,
            "human_review_required": True, "data": service.duplicate_candidates(_actor(user))}


@router.get("/ai/categories")
def ai_category_suggestions(
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(_service_for_request),
) -> dict[str, Any]:
    return {"success": True, "method": "TRANSPARENT_RULES", "auto_apply": False,
            "human_approval_required": True, "data": service.category_suggestions(_actor(user))}


@router.get("/ai/follow-ups")
def ai_follow_up_suggestions(
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(_service_for_request),
) -> dict[str, Any]:
    return {"success": True, "auto_message_sent": False, "data": service.follow_up_suggestions(_actor(user))}


@router.get("/reports/summary")
def report_summary(
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(_service_for_request),
) -> dict[str, Any]:
    return service.report(_actor(user))


@router.post("/contacts/{contact_id}/message-draft")
def create_message_draft(
    contact_id: str,
    request: MessageDraftRequest,
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(_service_for_request),
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


@router.get("/audit")
def list_audit_events(
    limit: int = Query(default=100, ge=1, le=500),
    user: dict[str, Any] = Depends(get_current_user),
    service: CRMService = Depends(_service_for_request),
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
