# SUPREME ECOSYSTEM Role Governance

## Dashboard placement

- This is reusable backend platform functionality for businesses, companies, teams, and people who use SUPREMESETUHUB; it is not a private owner-dashboard feature.
- The private SUPREME OWNER ADMIN control plane remains separate and is only for the platform owner’s own system governance.
- Business/company roles are scoped to the relevant organization/business/team/resource and never automatically grant platform-owner authority.

## Default role/title templates

The backend catalog includes PRIMARY OWNER, OWNER, FOUNDER, CO-FOUNDER, CEO, CMD, MD, CMA, ADMIN, MANAGER, MEMBER, and CUSTOM ROLE. The catalog also defines a permission dictionary and workflow sections.

A title is not a permission. A person may display FOUNDER or CEO while receiving only the explicit permissions approved for the assigned business scope. CMA is a professional designation, not an access role. Qualification, employment, company ownership, signing authority, and any statutory authority require independent verification where relevant.

## Permission domains

Business profile, people/invitations, role/permission administration, work/task assignment, review/approval, content, leads, finance summaries, finance management, payment approvals, learning, performance reviews, promotion recommendations/approvals, own earnings, earnings administration, audit, integrations, security, and company legal records have separate permission IDs.

Use least-privilege grants. Financial approvals, legal records, security controls, role/permission administration, and ownership transfer must never be granted just because a user has a senior-sounding title. Apply organization/business/team/resource scope and approval limits.

## Work and growth views

Each business workspace should present these separate sections:

- **WORK:** tasks, assignments, deadlines, deliverables, reviews, approvals.
- **PROGRESS:** status, milestones, completion, evidence, blockers, review history.
- **PROMOTION:** eligibility criteria, skills evidence, recommendation, authorized approval, effective date, audit history.
- **LEARNING:** learning paths, courses, skills, certifications, assessments, completion records.
- **EARNING:** compensation/commission policy, approved earnings, adjustments, payout status/history.
- **VERIFICATION:** identity, role assignment, permission review, qualification verification, work evidence, approval audit.

These are workflow definitions and data requirements, not proof that the underlying task, payroll, learning, or promotion services are already implemented. Earning/payout workflows do not move money without a separate authorized payment integration.

## Custom role option

The catalog defines fields for a future custom-role form: custom title, category, business/team scope, permission IDs, allowed work types, approval limits, learning goals, promotion criteria, earnings policy, effective date, expiry, and review date. The role should be previewed and verified before an authorized owner saves or assigns it.

## Current implementation status

The authenticated platform-user endpoint is:

`GET /api/v1/businesses/role-governance/catalog`

It returns default role templates, permission descriptions, workflow sections, custom-role fields, and verification rules to signed-in platform users. It is protected by the standard authenticated-user dependency, not the private SUPREME owner dependency. The catalog is shared metadata; any later role assignment or permission grant must be enforced against the authenticated user’s own business/company scope.

**Current limitation:** this change adds a shared template catalog only. It does not yet persist company records, custom roles, role assignments, individual permission grants, tasks, promotion decisions, learning progress, earnings, or verification events, and it does not enforce those permissions at runtime. Those require persistent data models, scoped authorization checks on each operation, audit logging, and tests before production use.
