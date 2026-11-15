# Global Agriculture Ecosystem

Bharat-to-global agriculture domain package covering crop production, soil,
seeds, irrigation, farm machinery, livestock, fisheries, agricultural finance
and agricultural supply chains.

The central domain registry defines geographic scopes (Bharat, regions and
global) and maturity levels (basic/normal through supreme long-horizon).
These are scope labels, not proof that every geography or maturity tier is
implemented.

## Current code
- Typed starter models for farms, crop plans and irrigation estimates.
- A discoverable catalogue of nine agriculture modules.
- Basic farm and crop-plan validation.
- A transparent irrigation water-use estimate using caller-supplied ET0 and Kc.

## Not yet implemented
Live weather/soil/market feeds, crop recommendations, government-scheme
integrations, payment rails, farm-device connectivity, database persistence,
public APIs and validated region-specific agronomic models. This package is
starter code, not a production agriculture platform. Validate agronomic inputs
with local experts before operational use.
