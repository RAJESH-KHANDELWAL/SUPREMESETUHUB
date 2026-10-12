# SUPREMESETUHUB Eight-Layer Security Baseline

## Security objective

Use defense in depth: each layer must independently reduce risk, fail closed on uncertainty, and be covered by automated tests and operational review. No layer is a substitute for another. This baseline is a target and implementation checklist, not a claim that the whole platform is already secure or certified.

## Group A — Identity and access control

### Layer 1 — Identity proofing and sign-in
- Require verified credentials for authentication; a public identifier such as a master ID is not an authentication factor.
- Use generic failure messages for invalid credentials.
- Keep account recovery as a separately authenticated and audited workflow, never as an authentication bypass.

### Layer 2 — Strong authentication
- Require strong passwords and secure password hashing.
- Require MFA for OWNER/ADMIN accounts and privileged actions.
- Apply login throttling and temporary lockout/risk controls without enabling account-enumeration.

### Layer 3 — Authorization and least privilege
- Deny by default; grant only the permissions explicitly needed.
- Enforce role and resource ownership checks on every private API operation, not only in the UI.
- Separate OWNER, ADMIN, staff, and ordinary-user privileges; do not trust client-supplied roles or user IDs.

### Layer 4 — Session and token integrity
- Require a validated Bearer session for protected actions.
- Enforce expiry, revocation, active-account checks, and safe logout bound to the authenticated session.
- Never let a body-supplied session ID select another user's session for revocation.
- Keep tokens out of URLs, logs, analytics, and error messages.

## Group B — Application, data, and operations

### Layer 5 — Input and application boundary
- Validate request schemas, lengths, formats, content types, and allowed values at every trust boundary.
- Use parameterized database queries; avoid unsafe deserialization, dynamic execution, and untrusted path construction.
- Apply request-size limits and safe error handling.

### Layer 6 — Data and secret protection
- Use TLS in transit and encryption at rest where supported by the deployment.
- Store secrets only in a secret manager or deployment environment, never in source control.
- Minimize sensitive data returned by APIs; redact credentials and tokens from logs.

### Layer 7 — Infrastructure and dependency protection
- Use least-privilege service/database credentials, private network boundaries, secure headers, and rate limits.
- Pin or constrain dependencies, scan for known vulnerabilities, and keep supported runtimes patched.
- Keep production/debug configuration separate; disable debug endpoints and unsafe defaults in production.

### Layer 8 — Detection, recovery, and verification
- Record security-relevant events with timestamps and actor/resource identifiers, while excluding secrets.
- Alert on repeated authentication failures, privilege changes, suspicious access, and unexpected configuration changes.
- Maintain tested backups and recovery procedures; verify restore capability.
- Run automated tests, dependency/security scans, and route-by-route authorization tests in CI before merge.

## Non-negotiable engineering rules

1. No hidden master key, secret URL, hard-coded universal password, or unauthenticated privileged route.
2. Fail closed when identity, permission, session state, or security configuration cannot be verified.
3. No production change is considered complete based only on a code commit; review CI results and deployment configuration.
4. Keep work on feature branches and merge only after review and passing required checks.
5. Track each layer as **Not audited**, **Finding**, **Fix proposed**, **Tests passing**, or **Verified in deployed environment**. Do not mark a layer fully secure based on unit tests alone.

## Current scope note

This document defines the minimum eight-layer baseline. It does not claim that every control above is already implemented. Each layer must be audited against actual routes, deployment settings, secrets, infrastructure, and recovery processes. External penetration testing and production verification remain separate activities.
