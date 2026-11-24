# Global Transport, Road, Rail, Air & Mobility Core Ecosystem

This package owns the normal, non-commercial classification of transport modes and
passenger mobility systems: road, rail, air, water/maritime and passenger mobility.

## Responsibilities

- Canonical transport-mode identity and classification
- High-level infrastructure and accessibility metadata
- Read-only discovery of transport modes
- Clear separation from commercial service, work, logistics and supply-chain business domains

## Layer boundary

This is a Core metadata/control-plane package only. It does not book journeys, dispatch
vehicles, track shipments, operate infrastructure, call provider APIs, process payments
or claim live transport availability. Those operations belong to the appropriate API,
engine, database and runtime layers.
