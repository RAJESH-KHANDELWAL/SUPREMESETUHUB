"""Owner-only CRM and referral endpoints for the GLOBAL CORE PEOPLE ENGINE.

These routes are private by default. They do not send messages or claim that
pending commissions are collected revenue.
"""
from __future__ import annotations

from typing import Any, Literal

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field

from backend.core.global_ecosystem.global_core_ecosystem.referral_service import (
    SupremeReferralService,
)
from backend.security.dependencies import require_admin

router = APIRouter(
    prefix="/api/v1/people",
    tags=["GLOBAL CORE PEOPLE ENGINE"],
    dependencies=[Depends(require_admin)],
)
service = SupremeReferralService()


class PersonCreateRequest(BaseModel):
    display_name: str = Field(min_length=1, max_length=200)
    source_platform: str = Field(min_length=1, max_length=80)
    need_category: str = Field(min_length=1, max_length=100)
    situation_notes: str = Field(default="", max_length=4000)
    preferred_channel: Literal["WHATSAPP", "EMAIL", "PHONE", "IN_PLATFORM"] = "IN_PLATFORM"
    whatsapp_contact: str = Field(default="", max_length=64)
    contact_consent: bool = False
    response_stage: str = "NEW"
    next_follow_up_at: str | None = None


class PersonStageRequest(BaseModel):
    response_stage: str = Field(min_length=1, max_length=40)
    next_follow_up_at: str | None = None


class ReferralLinkCreateRequest(BaseModel):
    platform: str = Field(min_length=1, max_length=80)
    program_name: str = Field(min_length=1, max_length=200)
    referral_url: str = Field(min_length=1, max_length=2048)
    whatsapp_contact: str = Field(default="", max_length=64)
    ownership_type: Literal["PERSONAL", "TEAM"] = "PERSONAL"
    active: bool = True


class CommissionCreateRequest(BaseModel):
    partner_name: str = Field(min_length=1, max_length=200)
    order_reference: str = Field(min_length=1, max_length=200)
    amount_paise: int = Field(ge=0)
    currency: str = Field(default="INR", min_length=3, max_length=3)
    person_id: str | None = None
    referral_id: str | None = None
    evidence_reference: str = Field(default="", max_length=1000)


def _call_or_422(callable_, *args, **kwargs):
    try:
        return callable_(*args, **kwargs)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.get("/summary")
def people_summary() -> dict[str, Any]:
    """Return privacy-safe counts; no contact records are exposed here."""
    people = service.list_people(limit=500)
    links = service.list_referral_links()
    commissions = service.list_commissions(limit=500)
    return {
        "success": True,
        "people_count": len(people),
        "consented_to_contact_count": sum(bool(item.get("contact_consent")) for item in people),
        "active_referral_links_count": sum(bool(item.get("active")) for item in links),
        "commission_records_count": len(commissions),
        "pending_commission_records_count": sum(
            str(item.get("status", "")).upper() == "PENDING" for item in commissions
        ),
        "note": "Commission records are not proof of collected revenue or payout.",
    }


@router.get("/")
def list_people(
    response_stage: str | None = None,
    limit: int = Query(default=100, ge=1, le=500),
) -> dict[str, Any]:
    records = service.list_people(response_stage=response_stage, limit=limit)
    return {"success": True, "count": len(records), "data": records}


@router.post("/", status_code=201)
def create_person(request: PersonCreateRequest) -> dict[str, Any]:
    record = _call_or_422(service.create_person, request.model_dump())
    return {"success": True, "data": record}


@router.get("/{person_id}")
def get_person(person_id: str) -> dict[str, Any]:
    record = service.get_person(person_id)
    if record is None:
        raise HTTPException(status_code=404, detail="PERSON_NOT_FOUND")
    return {"success": True, "data": record}


@router.patch("/{person_id}/stage")
def update_person_stage(person_id: str, request: PersonStageRequest) -> dict[str, Any]:
    record = _call_or_422(
        service.set_person_stage,
        person_id,
        request.response_stage,
        request.next_follow_up_at,
    )
    if record is None:
        raise HTTPException(status_code=404, detail="PERSON_NOT_FOUND")
    return {"success": True, "data": record}


@router.get("/referral-links/list")
def list_referral_links(
    platform: str | None = None,
    active_only: bool = False,
) -> dict[str, Any]:
    records = service.list_referral_links(platform=platform, active_only=active_only)
    return {"success": True, "count": len(records), "data": records}


@router.post("/referral-links", status_code=201)
def create_referral_link(request: ReferralLinkCreateRequest) -> dict[str, Any]:
    record = _call_or_422(service.create_referral_link, request.model_dump())
    return {"success": True, "data": record}


@router.get("/events/list")
def list_events(
    person_id: str | None = None,
    limit: int = Query(default=100, ge=1, le=500),
) -> dict[str, Any]:
    records = service.list_events(person_id=person_id, limit=limit)
    return {"success": True, "count": len(records), "data": records}


@router.get("/commissions/list")
def list_commissions(
    status: str | None = None,
    limit: int = Query(default=100, ge=1, le=500),
) -> dict[str, Any]:
    records = service.list_commissions(status=status, limit=limit)
    return {
        "success": True,
        "count": len(records),
        "data": records,
        "note": "Commission status is not payment-gateway reconciliation or collected revenue.",
    }


@router.post("/commissions", status_code=201)
def create_commission(request: CommissionCreateRequest) -> dict[str, Any]:
    record = _call_or_422(service.create_commission, request.model_dump())
    return {
        "success": True,
        "data": record,
        "note": "New commission records remain PENDING until verified evidence supports a status change.",
    }
