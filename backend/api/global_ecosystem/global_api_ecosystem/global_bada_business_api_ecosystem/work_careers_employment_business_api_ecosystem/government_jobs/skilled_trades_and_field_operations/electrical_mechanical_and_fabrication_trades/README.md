# Electrical, mechanical and fabrication trades

## Scope
Electricians, fitters, welders, machinists, mechanics and plumbers

## Classification boundary
This folder contains only electrical, mechanical and fabrication trades. Store recruiting authority, post/cadre, grade, discipline or trade, work context, official notification and appointment status separately. Do not treat a job family as a professional-sector track.

## Implementation
- `categories.py`: specialization-specific identifiers
- `models.py`: typed government-post model
- `validators.py`: required-field and official-URL validation
- `services.py`: registration and authority filtering
- `routes.py`: transport-neutral route handlers
- `api_ecosystem.py`: API registration metadata
- `tests/`: focused validation tests

Do not publish a vacancy as active without a dated official notification from the recruiting authority.
