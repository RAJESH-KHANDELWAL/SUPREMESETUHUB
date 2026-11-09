# Company Modules API Ecosystem

## Purpose
Provides a searchable index of the company-specific code packages already present under
`global_companies_ecosystem/`. It makes those modules discoverable through the parent
Company Companies API.

## Important boundary
This is a **code-module index**, not a company-profile database. A listed package does
not prove that its profile is implemented, verified, current, or connected to
`data/company_registry.json`. The shared company registry remains the source used by
the existing profile-search endpoints.

## API
- `GET /global/company-directory/company-modules/status`
- `GET /global/company-directory/company-modules`
- `GET /global/company-directory/company-modules/search?q=apple`
- `GET /global/company-directory/company-modules/{company_id}`

## Maintenance
When a company-specific package is added or removed, update
`registry.py` and the registry tests together. Do not add unsupported profile facts
or mark a module as verified merely because its package exists.
