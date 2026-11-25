from __future__ import annotations

import pytest

from backend.database.service import DatabaseService
from backend.tenancy.service import TenantService, TenantValidationError


def _add_user(database: DatabaseService, user_id: str) -> None:
    database.execute(
        """
        INSERT INTO users (user_id, full_name, username, email, role, status)
        VALUES (?, ?, ?, ?, 'USER', 'ACTIVE')
        """,
        (user_id, user_id, user_id.lower(), f"{user_id.lower()}@example.test"),
    )


def test_two_sites_have_independent_gate_policies_and_memberships(tmp_path):
    database = DatabaseService(db_path=str(tmp_path / "central.sqlite3"))
    database.initialize()
    _add_user(database, "USR-OWNER")
    _add_user(database, "USR-MEMBER")
    service = TenantService(database=database)

    tenant = service.create_tenant(
        tenant_name="Example Business",
        owner_user_id="USR-OWNER",
        site_bindings=[
            {"site_id": "rajeshkhandelwalofficial", "gate_count": 4},
            {"site_id": "drrajeshkhandelwalibc", "gate_count": 2},
        ],
    )

    primary_owner = service.get_membership(
        tenant["tenant_id"], "rajeshkhandelwalofficial", "USR-OWNER"
    )
    ibc_owner = service.get_membership(
        tenant["tenant_id"], "drrajeshkhandelwalibc", "USR-OWNER"
    )
    assert primary_owner["gate_level"] == 4
    assert ibc_owner["gate_level"] == 2

    service.add_member(
        tenant["tenant_id"], "rajeshkhandelwalofficial", "USR-MEMBER", 2
    )
    assert service.get_membership(
        tenant["tenant_id"], "drrajeshkhandelwalibc", "USR-MEMBER"
    ) is None


def test_members_only_read_records_at_or_below_their_gate(tmp_path):
    database = DatabaseService(db_path=str(tmp_path / "central.sqlite3"))
    database.initialize()
    _add_user(database, "USR-OWNER")
    _add_user(database, "USR-MEMBER")
    service = TenantService(database=database)

    tenant = service.create_tenant(
        tenant_name="Gate Test",
        owner_user_id="USR-OWNER",
        site_bindings=[{"site_id": "rajeshkhandelwalofficial", "gate_count": 4}],
    )
    tenant_id = tenant["tenant_id"]
    service.add_member(tenant_id, "rajeshkhandelwalofficial", "USR-MEMBER", 2)

    for gate in (1, 2, 3):
        service.create_record(
            tenant_id=tenant_id,
            site_id="rajeshkhandelwalofficial",
            domain_key="business",
            record_type="profile",
            min_gate=gate,
            payload={"gate": gate},
            created_by="USR-OWNER",
        )

    visible = service.list_records(
        tenant_id, "rajeshkhandelwalofficial", gate_level=2
    )
    assert [item["min_gate"] for item in visible] == [2, 1]


def test_gate_level_cannot_exceed_site_gate_count(tmp_path):
    database = DatabaseService(db_path=str(tmp_path / "central.sqlite3"))
    database.initialize()
    _add_user(database, "USR-OWNER")
    _add_user(database, "USR-MEMBER")
    service = TenantService(database=database)
    tenant = service.create_tenant(
        tenant_name="Two Gate Site",
        owner_user_id="USR-OWNER",
        site_bindings=[{"site_id": "drrajeshkhandelwalibc", "gate_count": 2}],
    )

    with pytest.raises(TenantValidationError, match="MEMBER_GATE_LEVEL_EXCEEDS_SITE_GATE_COUNT"):
        service.add_member(
            tenant["tenant_id"], "drrajeshkhandelwalibc", "USR-MEMBER", 3
        )
