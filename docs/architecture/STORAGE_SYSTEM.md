# Storage System

Status: **design documentation; provider connectivity and durable production storage are not certified here.**

Purpose: manage where durable data and backup artifacts live, how they are accessed, and how their lifecycle is controlled.

## Scope
- Storage targets and abstraction
- Object, file, and block storage adapters
- Capacity and health monitoring
- Access control and encryption
- Lifecycle and retention policies

## Suggested modules
- `providers/`
- `adapters/`
- `policies/`
- `capacity/`
- `health/`
- `access-control/`
- `encryption/`

## Safety
Separate production storage from backup destinations. Apply least-privilege access and never store credentials in source control.
