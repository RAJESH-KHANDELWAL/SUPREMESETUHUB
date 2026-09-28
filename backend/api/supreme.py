from supreme_config import (
    APP_NAME,
    SUPREME_ID,
    BUSINESS_ID,
    COMPANY_ID,
    PERSON_ID,
)

from identity_service import (
    get_supreme_profile,
    get_person_profile,
    search_entities,
)

from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel

from backend.supreme.controller import SupremeController
from backend.supreme.control import SupremeControlService


router = APIRouter(
    prefix="/supreme",
    tags=["Supreme"]
)

controller = SupremeController()
controller.initialize()


class CommandRequest(BaseModel):
    command: str
    payload: dict | None = None


def _require_service_token(authorization: str | None):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="INVALID_TOKEN",
        )

    token = authorization.replace("Bearer ", "", 1).strip()

    if not SupremeControlService.validate_token(token):
        raise HTTPException(
            status_code=401,
            detail="UNAUTHORIZED",
        )

    return token


@router.get("/")
def get_owner():
    return controller.get()


@router.post("/")
def create_owner():

    owner = controller.create(
        master_id="MBF-000001",
        supreme_id="SUP-000001",
        owner_name="DR RAJESH KHANDELWAL IBC",
        username="RAJESHKHANDELWALOFFICIAL",
        email="demo@example.com",
        phone="+910000000000",
        password="123456"
    )

    return {
        "message": "Supreme Owner Created Successfully",
        "data": owner
    }


@router.put("/{supreme_id}")
def update_owner(supreme_id: str):

    return {
        "message": "Update API Coming Soon",
        "supreme_id": supreme_id
    }


@router.delete("/{supreme_id}")
def delete_owner(supreme_id: str):

    controller.delete(supreme_id)

    return {
        "message": "Supreme Owner Deleted Successfully"
    }


@router.get("/list")
def list_owner():
    return controller.list()


@router.post("/login")
def login(identifier: str):
    return controller.login(identifier)


@router.post("/logout")
def logout():
    return controller.logout()


@router.put("/change-password")
def change_password(
    supreme_id: str,
    password: str
):
    return controller.change_password(
        supreme_id,
        password
    )


@router.get("/control/status")
def control_status(
    authorization: str | None = Header(default=None),
):
    _require_service_token(authorization)
    return SupremeControlService.get_status(controller)


@router.post("/control/command")
def control_command(
    payload: CommandRequest,
    authorization: str | None = Header(default=None),
):
    _require_service_token(authorization)

    try:
        return SupremeControlService.execute_command(
            controller,
            payload.command,
            payload.payload or {},
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc
# ============================================================
# SUPREME OWNER PROFILE API
# ============================================================

@router.get("/status")
def supreme_status():
    profile = get_supreme_profile()

    return {
        "service": APP_NAME,
        "status": "active",
        "supreme_id": profile["supreme_id"],
        "owner_person_id": profile["owner_person_id"],
        "business_id": BUSINESS_ID,
        "company_id": COMPANY_ID,
        "role": profile["role"],
    }


@router.get("/profile")
def supreme_profile():
    return get_supreme_profile()


@router.get("/person")
def supreme_person():
    return get_person_profile()


@router.get("/search")
def supreme_search(q: str = ""):
    q = q.strip()

    if not q:
        raise HTTPException(
            status_code=400,
            detail="Missing q query parameter",
        )

    results = search_entities(q)

    return {
        "query": q,
        "results": results,
        "count": len(results),
    }


@router.get("/persons")
def persons_list():
    return {
        "service": APP_NAME,
        "people": [get_person_profile()],
    }


@router.get("/businesses")
def businesses_list():
    return {
        "service": APP_NAME,
        "businesses": [
            {
                "business_id": BUSINESS_ID,
                "owner_person_id": PERSON_ID,
                "supreme_id": SUPREME_ID,
                "name": "RAJESH KHANDELWAL OFFICIAL",
                "display_name": "👑 RAJESH KHANDELWAL OFFICIAL 👑",
            }
        ],
    }


@router.get("/companies")
def companies_list():
    return {
        "service": APP_NAME,
        "companies": [
            {
                "company_id": COMPANY_ID,
                "owner_person_id": PERSON_ID,
                "business_id": BUSINESS_ID,
                "supreme_id": SUPREME_ID,
                "name": "DR RAJESH KHANDELWAL IBC",
                "display_name": "👑 DR RAJESH KHANDELWAL IBC 👑",
            }
        ],
    }
