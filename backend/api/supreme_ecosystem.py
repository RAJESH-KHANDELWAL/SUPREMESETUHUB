"""SUPREME ECOSYSTEM account, dashboard and integration-status API."""

from __future__ import annotations

import os

from fastapi import APIRouter, Depends, Header, HTTPException
from pydantic import BaseModel, EmailStr, Field, field_validator

from backend.auth.service import AuthenticationService
from backend.core.global_ecosystem.global_core_ecosystem.partner_programs import get_partner_program_catalog
from backend.supreme.capability_registry import get_capability_catalog
from backend.supreme.control import SupremeControlService
from backend.supreme.controller import SupremeController
from backend.users.service import UserService
from backend.supreme.config import USERNAME as SUPREME_OWNER_USERNAME
from backend.supreme.supreme_ecosystem.supreme_business_ecosystem import status as business_ecosystem_status
from backend.supreme.supreme_ecosystem.supreme_ai_ecosystem import status as ai_ecosystem_status
from backend.supreme.supreme_owner_admin.service import SupremeOwnerAdminService
from backend.supreme.rajesh_khandelwal import get_identity as get_rajesh_identity
from backend.supreme.rajesh_khandelwal_official import get_identity as get_rajesh_official_identity
from backend.supreme.dr_rajesh_khandelwal_ibc import get_identity as get_ibc_identity
from backend.supreme.dr_rajesh_khandelwal_ibc_official import get_identity as get_ibc_official_identity
from backend.supreme.social_media_control.registry import social_platform_status


authentication_service = AuthenticationService()
user_service = UserService()


