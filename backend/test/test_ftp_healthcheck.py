from __future__ import annotations

import ftplib

import pytest

from backend.infrastructure.ftp.healthcheck import FtpTarget, check_ftp_connection


def test_target_requires_all_credentials_without_echoing_password() -> None:
    with pytest.raises(ValueError, match="FTP_PASSWORD"):
        FtpTarget.from_environment({"FTP_SERVER": "ftp.example.com", "FTP_USERNAME": "user"})


def test_target_rejects_invalid_port() -> None:
    with pytest.raises(ValueError, match="FTP_PORT"):
        FtpTarget.from_environment({
            "FTP_SERVER": "ftp.example.com", "FTP_USERNAME": "user",
            "FTP_PASSWORD": "secret", "FTP_PORT": "70000",
        })


def test_target_password_is_not_in_repr() -> None:
    target = FtpTarget.from_environment({
        "FTP_SERVER": "ftp.example.com", "FTP_USERNAME": "user",
        "FTP_PASSWORD": "do-not-print-this",
    })
    assert "do-not-print-this" not in repr(target)


def test_530_is_reported_as_authentication_failure(monkeypatch: pytest.MonkeyPatch) -> None:
    class FakeFTP_TLS:
        def __init__(self, **kwargs): pass
        def connect(self, *args, **kwargs): pass
        def auth(self): pass
        def login(self, **kwargs): raise ftplib.error_perm("530 Login incorrect.")
        def prot_p(self): pass
        def quit(self): pass
        def close(self): pass

    monkeypatch.setattr(ftplib, "FTP_TLS", FakeFTP_TLS)
    target = FtpTarget("ftp.example.com", "user", "private", site="ibc")
    result = check_ftp_connection(target)
    assert result["status"] == "AUTHENTICATION_FAILED"
    assert result["success"] is False
    assert result["credentials_returned"] is False
    assert "private" not in repr(result)


def test_successful_check_only_reads_current_directory(monkeypatch: pytest.MonkeyPatch) -> None:
    class FakeFTP_TLS:
        def __init__(self, **kwargs): pass
        def connect(self, *args, **kwargs): pass
        def auth(self): pass
        def login(self, **kwargs): pass
        def prot_p(self): pass
        def pwd(self): return "/public_html"
        def quit(self): pass
        def close(self): pass

    monkeypatch.setattr(ftplib, "FTP_TLS", FakeFTP_TLS)
    target = FtpTarget("ftp.example.com", "user", "private", site="ibc")
    result = check_ftp_connection(target)
    assert result["status"] == "CONNECTED"
    assert result["remote_directory"] == "/public_html"
    assert result["mutations_performed"] is False
