from backend.database.service import DatabaseService
from backend.roles.service import RoleService


def test_role_service_persists_and_updates_role(tmp_path):
    service = RoleService(DatabaseService(str(tmp_path / "supreme-test.db")))
    service.initialize()

    role = service.create_role(
        role_id="ROLE-001",
        role_name="Administrator",
        description="Platform administration",
        organization_id="ORG-001",
        holder_id="USER-001",
        role_category="ADMIN",
        authority_level=9,
        scope="PLATFORM",
        appointment_type="ASSIGNED",
    )
    service.save_role(role)

    fetched = service.get_role("ROLE-001")
    assert fetched is not None
    assert fetched.role_name == "Administrator"
    assert fetched.organization_id == "ORG-001"
    assert fetched.authority_level == 9

    updated = service.update_role("ROLE-001", role_name="Platform Admin", status="SUSPENDED")
    assert updated["success"] is True
    assert service.get_role("ROLE-001").role_name == "Platform Admin"
    assert service.get_role("ROLE-001").status == "SUSPENDED"

    roles = service.get_all_roles()
    assert [item.role_id for item in roles] == ["ROLE-001"]

    deleted = service.delete_role("ROLE-001")
    assert deleted["success"] is True
    assert service.get_role("ROLE-001") is None


def test_role_service_initialize_preserves_legacy_roles(tmp_path):
    import sqlite3

    path = tmp_path / "legacy.db"
    with sqlite3.connect(path) as connection:
        connection.execute(
            """
            CREATE TABLE roles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role_id TEXT UNIQUE NOT NULL,
                role_name TEXT UNIQUE NOT NULL,
                description TEXT,
                level INTEGER DEFAULT 1,
                status TEXT DEFAULT 'ACTIVE',
                created_at TEXT,
                updated_at TEXT
            )
            """
        )
        connection.execute(
            "INSERT INTO roles (role_id, role_name, description, level, status) VALUES (?, ?, ?, ?, ?)",
            ("ROLE-OLD", "Legacy Admin", "Keep this record", 7, "ACTIVE"),
        )

    service = RoleService(DatabaseService(str(path)))
    service.initialize()

    legacy = service.get_role("ROLE-OLD")
    assert legacy is not None
    assert legacy.role_name == "Legacy Admin"
    assert legacy.description == "Keep this record"
    assert legacy.authority_level == 7
    assert legacy.organization_id == ""
