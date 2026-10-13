# SUPREMESETUHUB — One Business, Two Domain Gates

## Binding architecture decision

SUPREMESETUHUB is **one business and one shared platform**, reached through two domain gates. The domains are identities/entry points, not separate businesses or independent data silos.

- Gate A: `drrajeshkhandelwalibc.com` and `www.drrajeshkhandelwalibc.com`
- Gate B: `rajeshkhandelwalofficial.com` and `www.rajeshkhandelwalofficial.com`
- Source of truth: the SUPREMESETUHUB GitHub repository for code, with one deployed shared backend and one configured shared production data store.
- Both gates should preserve the same route paths after the hostname, for example `/services`, `/dashboard`, and `/profile`, wherever those routes exist in the application.
- The hostname may determine branding/display identity only. It must not silently create a second customer, business record, permission system, or database.
- Authentication, authorization, validation, and business rules belong in the shared backend, not in domain-specific frontend code.

## Request flow

```text
drrajeshkhandelwalibc.com ───┐
                             ├── same route contract ── shared backend/API ── shared production database
rajeshkhandelwalofficial.com ┘
```

GitHub is the source-control/automation foundation; it is not itself the live web host, API host, or database. A deployment is complete only after the hosting configuration and live endpoints are verified.

## Required implementation and deployment sequence

1. **Choose the single production backend URL** from the actual deployed service. Do not use placeholders such as `YOUR-PRODUCTION-DOMAIN.com`.
2. **Configure both domains as gates** in the hosting/DNS layer. Both domains must route to the same application origin or to equivalent frontend deployments that call the same API.
3. **Preserve paths.** Verify a request to `https://drrajeshkhandelwalibc.com/<path>` and `https://rajeshkhandelwalofficial.com/<path>` resolves to the same intended application route. Configure WordPress rewrite/proxy rules only if WordPress is serving as a gate; do not assume two separate WordPress installations share state automatically.
4. **Use one backend API contract.** Web and mobile clients should read the production API URL from one documented configuration point per client and use versioned HTTPS endpoints.
5. **Use one persistent production datastore.** Configure and verify a managed database or persistent storage on the backend host. Do not treat separate WordPress MySQL databases or ephemeral SQLite files as a shared source of truth.
6. **Configure CORS for both HTTPS origins**, including www variants only if those variants are actually served. CORS is not authentication and does not grant access.
7. **Keep user identity global.** Resolve users by stable backend IDs; usernames/display names may be gate-specific, but account ownership and permissions must be enforced server-side.
8. **Verify with smoke tests:** health endpoint, same path from both domains, login/session behavior, create/read/update of a test record from each gate, and confirm that the same record is visible from both. Confirm unauthorized users cannot read another user's data.
9. **Deploy WordPress changes separately.** Repository changes do not install plugins, change DNS, assign domains in Hostinger, set secrets, or migrate live data. Back up both WordPress sites and test on staging before changing production.

## Current evidence and blockers

The backend CORS allowlist in `backend/api/app.py` already includes both primary domains and their www variants. This is only browser-origin permission; it does **not** prove both domains reach the same backend.

The Render Blueprint currently defines the service `main-base-foundation-api`, but its public production URL must be verified in the Render dashboard. The environment template contains WordPress database placeholders only. No live shared WordPress database connection is implied.

Before claiming this architecture is live, record and verify:
- Actual production API URL and successful HTTPS health check
- DNS/Hostinger domain assignment for both domains
- Whether each domain is WordPress-served, proxy-served, or a redirect
- One shared persistent backend datastore and migration status
- Cross-domain route, authentication, and shared-record smoke-test results

## Safety rules

- Never commit passwords, OAuth secrets, API keys, session tokens, or database credentials.
- Do not merge two live WordPress databases blindly; establish the canonical dataset and a tested migration/backup plan first.
- Do not use redirects if both domains are required to remain independent gates. A redirect would make one domain forward to the other instead of serving as its own gate.
- Do not call the setup production-ready until real deployed checks pass.
