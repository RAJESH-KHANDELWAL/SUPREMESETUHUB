# Government Jobs

## Purpose
Dedicated taxonomy for public-authority recruitment tracks. This is not a live vacancy directory, employer verification service, recruitment agency, examination calendar or legal eligibility engine.

## Recruitment tracks
Central/national government; state/provincial government; local government; civil services; public education; public health; public safety; defence civilian; public research and scientific; judiciary and public legal; public finance and audit; public infrastructure and engineering; and public-sector enterprise recruitment.

## Package responsibilities
- `categories.py`: detailed recruitment-track definitions and internal integrity checks
- `models.py`: typed track and recruitment-notice provenance records
- `schemas.py`: typed notice contract
- `services.py`: listing, lookup, search and status operations
- `validators.py`: structural notice-provenance checks
- `routes.py`: status, tracks, detail, search and integrity API endpoints
- `tests/`: unit tests

## Notice provenance
A notice record should preserve issuing authority, jurisdiction, official source URL, notice identifier, publication date, application deadline when supplied, last-verified timestamp and verification status. HTTPS format validation is not proof that a domain is official. A status such as `authority_confirmed` must be backed by a separate verification evidence record before use.

## Explicit limitations
This package does not provide live vacancies, examination schedules, candidate eligibility determinations, reservation decisions, visa/work authorization, professional licensing decisions or legal opinions. Do not collect candidate identity documents or sensitive personal data in this taxonomy package.
