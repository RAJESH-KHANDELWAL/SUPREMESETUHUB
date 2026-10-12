# SUPREMESETUHUB Central Repository Registry

## Purpose

SUPREMESETUHUB is the main base foundation. This registry gives the foundation
one canonical record for each repository visible to the connected GitHub account.

## Current registered repositories

| Registry key | GitHub repository | Purpose |
|---|---|---|
| `SUPREMESETUHUB` | [RAJESH-KHANDELWAL/SUPREMESETUHUB](https://github.com/RAJESH-KHANDELWAL/SUPREMESETUHUB) | Main base foundation |
| `RAJESHKHANDELWAL` | [RAJESH-KHANDELWAL/RAJESHKHANDELWAL](https://github.com/RAJESH-KHANDELWAL/RAJESHKHANDELWAL) | AI engine project |
| `SUPREMESETUHUB_DEMO` | [RAJESH-KHANDELWAL/demo-repository](https://github.com/RAJESH-KHANDELWAL/demo-repository) | Demo project |
| `RAJESHKHANDELWALOFFICIAL` | [RAJESH-KHANDELWAL-OFFICIAL/RAJESHKHANDELWALOFFICIAL](https://github.com/RAJESH-KHANDELWAL-OFFICIAL/RAJESHKHANDELWALOFFICIAL) | Official brand project |
| `IBC_DEMO` | [DR-RAJESH-KHANDELWAL-IBC/demo-repository](https://github.com/DR-RAJESH-KHANDELWAL-IBC/demo-repository) | Demo project |
| `DRRAJESHKHANDELWALIBC` | [DR-RAJESH-KHANDELWAL-IBC/DRRAJESHKHANDELWALIBC](https://github.com/DR-RAJESH-KHANDELWAL-IBC/DRRAJESHKHANDELWALIBC) | IBC identity project |

## API

The authenticated backend endpoint `GET /api/v1/connectors/github/repositories`
returns the canonical repository registry and each project's declared integration
state. The existing API authentication middleware applies to this route.

## Important state distinction

- `PRIMARY` means the main foundation repository.
- `REGISTERED` means a repository is listed in the central registry.
- `runtime_connection: NOT_CONFIGURED` means a live service-to-service connection
  has not been configured and verified.
- Automatic repository synchronization is disabled until authenticated sync,
  per-repository authorization, conflict handling, and audit logging are implemented
  and tested.

A GitHub URL in this registry is not proof that a deployed website, app, server,
database, or AI runtime is already connected. Do not mark a project as live-connected
until a real authenticated health check or integration test succeeds.

## Safe integration sequence

1. Keep SUPREMESETUHUB as the canonical identity and project registry.
2. Configure per-project API base URLs through deployment environment variables.
3. Use scoped credentials stored in deployment secrets; never commit tokens.
4. Add per-service health checks and explicit timeout/error handling.
5. Enforce owner/admin authorization and resource-level access controls.
6. Test each integration in staging, log results, and enable sync only after review.
7. Keep each project independently deployable; the foundation coordinates them
   through APIs rather than requiring every project to share one process or database.
