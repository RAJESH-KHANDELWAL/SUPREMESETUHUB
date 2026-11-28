# ASYNC JOBS INFRA CORE ECOSYSTEM

**Parent:** NSF Winfra Core Ecosystem  
**Package:** `nsfwinfra_async_jobs_core_ecosystem/`  
**Ecosystem ID:** `NSFW-INFRA-ASYNC-JOBS-CORE`

## Scope

Contracts and policies for asynchronous job types, states, queues, priorities, worker capability metadata, concurrency, retries, timeouts, cancellation, dead-letter handling, idempotency, dependencies, progress and recovery. Execution, workers, queues and persistence are separate runtime responsibilities.

## Capability metadata

- `JOB_CONTRACTS`
- `LIFECYCLE_STATES`
- `QUEUE_METADATA`
- `PRIORITY_AND_SCHEDULING`
- `WORKER_CAPABILITY_METADATA`
- `CONCURRENCY_LIMITS`
- `RETRY_AND_BACKOFF_POLICY`
- `TIMEOUTS`
- `CANCELLATION_METADATA`
- `DEAD_LETTER_POLICY`
- `IDEMPOTENCY_REFERENCES`
- `PROGRESS_AND_RESULT_CONTRACTS`
- `RECOVERY_METADATA`

## Package interface

- `manager.py`: canonical package manager, status and capability inventory.
- `__init__.py`: public package exports.

The manager reports `CORE_CATALOG_ONLY`; it does not execute infrastructure operations, persist records, call APIs, or claim verified live connections. Authorization, secrets, transport, execution and persistence remain in their designated layers. Add package files only for concrete additional responsibilities.
