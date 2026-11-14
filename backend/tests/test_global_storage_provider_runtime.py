from __future__ import annotations

from io import BytesIO


def test_local_provider_runtime_round_trip(tmp_path, monkeypatch):
    monkeypatch.setenv("SUPREME_FILE_STORAGE_DIR", str(tmp_path / "objects"))
    monkeypatch.setenv("SUPREME_STORAGE_PROVIDER", "local")

    from backend.storage.global_ecosystem.global_storage_ecosystem.provider_runtime import StorageProviderRuntime

    runtime = StorageProviderRuntime()
    status = runtime.status()
    assert status["provider_id"] == "local"
    assert status["write_verified"] is True

    saved = runtime.store_stream(
        BytesIO(b"global storage runtime"),
        owner_id="USR_1", area_id="documents",
        filename="sample.txt", max_bytes=1024,
    )
    assert saved["storage_backend"] == "LOCAL_FILESYSTEM"
    assert saved["size_bytes"] == len(b"global storage runtime")
    assert runtime.exists_key(saved["storage_key"]) is True

    with runtime.open_key(saved["storage_key"]) as stream:
        assert stream.read() == b"global storage runtime"

    assert runtime.delete_key(saved["storage_key"]) is True
    assert runtime.exists_key(saved["storage_key"]) is False


def test_provider_runtime_rejects_unknown_provider():
    from backend.storage.global_ecosystem.global_storage_ecosystem.provider_runtime import StorageProviderRuntime

    try:
        StorageProviderRuntime("unknown-provider")
    except ValueError as exc:
        assert str(exc) == "UNSUPPORTED_STORAGE_PROVIDER"
    else:
        raise AssertionError("unknown provider was accepted")


def test_provider_runtime_reports_s3_unconfigured_without_bucket(monkeypatch):
    monkeypatch.delenv("AWS_S3_BUCKET", raising=False)
    from backend.storage.global_ecosystem.global_storage_ecosystem.provider_runtime import StorageProviderRuntime

    status = StorageProviderRuntime("aws_s3").status()
    assert status["configured"] is False
    assert status["write_verified"] is False
    assert status["backend"] == "AWS_S3"
