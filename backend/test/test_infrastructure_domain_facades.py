"""Tests for the canonical Database and FTP Infrastructure domain facades."""
from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.database import (
    DatabaseInfrastructureController,
    DatabaseInfrastructureService,
)
from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.ftp import (
    FtpInfrastructureController,
    FtpInfrastructureService,
)
from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.ftp.model import (
    FtpProfile,
    FtpTarget,
)
from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.manager import (
    get_manager,
)


def test_all_21_domains_meet_their_declared_file_contracts():
    report = get_manager().health()
    assert report["healthy"], report
    assert report["present_domain_count"] == 21
    assert all(
        all(file_checks.values())
        for file_checks in report["domain_file_checks"].values()
    )


def test_database_facade_uses_read_only_service_without_creating_database():
    controller = DatabaseInfrastructureController()
    result = controller.check_all(check_mysql=False)
    assert result["service"] == "DatabaseInfrastructureService"
    assert result["mutations_performed"] is False
    assert result["checks"]["central_mysql"]["status"] == "NOT_CHECKED"


def test_database_controller_delegates_to_injected_service():
    class FakeService:
        def check_all(self, *, check_mysql=False):
            return {"success": True, "check_mysql": check_mysql}

        def check_sqlite_runtime(self):
            return {"status": "HEALTHY"}

        def check_central_mysql(self):
            return {"status": "HEALTHY"}

    controller = DatabaseInfrastructureController(FakeService())
    assert controller.check_all(check_mysql=True) == {"success": True, "check_mysql": True}
    assert controller.check_sqlite_runtime()["status"] == "HEALTHY"
    assert controller.check_central_mysql()["status"] == "HEALTHY"


def test_ftp_facade_exposes_profile_model_and_read_only_service():
    assert FtpProfile is not None
    assert FtpTarget is not None
    controller = FtpInfrastructureController(FtpInfrastructureService(environ={}))
    profiles = controller.list_profiles()
    assert profiles
    assert all("password" not in item and "username" not in item for item in profiles)


def test_ftp_controller_delegates_profile_checks():
    class FakeService:
        def list_profiles(self):
            return [{"profile_id": "test", "configured": False}]

        def check_profile(self, profile_id):
            return {"profile_id": profile_id, "mutations_performed": False}

    controller = FtpInfrastructureController(FakeService())
    assert controller.list_profiles()[0]["profile_id"] == "test"
    assert controller.check_profile("test")["mutations_performed"] is False
