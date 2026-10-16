import pytest

from backend.core.payments.payee_verification import (
    parse_upi_qr,
    precheck_payee_details,
)


def test_valid_upi_id_is_not_misrepresented_as_verified():
    result = precheck_payee_details("UPI_ID", upi_id="rajesh.khandelwal@bank")
    assert result["format_valid"] is True
    assert result["verification_status"] == "NOT_VERIFIED"
    assert result["verified"] is False
    assert result["account_holder_name"] is None


def test_invalid_upi_id_is_rejected():
    result = precheck_payee_details("UPI_ID", upi_id="not-an-upi-id")
    assert result["format_valid"] is False
    assert result["verification_status"] == "INVALID_FORMAT"
    assert result["verified"] is False


def test_valid_bank_format_does_not_claim_account_name_verified():
    result = precheck_payee_details(
        "BANK_ACCOUNT",
        account_number="123456789012",
        ifsc="HDFC0001234",
    )
    assert result["format_valid"] is True
    assert result["verification_status"] == "NOT_VERIFIED"
    assert result["account_holder_name"] is None
    assert result["verified"] is False
    assert result["masked_account_number"] == "********9012"


def test_invalid_ifsc_is_rejected():
    result = precheck_payee_details(
        "BANK_ACCOUNT",
        account_number="123456789012",
        ifsc="BAD",
    )
    assert result["format_valid"] is False
    assert result["ifsc_format_valid"] is False


def test_upi_qr_parses_payee_but_does_not_trust_embedded_name():
    result = parse_upi_qr(
        "upi://pay?pa=merchant@bank&pn=Example%20Merchant&am=125.00&cu=INR"
    )
    assert result["payee_upi_id"] == "merchant@bank"
    assert result["qr_payee_name"] == "Example Merchant"
    assert result["verification_status"] == "NOT_VERIFIED"
    assert result["verification_source"] == "QR_PAYLOAD_ONLY"


def test_unsupported_qr_payload_is_rejected():
    with pytest.raises(ValueError, match="UNSUPPORTED_QR_FORMAT"):
        parse_upi_qr("https://example.com/fake-qr")


def test_global_methods_fail_closed_when_provider_not_configured():
    from backend.api.payee_verification import PayeePrecheckRequest, precheck

    response = precheck(
        PayeePrecheckRequest(
            payment_method="IBAN",
            country_code="DE",
            payee_identifier="DE89370400440532013000",
        )
    )
    assert response["data"]["country_code"] == "DE"
    assert response["data"]["verification_status"] == "NOT_CONFIGURED"
    assert response["data"]["verified"] is False
    assert response["data"]["account_holder_name"] is None


def test_provider_registry_is_empty_until_authorized_adapter_is_configured():
    from backend.core.payments.provider_registry import configured_providers, find_provider

    assert configured_providers() == []
    assert find_provider(country_code="IN", payment_method="UPI_ID") is None
