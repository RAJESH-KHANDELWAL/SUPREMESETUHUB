from __future__ import annotations

from types import SimpleNamespace


def test_create_business_uses_unique_server_generated_ids(monkeypatch):
    from backend.api import businesses as businesses_module

    ids = iter(
        [
            SimpleNamespace(hex="a" * 32),
            SimpleNamespace(hex="b" * 32),
        ]
    )
    monkeypatch.setattr(businesses_module, "uuid4", lambda: next(ids))
    monkeypatch.setattr(businesses_module.controller, "list", lambda: [])
    monkeypatch.setattr(
        businesses_module.controller,
        "create",
        lambda **kwargs: SimpleNamespace(to_dict=lambda: dict(kwargs)),
    )

    user = {"user_id": "user-123", "role": "USER"}
    first = businesses_module.create_business(
        businesses_module.BusinessCreateRequest(name="First business"),
        current_user=user,
    )
    second = businesses_module.create_business(
        businesses_module.BusinessCreateRequest(name="Second business"),
        current_user=user,
    )

    first_id = first["data"]["business_id"]
    second_id = second["data"]["business_id"]

    assert first_id == f"BUS-{'A' * 32}"
    assert second_id == f"BUS-{'B' * 32}"
    assert first_id != second_id
