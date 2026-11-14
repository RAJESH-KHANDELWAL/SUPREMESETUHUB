from pathlib import Path

import pytest

from backend.database.gde_connection import SupremeDatabaseConfig
from backend.database.migration_manager import DatabaseMigrationManager
from backend.database.restore_manager import DatabaseRestoreManager
from backend.infrastructure.ftp.deployer import FtpDeploymentManager


def central_config():
    return SupremeDatabaseConfig(
        host="db.example.invalid",
        database="supremesetuhub_test",
        username="supreme_test",
        password="not-a-real-password",
    )


@pytest.mark.parametrize(
    "value",
    ["../wp-config.php", "/public_html", "supremesetuhub/../../wordpress", r"..\secret"],
)
def test_ftp_deployer_rejects_path_traversal(value):
    with pytest.raises(ValueError):
        FtpDeploymentManager._safe_relative_path(value)


def test_ftp_deployer_accepts_site_relative_path():
    assert FtpDeploymentManager._safe_relative_path("supremesetuhub/assets") == "supremesetuhub/assets"


def test_migration_statement_parser_ignores_comment_lines():
    sql = """
    -- migration heading
    CREATE TABLE sample (id INT PRIMARY KEY);
    INSERT INTO sample (id) VALUES (1);
    """
    assert DatabaseMigrationManager._statements(sql) == [
        "CREATE TABLE sample (id INT PRIMARY KEY)",
        "INSERT INTO sample (id) VALUES (1)",
    ]


def test_migration_dry_run_never_connects(tmp_path: Path):
    (tmp_path / "001_create_sample.sql").write_text(
        "CREATE TABLE sample (id INT);", encoding="utf-8"
    )
    manager = DatabaseMigrationManager(central_config(), tmp_path)
    result = manager.apply_pending(dry_run=True)
    assert result["success"] is True
    assert result["dry_run"] is True
    assert result["pending"] == ["001_create_sample.sql"]
    assert result["applied"] == []


def test_restore_requires_exact_confirmation_before_any_client_access(tmp_path: Path):
    manager = DatabaseRestoreManager(
        central_config(), tmp_path, executable="client-that-does-not-exist"
    )
    with pytest.raises(PermissionError):
        manager.restore_backup("backup.sql", confirmation="yes")
