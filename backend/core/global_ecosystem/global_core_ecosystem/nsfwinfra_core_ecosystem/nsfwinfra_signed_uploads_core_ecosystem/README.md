# SIGNED UPLOADS INFRA CORE ECOSYSTEM

Parent: NSF Winfra Core. Package `nsfwinfra_signed_uploads_core_ecosystem/`. ID: `NSFW-INFRA-SIGNED-UPLOADS-CORE`.

## Scope
Policy/contracts for upload authorization, signatures/expiry, file limits/validation, purpose, storage refs, chunks, integrity, retry, abuse and cleanup. Secrets, transport and storage writes external.

## Capability metadata
- `UPLOAD_CONTRACTS`
- `AUTHORIZATION_REQUIREMENTS`
- `SIGNATURE_METADATA`
- `EXPIRATION_POLICY`
- `SIZE_AND_TYPE_LIMITS`
- `MIME_AND_CONTENT_VALIDATION_POLICY`
- `UPLOAD_PURPOSE_METADATA`
- `STORAGE_DESTINATION_REFERENCES`
- `MULTIPART_AND_CHUNK_METADATA`
- `INTEGRITY_METADATA`
- `RETRY_POLICY`
- `ABUSE_PREVENTION`
- `CLEANUP_AND_RETENTION`
- `READINESS`

## Interface
- `manager.py`: status and capability metadata.
- `__init__.py`: public exports.

Metadata-only; no infrastructure execution, API calls, persistence or verified-live claim. Auth, secrets, transport, runtime and storage are separate layers.
