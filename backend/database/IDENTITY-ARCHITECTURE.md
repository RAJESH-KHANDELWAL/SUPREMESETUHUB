# SUPREMESETUHUB — Central Identity Architecture

## Intended hierarchy

- **Central system:** `SUPREMESETUHUB`
- **Logical identity gates:**
  - `RAJESHKHANDELWALOFFICIAL`
  - `RAJESHKHANDELWAL`
  - `DRRAJESHKHANDELWALIBCOFFICIAL`
  - `DRRAJESHKHANDELWALIBC`

There are five identities, not five separate operational systems. All five use
one central SUPREMESETUHUB database. Existing WordPress databases remain
separate and are not migrated or modified by this identity layer.

## What this foundation provides

1. **Identity registry** — stable codes, display names, main/gate classification,
   active/inactive status, and one central storage target.
2. **Identity resolution** — rejects unknown, disabled, or out-of-database gates.
3. **Identity-scoped authorization** — principal-to-identity role assignments
   and role-to-permission mapping (RBAC).
4. **Request context** — Python request-local context so one request's identity
   cannot accidentally bleed into another concurrent request.
5. **Data isolation contract** — every identity-owned record must carry
   `identity_code`; reads, updates, and deletes must include a parameterized
   identity predicate. New business tables should use a composite key or index
   beginning with `identity_code` where appropriate.
6. **PHP integration helper** — validates identity codes and returns parameterized
   scope predicates for PDO-based applications.
7. **Audit-ready extension points** — role grants, permission changes, identity
   activation/deactivation, and cross-gate administrative actions should be
   audited before production use.

## Database schema

- `001_identity_gate_foundation.sql`: the five identity registry rows.
- `002_identity_access_control.sql`: principal-role assignments and
  role-permission definitions. It assigns no principal and grants no user access.

Apply migrations manually only after confirming the configured central database
name and taking a verified backup. Do not run these against either WordPress
database. The SQL migration files are not applied merely by committing them.

## Roles

- `OWNER`: identity and user administration plus data read/write.
- `ADMIN`: identity read, user administration, data read/write.
- `EDITOR`: identity read and data read/write.
- `VIEWER`: identity and data read.

Role definitions are not account provisioning. A trusted authentication layer
must establish `principal_id`; an administrator must explicitly assign the
principal a role for a specific identity.

## Required integration rules

- Never trust an identity code supplied by a client without validating it.
- Authenticate the principal first, then call `IdentityGateService.authorize`.
- Set and reset the Python identity context around each request.
- Add `identity_code` to every identity-owned table and enforce it in every
  repository query. Do not rely only on frontend filtering.
- Cross-identity access is denied by default. A future central owner/super-admin
  flow must be explicit, permission-checked, and audited.
- Do not store passwords, API keys, session tokens, or database credentials in
  this registry or in Git.

## Not yet provisioned

This is repository-side architecture only. It does not create a live Hostinger
database, apply SQL, provision users, connect production domains, or change
WordPress installations. Runtime secrets, database provisioning, migrations,
and API middleware integration remain separate deployment tasks.
