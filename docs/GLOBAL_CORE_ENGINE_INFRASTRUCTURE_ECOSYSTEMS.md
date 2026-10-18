# GLOBAL CORE, ENGINE, AND INFRASTRUCTURE ECOSYSTEMS

The GLOBAL API ECOSYSTEM now exposes a separate subsystem catalog for:

- GLOBAL CORE ECOSYSTEM
- GLOBAL ENGINE ECOSYSTEM
- GLOBAL DATABASE ECOSYSTEM
- GLOBAL STORAGE ECOSYSTEM
- GLOBAL DNS ECOSYSTEM
- GLOBAL VPS ECOSYSTEM
- GLOBAL VPN ECOSYSTEM
- GLOBAL CLOUD ECOSYSTEM

## API

- `GET /api/v1/global-api-ecosystem/subsystems`
- `GET /api/v1/global-api-ecosystem/subsystems/{subsystem_id}`

IDs are `core`, `engine`, `database`, `storage`, `dns`, `vps`, `vpn`, and `cloud`.

## Architecture boundary

This catalog links existing source paths and provides one discovery surface. It does not replace or merge runtime `backend/...`, master `BACKEND/...`, or visual/documentation `🖥️ BACKEND 🖥️/...` layers. Existing subsystem implementations remain in place. Provider-specific provisioning, DNS mutation, VPN tunnel creation, and live cloud/storage/database connection verification must be implemented and tested separately before being represented as live.

The status fields describe project-code linkage only. `external_connection_verified` is deliberately false for every catalog entry.

## Google ecosystem cross-links

The provider catalog also links the existing Google entrypoints and subsystem modules:

- Root Python/PHP entrypoints and canonical Google ecosystem service
- Google company API ecosystem and existing Google API router
- Google Cloud, Database, DNS, Server, and Storage subsystem service paths
- Existing provider readiness and platform-specific Google Workspace, Google Cloud, and Google Play paths

These are references to existing source code, not duplicated implementations. They do not imply that every Google product API is implemented or that a live Google account is connected.
