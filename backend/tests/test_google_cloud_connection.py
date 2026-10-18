from types import SimpleNamespace

from backend.google.google_ecosystem.cloud.connection import check_cloud_connection


def test_cloud_connection_reports_missing_credentials(monkeypatch):
    import google.auth

    def no_credentials(*args, **kwargs):
        raise google.auth.exceptions.DefaultCredentialsError("no credentials")

    monkeypatch.setattr(google.auth, "default", no_credentials)
    result = check_cloud_connection()
    assert result["status"] == "AUTHENTICATION_NOT_CONFIGURED"
    assert result["connected"] is False


def test_cloud_connection_reports_project_not_configured(monkeypatch):
    import google.auth

    monkeypatch.delenv("GOOGLE_CLOUD_PROJECT", raising=False)
    monkeypatch.setattr(google.auth, "default", lambda **kwargs: (object(), None))
    result = check_cloud_connection()
    assert result["status"] == "PROJECT_NOT_CONFIGURED"
    assert result["connected"] is False


def test_cloud_connection_reports_read_only_success(monkeypatch):
    import google.auth
    import google.auth.transport.requests

    monkeypatch.setenv("GOOGLE_CLOUD_PROJECT", "demo-project")
    monkeypatch.setattr(google.auth, "default", lambda **kwargs: (object(), None))

    class FakeSession:
        def __init__(self, credentials):
            pass

        def get(self, url, timeout):
            assert url.endswith("/demo-project")
            assert timeout == 10
            return SimpleNamespace(status_code=200, json=lambda: {"state": "ACTIVE"})

    monkeypatch.setattr(
        google.auth.transport.requests,
        "AuthorizedSession",
        FakeSession,
    )
    result = check_cloud_connection()
    assert result["status"] == "CONNECTED_READ_ONLY"
    assert result["connected"] is True
    assert result["project_state"] == "ACTIVE"


def test_cloud_connection_does_not_claim_success_on_permission_denied(monkeypatch):
    import google.auth
    import google.auth.transport.requests

    monkeypatch.setenv("GOOGLE_CLOUD_PROJECT", "demo-project")
    monkeypatch.setattr(google.auth, "default", lambda **kwargs: (object(), None))

    class FakeSession:
        def __init__(self, credentials):
            pass

        def get(self, url, timeout):
            return SimpleNamespace(status_code=403)

    monkeypatch.setattr(
        google.auth.transport.requests,
        "AuthorizedSession",
        FakeSession,
    )
    result = check_cloud_connection()
    assert result["status"] == "PERMISSION_DENIED"
    assert result["connected"] is False
