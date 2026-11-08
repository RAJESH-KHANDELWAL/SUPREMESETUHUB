from __future__ import annotations

from backend.supreme.control import SupremeControlService


class ReadyController:
    def status(self):
        return {"initialized": True, "owner_exists": True}

    def exists(self):
        return True


class UnavailableController:
    def status(self):
        raise RuntimeError("database unavailable")


def test_supreme_control_reports_ready_controller():
    result = SupremeControlService.get_status(ReadyController())
    assert result["system"] == "SUPREME"
    assert result["status"] == "READY"
    assert result["owner_exists"] is True


def test_supreme_control_does_not_claim_unavailable_controller_is_healthy():
    result = SupremeControlService.get_status(UnavailableController())
    assert result["status"] == "DEGRADED"
    assert result["unavailable_reason"] == "SUPREME_CONTROLLER_UNAVAILABLE"


def test_supreme_control_only_runs_allowlisted_read_only_commands():
    assert SupremeControlService.execute_command(
        ReadyController(), "modules.list"
    )["status"] == "ok"
    try:
        SupremeControlService.execute_command(ReadyController(), "users.list")
    except ValueError as exc:
        assert "Unsupported command" in str(exc)
    else:
        raise AssertionError("Unsupported command was accepted")


def test_control_token_comparison_requires_configured_token(monkeypatch):
    monkeypatch.delenv("SUPREME_CONTROL_TOKEN", raising=False)
    assert SupremeControlService.validate_token("any-token") is False
    monkeypatch.setenv("SUPREME_CONTROL_TOKEN", "correct-token")
    assert SupremeControlService.validate_token("wrong-token") is False
    assert SupremeControlService.validate_token("correct-token") is True


def test_control_routes_are_registered_in_supreme_and_supreme_ecosystem():
    from backend.api.supreme import router as supreme_router
    from backend.api.supreme_ecosystem import router as ecosystem_router

    supreme_paths = {route.path for route in supreme_router.routes}
    ecosystem_paths = {route.path for route in ecosystem_router.routes}
    assert "/supreme/control/status" in supreme_paths
    assert "/supreme/control/commands" in supreme_paths
    assert "/api/v1/supreme-ecosystem/control/status" in ecosystem_paths
    assert "/api/v1/supreme-ecosystem/control/commands" in ecosystem_paths
