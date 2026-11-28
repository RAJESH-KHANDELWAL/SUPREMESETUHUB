# GOOGLE DRIVE STORAGE ECOSYSTEM

Storage-domain catalog for Google Drive files, folders, shared drives, and file lifecycle metadata.

## Scope
- My Drive files and folders
- Shared drives and membership-related storage metadata
- File identity, MIME type, size, checksums, and parent relationships
- Revisions, trash, and lifecycle metadata
- Shortcuts, sync, and offline-availability metadata where applicable

## Ownership boundary
This package owns storage taxonomy and metadata. Drive API clients, OAuth, permissions changes, uploads, downloads, exports, and deletes belong in the Google API/integration layer.

## Safety and readiness
This scaffold does not connect a Drive account or prove upload/download capability. Respect file-level permissions and shared-drive policies. Never commit credentials or user files.
