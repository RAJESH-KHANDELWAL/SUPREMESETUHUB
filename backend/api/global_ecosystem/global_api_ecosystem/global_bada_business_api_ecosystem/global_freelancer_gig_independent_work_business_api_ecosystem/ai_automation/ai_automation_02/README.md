# Independent Work-Type API Package

This folder is the independently addressable package for one canonical work type.

## Source of truth
The stable work-type ID, display name and description remain owned by the parent specialization's `work_types.py`. This package resolves its own ID from its folder name and reads the canonical record; it does not duplicate or fork that metadata.

## Package modules
- `categories.py`: canonical work-type binding and metadata integrity.
- `models.py`: typed work-type record.
- `catalog.py`: lookup and serialization.
- `schemas.py`: response contracts.
- `services.py`: status and resource facade.
- `routes.py`: dedicated API endpoints.
- `validators.py`: structural validation.
- `tests/`: independent package tests.

## Scope
This is a taxonomy/API contract only. It does not represent a live gig, vacancy, client, payment, licence or provider verification.
