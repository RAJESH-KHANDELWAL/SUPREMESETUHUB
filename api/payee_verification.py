"""Private API for payee-detail prechecks.

Provider integration is intentionally fail-closed: these endpoints never mark
a payee verified until an authorized bank/payment provider is integrated.
"""
from __future__ import annotations

from typing import Literal

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from backend.core.payments.payee_verification import precheck_payee_details
from backend.core.payments.provider_registry import configured_providers, find_provider
from backend.security.dependencies import require_admin

router = APIRouter(
    prefix="/api/v1/payments/payee-verification",
    tags=["PAYEE VERIFICATION"],
    dependencies=[Depends(require_admin)],
)


class PayeePrecheckRequest(BaseModel):
    payment_method: Literal["UPI_ID", "UPI_QR", "BANK_ACCOUNT", "IBAN", "SWIFT_BIC", "LOCAL_BANK_ACCOUNT", "DIGITAL_WALLET", "LOCAL_PAYMENT_NETWORK"]
    country_code: str = Field(default="IN", min_length=2, max_length=2)
    network: str = Field(default="", max_length=80)
    payee_identifier: str = Field(default="", max_length=256)
    upi_id: str = Field(default="", max_length=256)
    qr_payload: str = Field(default="", max_length=4096)
    account_number: str = Field(default="", max_length=34)
    ifsc: str = Field(default="", max_length=11)


@router.get("/capabilities")
def capabilities() -> dict[str, object]:
    return {
        "success": True,
        "service": "SUPREMESETUHUB_PAYEE_VERIFICATION",
        "supported_prechecks": ["UPI_ID", "UPI_QR", "BANK_ACCOUNT"],
        "global_methods_planned": ["IBAN", "SWIFT_BIC", "LOCAL_BANK_ACCOUNT", "DIGITAL_WALLET", "LOCAL_PAYMENT_NETWORK"],
        "configured_providers": configured_providers(),
        "provider_name_verification": "NOT_CONFIGURED",
        "live_bank_credit_confirmation": "NOT_CONFIGURED",
        "green_verified_badge_enabled": False,
        "message": (
            "Input format and QR payload checks only. No account-holder name "
            "or bank ownership is confirmed until an authorized provider is integrated."
        ),
    }


@router.post("/precheck")
def precheck(request: PayeePrecheckRequest) -> dict[str, object]:
    country = request.country_code.upper()
    method = request.payment_method.upper()
    provider = find_provider(country_code=country, payment_method=method)
    if method not in {"UPI_ID", "UPI_QR", "BANK_ACCOUNT"}:
        if provider is None:
            return {
                "success": True,
                "data": {
                    "country_code": country,
                    "payment_method": method,
                    "network": request.network or None,
                    "verification_status": "NOT_CONFIGURED",
                    "verified": False,
                    "account_holder_name": None,
                    "verification_source": None,
                    "message": "No authorized verification provider is configured for this country and method yet.",
                    "next_step": "ONBOARD_AUTHORIZED_COUNTRY_NETWORK_PROVIDER",
                },
                "disclaimer": "No live ownership verification has occurred.",
            }
        # Adapter invocation will be added only with an audited provider-specific
        # request/response mapping; never guess a provider's API contract here.
        return {
            "success": True,
            "data": {
                "country_code": country,
                "payment_method": method,
                "verification_status": "PROVIDER_ADAPTER_PENDING",
                "verified": False,
                "account_holder_name": None,
                "provider_id": provider.provider_id,
                "message": "Provider is registered but its audited verification flow is not implemented.",
            },
        }
    try:
        result = precheck_payee_details(
            request.payment_method,
            upi_id=request.upi_id,
            qr_payload=request.qr_payload,
            account_number=request.account_number,
            ifsc=request.ifsc,
        )
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    return {
        "success": True,
        "data": result,
        "disclaimer": (
            "A valid format or QR payload is not proof of account ownership. "
            "Do not send money based on this precheck alone."
        ),
    }