class SignupRequest(BaseModel):
    full_name: str = Field(min_length=1, max_length=120)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    confirm_password: str = Field(min_length=8, max_length=128)

    @field_validator("full_name")
    @classmethod
    def clean_name(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("FULL_NAME_REQUIRED")
        return value

    @field_validator("confirm_password")
    @classmethod
    def passwords_match(cls, value: str, info):
        password = info.data.get("password")
        if password and value != password:
            raise ValueError("PASSWORDS_DO_NOT_MATCH")
        return value


class SigninRequest(BaseModel):
    username: str = Field(min_length=1, max_length=100)
    password: str = Field(min_length=1, max_length=128)


class EcosystemControlCommandRequest(BaseModel):
    command: str = Field(min_length=1, max_length=80)
    payload: dict = Field(default_factory=dict)


def require_supreme_ecosystem_owner(
    authorization: str | None = Header(default=None, alias="Authorization"),
) -> str:
    """Require an active session for the configured private SUPREME owner."""
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="AUTHENTICATION_REQUIRED",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = authorization[len("Bearer "):].strip()
    if not token:
        raise HTTPException(status_code=401, detail="AUTHENTICATION_REQUIRED")

    result = authentication_service.validate_token(token)
    if not isinstance(result, dict) or not result.get("authenticated"):
        raise HTTPException(
            status_code=401,
            detail=result.get("message", "INVALID_OR_EXPIRED_TOKEN")
            if isinstance(result, dict) else "INVALID_OR_EXPIRED_TOKEN",
            headers={"WWW-Authenticate": "Bearer"},
        )

    username = str(result.get("username", "")).strip()
    if username.casefold() != SUPREME_OWNER_USERNAME.casefold():
        raise HTTPException(
            status_code=403,
            detail="SUPREME_ECOSYSTEM_PRIVATE",
        )
    return username


router = APIRouter(
    prefix="/api/v1/supreme-ecosystem",
    tags=["SUPREME ECOSYSTEM"],
    dependencies=[Depends(require_supreme_ecosystem_owner)],
)


def _current_user(authorization: str | None) -> tuple[str, object]:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="AUTHENTICATION_REQUIRED",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = authorization[len("Bearer "):].strip()
    result = authentication_service.validate_token(token)
    if not result.get("authenticated"):
        raise HTTPException(
            status_code=401,
            detail=result.get("message", "INVALID_OR_EXPIRED_TOKEN"),
            headers={"WWW-Authenticate": "Bearer"},
        )

    username = str(result.get("username", "")).strip()
    user = user_service.search_user_by_username(username)
    if user is None:
        raise HTTPException(status_code=404, detail="ACCOUNT_NOT_FOUND")
    return username, user


@router.get("/status")
def ecosystem_status():
    return {
        "success": True,
        "system": "SUPREME ECOSYSTEM",
        "status": "ACTIVE",
        "parent": "MAIN SUPREME",
        "privacy": "PRIVATE_BY_DEFAULT",
        "modules": [
            "SIGNUP",
            "SIGNIN",
            "DASHBOARD",
            "ACCOUNT",
            "GOOGLE_GMAIL",
            "MICROSOFT",
            "WHATSAPP_AI",
            "SUPREME_OWNER_ADMIN",
            "WORDPRESS_OWNER_CONTROL",
            "HOSTINGER_REFERRAL_REGISTRY",
            "GOOGLE_OWNER_ACCOUNT_CONTROL",
        ],
    }



@router.get("/owner-admin/profiles")
def supreme_owner_admin_profiles():
    """Return the four registered owner identity cards for the private dashboard.

    Profile and cover image URLs are optional public image URLs configured through
    deployment environment variables. The API never guesses image URLs or exposes
    credentials. Registry IDs are internal SUPREME IDs, not external social IDs.
    """
    profiles = [
        get_rajesh_identity(),
        get_rajesh_official_identity(),
        get_ibc_identity(),
        get_ibc_official_identity(),
    ]
    image_keys = (
        ("SUPREME_PROFILE_RAJESH_KHANDELWAL_AVATAR_URL", "SUPREME_PROFILE_RAJESH_KHANDELWAL_COVER_URL"),
        ("SUPREME_PROFILE_RAJESH_KHANDELWAL_OFFICIAL_AVATAR_URL", "SUPREME_PROFILE_RAJESH_KHANDELWAL_OFFICIAL_COVER_URL"),
        ("SUPREME_PROFILE_DR_RAJESH_KHANDELWAL_IBC_AVATAR_URL", "SUPREME_PROFILE_DR_RAJESH_KHANDELWAL_IBC_COVER_URL"),
        ("SUPREME_PROFILE_DR_RAJESH_KHANDELWAL_IBC_OFFICIAL_AVATAR_URL", "SUPREME_PROFILE_DR_RAJESH_KHANDELWAL_IBC_OFFICIAL_COVER_URL"),
    )
    result = []
    for profile, (avatar_key, cover_key) in zip(profiles, image_keys):
        item = dict(profile)
        item["avatar_url"] = os.getenv(avatar_key, "").strip() or None
        item["cover_url"] = os.getenv(cover_key, "").strip() or None
        item["avatar_config_key"] = avatar_key
        item["cover_config_key"] = cover_key
        item["image_status"] = "CONFIGURED" if item["avatar_url"] and item["cover_url"] else "IMAGE_URLS_NOT_FULLY_CONFIGURED"
        item["external_ids_verified"] = False
        result.append(item)
    return {
        "success": True,
        "privacy": "OWNER_ONLY",
        "count": len(result),
        "profiles": result,
        "note": "Profile IDs shown here are SUPREME internal registry IDs. Set each avatar/cover URL using the named deployment environment variables; external social IDs and live account ownership are not verified by this registry.",
    }


@router.get("/owner-admin/status")
def supreme_owner_admin_status():
    """Private owner-only governance status for the SUPREME control plane."""
    return SupremeOwnerAdminService().owner_status()


@router.get("/owner-admin/owned-platforms")
def supreme_owner_admin_owned_platforms():
    """List the owner's registered platforms, including WordPress sites."""
    service = SupremeOwnerAdminService()
    return {
        "success": True,
        "privacy": "OWNER_ONLY",
        "owned_platforms": service.owned_platforms(),
    }


@router.get("/owner-admin/google-accounts")
def supreme_owner_admin_google_accounts():
    """List owner-approved Google identities and their safe connection readiness."""
    service = SupremeOwnerAdminService()
    return {
        "success": True,
        "privacy": "OWNER_ONLY",
        "accounts": service.google_owner_accounts(),
        "live_connection_verified": False,
        "note": "Allowlisting is not OAuth consent. Gmail/Drive use remains disabled until secure OAuth token storage and live API verification are implemented.",
    }


@router.get("/owner-admin/social-platforms")
def supreme_owner_admin_social_platforms():
    """Return private social platform registry and safe connection readiness."""
    return social_platform_status()


@router.get("/owner-admin/business-coach-profile")
def supreme_owner_admin_business_coach_profile():
    """Return the registered global business coaching contact profile."""
    return {
        "success": True,
        "privacy": "OWNER_ONLY",
        "profile": SupremeOwnerAdminService().global_business_coach_profile(),
    }


@router.get("/owner-admin/governance")
def supreme_owner_admin_governance():
    """Return owner governance rules and safe integration readiness metadata."""
    return SupremeOwnerAdminService().governance()


@router.get("/business/status")
def supreme_business_status():
    return business_ecosystem_status()


@router.get("/ai/status")
def supreme_ai_status():
    return ai_ecosystem_status()


@router.post("/auth/signup", status_code=201)
def signup(payload: SignupRequest):
    try:
        user = user_service.create_user(
            full_name=payload.full_name,
            email=str(payload.email),
            password=payload.password,
            role="USER",
            status="ACTIVE",
        )
        user_service.save_user(user)
        return {
            "success": True,
            "message": "Account created. Sign in to start a private session.",
            "account": user.to_dict(),
        }
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/auth/signin")
def signin(payload: SigninRequest):
    result = authentication_service.login(
        username=payload.username,
        password=payload.password,
    )
    if isinstance(result, dict):
        raise HTTPException(
            status_code=401,
            detail=result.get("message", "INVALID_USERNAME_OR_PASSWORD"),
        )
    if not result.authenticated:
        raise HTTPException(status_code=401, detail="INVALID_USERNAME_OR_PASSWORD")
    return {"success": True, **result.to_dict()}


@router.get("/account")
def account(authorization: str | None = Header(default=None)):
    username, user = _current_user(authorization)
    return {
        "success": True,
        "account": user.to_dict(),
        "is_supreme_owner": username.casefold() == SUPREME_OWNER_USERNAME.casefold(),
    }


@router.get("/dashboard")
def dashboard(authorization: str | None = Header(default=None)):
    username, user = _current_user(authorization)
    return {
        "success": True,
        "dashboard": "SUPREME ECOSYSTEM",
        "account": {
            "user_id": user.user_id,
            "username": user.username,
            "full_name": user.full_name,
            "role": user.role,
        },
        "is_supreme_owner": username.casefold() == SUPREME_OWNER_USERNAME.casefold(),
        "features": [
            "ACCOUNT",
            "PROFILE",
            "PRIVATE_MESSAGES",
            "AUTHORIZED_INTEGRATIONS",
        ],
    }


@router.get("/partner-programs")
def supreme_partner_programs():
    """Return configured partner/referral links to the authenticated SUPREME owner."""
    programs = get_partner_program_catalog()
    return {
        "success": True,
        "privacy": "OWNER_ONLY",
        "count": len(programs),
        "programs": programs,
        "note": "Configured referral URLs are not proof of live link validity or completed purchases. Confirm active codes and commissions in the provider dashboard.",
    }


@router.get("/integrations")
def integration_status():
    google_configured = all(
        os.getenv(name, "").strip()
        for name in ("GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET", "GOOGLE_REDIRECT_URI")
    )
    microsoft_configured = all(
        os.getenv(name, "").strip()
        for name in ("MICROSOFT_CLIENT_ID", "MICROSOFT_CLIENT_SECRET", "MICROSOFT_REDIRECT_URI")
    )
    whatsapp_configured = all(
        os.getenv(name, "").strip()
        for name in (
            "WHATSAPP_ACCESS_TOKEN",
            "WHATSAPP_PHONE_NUMBER_ID",
            "WHATSAPP_APP_SECRET",
            "WHATSAPP_VERIFY_TOKEN",
            "WHATSAPP_GRAPH_API_VERSION",
            "WHATSAPP_OUTREACH_TEMPLATE_NAME",
            "OPENAI_API_KEY",
        )
    )

    return {
        "success": True,
        "privacy": "PRIVATE_BY_DEFAULT",
        "integrations": [
            {
                "provider": "GOOGLE_WORKSPACE_AND_GOOGLE_SERVICES",
                "status": "CONFIGURED_NEEDS_OAUTH_FLOW" if google_configured else "NOT_CONFIGURED",
                "connected": False,
                "capabilities": [
                    "GOOGLE_SIGN_IN_OIDC",
                    "GMAIL",
                    "GOOGLE_DRIVE",
                    "GOOGLE_CALENDAR",
                    "GOOGLE_CONTACTS",
                    "GOOGLE_SHEETS",
                    "GOOGLE_DOCS",
                    "GOOGLE_FORMS",
                    "GOOGLE_MEET",
                    "GOOGLE_MAPS",
                    "YOUTUBE",
                    "GOOGLE_CLOUD",
                    "GOOGLE_ANALYTICS",
                    "GOOGLE_SEARCH_CONSOLE",
                    "GOOGLE_ADS",
                ],
                "authorization_policy": "EXPLICIT_USER_CONSENT_AND_LEAST_PRIVILEGE",
            },
            {
                "provider": "MICROSOFT_GRAPH",
                "status": "CONFIGURED_NEEDS_OAUTH_FLOW" if microsoft_configured else "NOT_CONFIGURED",
                "connected": False,
            },
            {
                "provider": "WHATSAPP_BUSINESS_AI",
                "status": "CONFIGURED_NEEDS_META_WEBHOOK_AND_END_TO_END_TEST" if whatsapp_configured else "NOT_CONFIGURED",
                "connected": False,
            },
        ],
        "note": "Environment variables alone do not establish a live provider connection.",
    }


@router.get("/capabilities")
def ecosystem_capabilities():
    """Expose the same shared backend capability catalog from SUPREME ECOSYSTEM."""
    catalog = get_capability_catalog()
    return {
        **catalog,
        "dashboard": "SUPREME ECOSYSTEM",
        "parent": "SUPREME",
        "access": "SUPREME_OWNER",
    }

class EcosystemControlCommandRequest(BaseModel):
    command: str = Field(min_length=1, max_length=80)
    payload: dict = Field(default_factory=dict)


@router.get("/control/status")
def ecosystem_control_status():
    """Expose the shared SUPREME owner-control status inside the ecosystem."""
    control = SupremeControlService.get_status(SupremeController())
    business = business_ecosystem_status()
    ai = ai_ecosystem_status()
    return {
        "success": control.get("status") == "READY",
        "control_plane": "SUPREME ECOSYSTEM",
        "parent_control_plane": "SUPREME",
        "status": control,
        "ecosystem_modules": {
            "business": business,
            "ai": ai,
        },
    }


@router.post("/control/commands")
def ecosystem_control_command(
    request: EcosystemControlCommandRequest,
    x_supreme_control_token: str | None = Header(default=None, alias="X-Supreme-Control-Token"),
):
    """Run the same safe allowlisted control commands from SUPREME ECOSYSTEM."""
    if SupremeControlService._configured_token() and not SupremeControlService.validate_token(
        x_supreme_control_token
    ):
        raise HTTPException(status_code=401, detail="SUPREME_CONTROL_TOKEN_REQUIRED")
    try:
        result = SupremeControlService.execute_command(
            SupremeController(), request.command, request.payload
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return {
        "success": True,
        "control_plane": "SUPREME ECOSYSTEM",
        "parent_control_plane": "SUPREME",
        "result": result,
    }
