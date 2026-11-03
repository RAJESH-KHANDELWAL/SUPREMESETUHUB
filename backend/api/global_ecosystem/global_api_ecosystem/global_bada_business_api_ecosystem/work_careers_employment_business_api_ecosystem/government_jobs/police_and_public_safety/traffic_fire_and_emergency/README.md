# Traffic, fire and emergency response posts

## Scope
Traffic police, fire officers, firefighters, emergency dispatch and disaster response personnel

## Classification boundary
This folder contains only traffic, fire and emergency response posts. Store recruiting authority, post/cadre, grade, discipline or trade, work context, official notification and appointment status separately. Do not treat a job family as a professional-sector track.

## Implementation
- `categories.py`: specialization-specific identifiers
- `models.py`: typed government-post model
- `validators.py`: required-field and official-URL validation
- `services.py`: registration and authority filtering
- `routes.py`: transport-neutral route handlers
- `api_ecosystem.py`: API registration metadata
- `tests/`: focused validation tests

Do not publish a vacancy as active without a dated official notification from the recruiting authority.
