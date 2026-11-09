"""Email infrastructure API for SUPREMESETUHUB."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from backend.infrastructure.email.controller import EmailController
from backend.infrastructure.email.model import EmailAccountInfo
from backend.infrastructure.email.providers import (
    email_provider_registry,
)


router = APIRouter(
    prefix="/api/v1/email",
    tags=["Email Infrastructure"],
)


email_controller = EmailController()


# ============================================================
# REQUEST MODELS
# ============================================================


class EmailAccountCreateRequest(BaseModel):
    """Request model for creating a SUPREMESETU MAIL account."""

    account_id: str = Field(min_length=1)
    user_id: str = Field(min_length=1)
    email_address: str = Field(min_length=3)
    username: str = Field(min_length=1)
    domain: str = ""
    provider: str = "SUPREMESETU"
    account_type: str = "MAILBOX"
    status: str = "PLANNED"


class EmailAccountStatusRequest(BaseModel):
    """Request model for updating account status."""

    status: str = Field(min_length=1)


# ============================================================
# EMAIL INFRASTRUCTURE STATUS
# ============================================================


@router.get("/status")
def email_status():
    """Return email infrastructure status."""

    accounts = email_controller.list_accounts()
    providers = email_provider_registry.list_all()

    return {
        "success": True,
        "system": "SUPREMESETU MAIL",
        "status": "active",
        "accounts": len(accounts),
        "providers": len(providers),
    }


# ============================================================
# EMAIL PROVIDERS
# ============================================================


@router.get("/providers")
def list_email_providers():
    """Return registered email providers."""

    return {
        "success": True,
        "providers": email_provider_registry.public_list(),
    }


@router.get("/providers/{provider_id}")
def get_email_provider(
    provider_id: str,
):
    """Return a registered email provider."""

    provider = email_provider_registry.get(
        provider_id
    )

    if not provider:
        raise HTTPException(
            status_code=404,
            detail="EMAIL_PROVIDER_NOT_FOUND",
        )

    return {
        "success": True,
        "provider": provider.to_dict(),
    }


# ============================================================
# SUPREMESETU MAIL ACCOUNTS
# ============================================================


@router.post("/accounts")
def create_email_account(
    payload: EmailAccountCreateRequest,
):
    """Create a SUPREMESETU MAIL account."""

    existing = email_controller.get_account_by_email(
        payload.email_address
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="EMAIL_ACCOUNT_ALREADY_EXISTS",
        )

    account = EmailAccountInfo(
        account_id=payload.account_id,
        user_id=payload.user_id,
        email_address=payload.email_address,
        username=payload.username,
        domain=payload.domain,
        provider=payload.provider,
        account_type=payload.account_type,
        status=payload.status,
    )

    try:
        result = email_controller.create_account(
            account
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail={
                "error": "EMAIL_ACCOUNT_CREATION_FAILED",
                "message": str(exc),
            },
        ) from exc

    return {
        "success": True,
        "account": result,
    }


@router.get("/accounts")
def list_email_accounts(
    user_id: str | None = None,
):
    """List SUPREMESETU MAIL accounts."""

    return {
        "success": True,
        "accounts": email_controller.list_accounts(
            user_id=user_id
        ),
    }


@router.get("/accounts/{account_id}")
def get_email_account(
    account_id: str,
):
    """Get a SUPREMESETU MAIL account."""

    account = email_controller.get_account(
        account_id
    )

    if not account:
        raise HTTPException(
            status_code=404,
            detail="EMAIL_ACCOUNT_NOT_FOUND",
        )

    return {
        "success": True,
        "account": account,
    }


@router.post("/accounts/{account_id}/verify")
def verify_email_account(
    account_id: str,
):
    """Verify a SUPREMESETU MAIL account."""

    account = email_controller.verify_account(
        account_id
    )

    if not account:
        raise HTTPException(
            status_code=404,
            detail="EMAIL_ACCOUNT_NOT_FOUND",
        )

    return {
        "success": True,
        "account": account,
    }


@router.patch("/accounts/{account_id}/status")
def update_email_account_status(
    account_id: str,
    payload: EmailAccountStatusRequest,
):
    """Update a SUPREMESETU MAIL account status."""

    account = email_controller.update_account_status(
        account_id,
        payload.status,
    )

    if not account:
        raise HTTPException(
            status_code=404,
            detail="EMAIL_ACCOUNT_NOT_FOUND",
        )

    return {
        "success": True,
        "account": account,
    }


@router.delete("/accounts/{account_id}")
def delete_email_account(
    account_id: str,
):
    """Delete a SUPREMESETU MAIL account."""

    deleted = email_controller.delete_account(
        account_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="EMAIL_ACCOUNT_NOT_FOUND",
        )

    return {
        "success": True,
        "deleted": True,
        "account_id": account_id,
    }
