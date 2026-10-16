# SUPREMESETUHUB — Provider-Neutral Hosting and Storage Architecture

## Core rule

**GitHub is the source of truth for code, configuration templates, tests, release workflows, and deployment definitions.** It is not a runtime database or file store. Render is a temporary API/runtime target and must not be treated as permanent storage.

## Control plane and execution plane

- **SUPREME / SUPREME ECOSYSTEM:** owner control, identity, permissions, orchestration, and service health.
- **GitHub:** source repository, reviewed changes, CI, release artifacts, and deployment automation.
- **Runtime targets:** Render temporarily; future supported targets can include Hostinger-hosted web frontend, AWS runtime, Google Cloud services, or Microsoft-hosted services. Each target needs its own tested deployment adapter and environment configuration.
- **Database:** central MAIN BASE FOUNDATION database interface. Current implementation is SQLite; a shared managed database requires a real adapter and migration.
- **Storage:** central MAIN BASE FOUNDATION storage boundary. GALLARY WOULT owns folder/file metadata and workflows; storage adapters own bytes.

## Planned storage provider catalog

The provider catalog names intended targets without falsely marking them connected:

| Provider | Intended role | Current state |
|---|---|---|
| Local filesystem | Development or explicitly mounted persistent volume | Adapter exists |
| AWS S3 | Durable object storage and backups | Adapter not implemented |
| Google Drive | Owner-authorized Drive storage/sync | Adapter not implemented |
| Microsoft OneDrive / Graph | Owner-authorized Microsoft storage/sync | Adapter not implemented |
| MEGA | Optional cloud file synchronization | Adapter not implemented |
| Hostinger | Website/runtime hosting; storage depends on product/plan | Adapter not implemented |

A provider must not be called "connected" merely because its name or environment variables exist. Every provider adapter needs authorization, secure secret handling, upload/download/list/delete tests, checksum validation, error handling, and recovery tests.

## Render temporary deployment rule

Do not rely on the Render instance filesystem for durable user files. Until a real cloud storage adapter is implemented and verified, hosted uploads should fail closed when durable storage is not explicitly configured. Do not add provider secrets to GitHub; use the runtime's private environment or a secret manager.

## Rollout sequence

1. Keep GitHub main as source of truth and PR-based changes.
2. Use Render only for temporary API testing.
3. Implement AWS S3 as the first durable object-storage adapter, with least-privilege credentials and private buckets.
4. Add Google Drive and Microsoft Graph adapters through OAuth with owner-granted permissions.
5. Add MEGA only after validating an officially supported API/client and its operational/security requirements.
6. Treat Hostinger primarily as a web hosting/deployment target unless the selected product exposes a suitable storage API.
7. Add shared managed database migration, backup/restore drills, monitoring, and staging tests before production launch.

## Honest readiness criteria

- CI passes on the proposed commit.
- Staging upload/download survives runtime restart and redeploy.
- Stored object checksums match after retrieval.
- Database metadata and object bytes can be restored together.
- Provider connection is confirmed by live, permission-scoped end-to-end checks.
