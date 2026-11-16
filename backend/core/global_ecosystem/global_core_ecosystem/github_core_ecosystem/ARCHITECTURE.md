# GitHub CORE Architecture

GitHub CORE is the provider control plane above 12 family packages. Each package owns stable family identity, capability metadata, request contracts, lifecycle vocabulary, policy metadata, documentation and tests.

## Request flow
1. Application authenticates the caller and supplies tenant/actor context.
2. CORE resolves the family and validates safe request shape and capability metadata.
3. API/Integration authenticates to GitHub and performs a specific REST/GraphQL operation.
4. ENGINE owns retries, rate-limit backoff, asynchronous jobs and webhook delivery.
5. DATABASE/STORAGE own persistence and artifacts.
6. Application presents the result.

CORE never reads environment secrets, constructs Authorization headers, calls GitHub, writes repository data or executes jobs.

## Current API boundary
Shared authenticated REST transport exists at `backend/integration/provider/github.py`. Routes in `backend/api/connectors.py` currently expose status, authenticated user, repository listing and repository metadata. Other family directories remain catalog/API scaffolds until endpoint-specific implementations and tests exist.
