# GLOBAL ENTITY RELATIONSHIPS CORE ECOSYSTEM — Architecture

## Control plane
`catalog.py` → `registry.py` → `manager.py` → `service.py`

`models.py` defines relationship metadata. `policy.py` validates metadata shape, relationship types, verification-state labels, self-edge restrictions, and evidence URL format. `orchestrator.py` provides discovery and health coordination.

## Data boundary
- Taxonomy and metadata are read-only.
- No relationship persistence, API transport, OAuth, scraping, or background execution.
- No claim is independently verified by this CORE.
- The 2468 master catalog is referenced by path and counts; it is not copied or modified.

## Safety and privacy
Minimize personal data; treat sensitive categories as restricted metadata; require lawful purpose, applicable consent, access controls, and human review. Validation must never be presented as proof of a real-world relationship.
