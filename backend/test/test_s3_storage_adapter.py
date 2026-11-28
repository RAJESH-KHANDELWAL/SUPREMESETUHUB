from __future__ import annotations

import hashlib
from io import BytesIO

import pytest

from backend.storage.s3 import S3ObjectStorage


class FakeS3:
    def __init__(self):
        self.objects = {}

    def head_bucket(self, **kwargs):
        return {}

    def put_object(self, *, Bucket, Key, Body, Metadata=None, ServerSideEncryption=None):
        raw_body = Body if isinstance(Body, bytes) else Body.read()
        self.objects[(Bucket, Key)] = {
            "body": raw_body,
            "metadata": dict(Metadata or {}),
            "encryption": ServerSideEncryption,
        }

    def get_object(self, *, Bucket, Key):
        from io import BytesIO
        item = self.objects[(Bucket, Key)]
        return {"Body": BytesIO(item["body"]), "Metadata": dict(item["metadata"])}

    def head_object(self, *, Bucket, Key):
        item = self.objects.get((Bucket, Key))
        if item is None:
            raise FakeClientError("404")
        return {"ContentLength": len(item["body"]), "Metadata": item["metadata"]}

    def copy_object(self, *, Bucket, Key, CopySource, MetadataDirective, ServerSideEncryption):
        source = self.objects[(CopySource["Bucket"], CopySource["Key"])]
        self.objects[(Bucket, Key)] = {
            "body": source["body"],
            "metadata": dict(source["metadata"]),
            "encryption": ServerSideEncryption,
        }

    def delete_object(self, *, Bucket, Key):
        self.objects.pop((Bucket, Key), None)


class FakeClientError(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.response = {"Error": {"Code": code}}


def test_s3_upload_download_checksum_and_server_side_encryption():
    client = FakeS3()
    storage = S3ObjectStorage(bucket="private-test-bucket", client=client)
    payload = b"SUPREME S3 storage test"
    size, checksum = storage.save_stream_at_key(BytesIO(payload), "gallary_woult/user-1/file-1/note.txt")
    assert size == len(payload)
    assert checksum == hashlib.sha256(payload).hexdigest()
    assert client.objects[("private-test-bucket", "gallary_woult/user-1/file-1/note.txt")]["encryption"] == "AES256"
    with storage.open_key("gallary_woult/user-1/file-1/note.txt") as handle:
        assert handle.read() == payload


def test_s3_upload_rejects_oversized_stream():
    storage = S3ObjectStorage(bucket="private-test-bucket", client=FakeS3())
    with pytest.raises(ValueError, match="MAX_UPLOAD_SIZE_EXCEEDED"):
        storage.save_stream_at_key(BytesIO(b"12345"), "u/f/large.bin", max_bytes=4)


def test_s3_copy_and_delete_preserve_object_bytes_and_checksum():
    client = FakeS3()
    storage = S3ObjectStorage(bucket="private-test-bucket", client=client)
    payload = b"copy integrity"
    _, checksum = storage.save_stream_at_key(BytesIO(payload), "u/f/source.bin")
    size, copied_checksum = storage.copy_key("u/f/source.bin", "u/f/copy.bin")
    assert size == len(payload)
    assert copied_checksum == checksum
    assert storage.exists_key("u/f/copy.bin") is True
    assert storage.delete_key("u/f/copy.bin") is True
    assert storage.exists_key("u/f/copy.bin") is False


@pytest.mark.parametrize("key", ["", "/absolute/file", "../escape", "u/../escape", "u//file"])
def test_s3_rejects_unsafe_keys(key):
    storage = S3ObjectStorage(bucket="private-test-bucket", client=FakeS3())
    with pytest.raises(ValueError, match="INVALID_STORAGE_KEY"):
        storage.save_stream_at_key(BytesIO(b"x"), key)


def test_s3_without_bucket_fails_closed():
    storage = S3ObjectStorage(bucket="", client=FakeS3())
    assert storage.health()["writable"] is False
