# Architecture

- catalog.py: canonical 35-category taxonomy, root and relationship type set.
- models.py: immutable relationship record contract.
- registry.py: in-memory taxonomy registry with duplicate-key detection.
- policy.py: required-field, relationship-type, self-edge and evidence checks.
- service.py: read-only service facade.
- manager.py: status, discovery, hierarchy and master-catalog reference.
- manager.php: PHP metadata contract facade; no duplicated catalog data.
- test_global_entity_relationships_core.py: naming, counts, tree, policy and 2468 reference checks.

Architecture boundaries: no API calls, credential access, persistence writes, or claims of real-world verification.
