# Global Defence Ecosystem

Bharat-to-global catalogue for lawful defence-adjacent services, civil protection,
cyber defence, disaster response, public safety, resilience and readiness.

## Scope
- Geographic coverage: India, states/districts, South Asia, APAC, Middle East,
  Africa, Europe, North America, Latin America, Oceania and cross-border.
- Maturity: normal/basic, standard, professional, advanced, expert, enterprise,
  research, frontier and supreme long-horizon planning.
- Capabilities: defensive cybersecurity, emergency preparedness, civil
  protection, public information, resilience, safety research and training.

## Architecture boundaries
This package owns domain metadata and non-operational planning helpers only.
API routing belongs to API; orchestration belongs to ENGINE; general policies
belong to CORE; persistence and credentials belong to DATABASE and SECURITY.
It does not connect to defence networks or command systems.

## Safety boundary
No autonomous target selection, weapon release, lethal action, unlawful
surveillance, coercive population control or civilian-harm optimization.
Human authority, legal review, auditability, privacy and proportionality are
required. Adult sexual-content services are not part of this defence package;
they belong in the separate adult-health/intimacy domain and must be adult-only,
consensual and legally compliant.

## Current implementation
- `catalog.py`: capability groups, geographic scopes, maturity levels.
- `models.py`: typed use-case records.
- `registry.py`: in-memory metadata registry.
- `risk/`: safeguard checks.
- `civil_protection/`: emergency planning checklist.
- `cyber_defence/`: defensive control coverage.
- `readiness/`: readiness scorecard.
- `tests/`: test definitions (not yet executed in this commit).

These are catalogue and planning utilities, not a production command platform.
