from __future__ import annotations

from io import BytesIO

import pytest

from backend.gallary_woult.object_store import GalleryWoultObjectStore, UploadTooLargeError


def test_object_store_saves_and_reads_file(tmp_path, monkeypatch):
    monkeypatch.delenv("RENDER", raising=False)
    monkeypatch.delenv("RENDER_SERVICE_ID", raising=False)
    store = GalleryWoultObjectStore(root=str(tmp_path / "objects"), max_upload_bytes=16)
    key = store.make_storage_key("user-1", "file-1", "hello.txt")
    size, digest = store.save_stream(BytesIO(b"hello"), key)
    assert size == 5
    assert len(digest) == 64
    with store.open(key) as handle:
        assert handle.read() == b"hello"


def test_object_store_rejects_oversized_upload_without_partial_file(tmp_path, monkeypatch):
    monkeypatch.delenv("RENDER", raising=False)
    monkeypatch.delenv("RENDER_SERVICE_ID", raising=False)
    store = GalleryWoultObjectStore(root=str(tmp_path / "objects"), max_upload_bytes=4)
    key = store.make_storage_key("user-1", "file-2", "large.bin")
    with pytest.raises(UploadTooLargeError):
        store.save_stream(BytesIO(b"12345"), key)
    assert store.exists(key) is False
    assert list((tmp_path / "objects").rglob("*.tmp")) == []


def test_hosted_storage_fails_closed_without_persistence_ack(tmp_path, monkeypatch):
    monkeypatch.setenv("RENDER", "true")
    monkeypatch.delenv("RENDER_SERVICE_ID", raising=False)
    monkeypatch.delenv("GALLERY_WOULT_STORAGE_ROOT", raising=False)
    monkeypatch.delenv("SUPREME_FILE_STORAGE_DIR", raising=False)
    monkeypatch.delenv("GALLERY_WOULT_STORAGE_DURABILITY_ACKNOWLEDGED", raising=False)
    monkeypatch.delenv("SUPREME_FILE_STORAGE_DURABILITY_ACKNOWLEDGED", raising=False)
    store = GalleryWoultObjectStore(root=None)
    assert store.status()["status"] == "PERSISTENCE_NOT_VERIFIED"
    with pytest.raises(RuntimeError, match="PERSISTENT_STORAGE_NOT_CONFIGURED_OR_VERIFIED"):
        store.save_stream(BytesIO(b"hello"), "user/file/name.txt")


def test_hosted_storage_requires_explicit_root_and_ack(tmp_path, monkeypatch):
    monkeypatch.setenv("RENDER", "true")
    monkeypatch.setenv("GALLERY_WOULT_STORAGE_ROOT", str(tmp_path / "persistent"))
    monkeypatch.setenv("GALLERY_WOULT_STORAGE_DURABILITY_ACKNOWLEDGED", "true")
    store = GalleryWoultObjectStore(root=None)
    assert store.status()["status"] == "CONFIGURED_OPERATOR_ACKNOWLEDGED"
    assert store.status()["writable"] is True


def test_gallery_woult_uses_central_database_service_and_reopens_data(tmp_path, monkeypatch):
    monkeypatch.delenv("RENDER", raising=False)
    monkeypatch.delenv("RENDER_SERVICE_ID", raising=False)
    database_path = tmp_path / "central" / "supreme.db"
    storage_root = tmp_path / "durable-files"
    monkeypatch.setenv("SUPREME_DB_PATH", str(database_path))
    monkeypatch.setenv("GALLERY_WOULT_STORAGE_ROOT", str(storage_root))

    from backend.gallary_woult.service import GalleryWoultService

    first = GalleryWoultService(db_path=str(database_path), storage_root=str(storage_root))
    folder = first.create_folder("canonical-user-1", "Documents")
    uploaded = first.save_bytes(
        actor_id="canonical-user-1",
        filename="note.txt",
        data=b"central database + separate object bytes",
        parent_id=folder["object_id"],
    )
    assert first.database.db_path == str(database_path)

    second = GalleryWoultService(db_path=str(database_path), storage_root=str(storage_root))
    recovered = second.get(uploaded["object_id"], "canonical-user-1")
    assert recovered["name"] == "note.txt"
    assert second.get_download_path(uploaded["object_id"], "canonical-user-1").read_bytes() == b"central database + separate object bytes"
