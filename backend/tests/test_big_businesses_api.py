import pytest
from fastapi import HTTPException

from backend.api import big_businesses
from backend.schemas.business import BusinessCreateRequest


def test_big_business_listing_excludes_small_and_medium_businesses(monkeypatch):
    records = [
        {"business_id": "B1", "business_type": "SMALL_BUSINESS"},
        {"business_id": "B2", "business_type": "MEDIUM_BUSINESS"},
        {"business_id": "B3", "business_type": "LARGE_BUSINESS"},
        {"business_id": "B4", "business_type": "ENTERPRISE"},
    ]
    monkeypatch.setattr(
        big_businesses.business_api,
        "get_businesses",
        lambda current_user: {"data": records},
    )

    result = big_businesses._big_business_records({"user_id": "owner-1"})
    assert [item["business_id"] for item in result] == ["B3", "B4"]


def test_big_business_creation_rejects_small_business_type():
    request = BusinessCreateRequest(name="Ordinary shop", business_type="SMALL_BUSINESS")
    with pytest.raises(HTTPException) as error:
        big_businesses.create_big_business(request, current_user={"user_id": "owner-1"})
    assert error.value.status_code == 422
    assert error.value.detail == "BIG_BUSINESS_TYPE_REQUIRED"


def test_big_business_creation_accepts_enterprise_type(monkeypatch):
    request = BusinessCreateRequest(name="Large company", business_type="ENTERPRISE")
    expected = {"message": "created"}
    monkeypatch.setattr(
        big_businesses.business_api,
        "create_business",
        lambda request, current_user: expected,
    )

    assert big_businesses.create_big_business(
        request, current_user={"user_id": "owner-1"}
    ) == expected
