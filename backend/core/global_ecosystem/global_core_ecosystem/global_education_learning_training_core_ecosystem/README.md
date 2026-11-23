# Global Education Learning Training CORE Ecosystem

Canonical, vendor-neutral knowledge taxonomy for the full education lifecycle: teaching, learning, training, research, skills, qualifications, institutions, lifelong learning and knowledge services.

## Coverage
The taxonomy spans early childhood through doctoral and lifelong learning; school and open schooling; higher, medical, legal, agricultural, technical and vocational education; research; educator development; apprenticeships; digital and AI learning; languages; inclusive learning; examinations; careers; citizenship; health; environment; finance; arts; sports; community education; and education governance.

## Bharat and Global overlays
- `region_catalog.py` defines India/Bharat and global jurisdiction overlays without duplicating canonical domain IDs.
- Bharat coverage includes central, state, union-territory, district, rural, urban, tribal and community education contexts. Framework names are classification references, not claims of regulatory approval.
- Global coverage supports country, territory, regional, cross-border and international education systems. Country-specific regulations must be verified independently.

## Architecture
- `domain_catalog.py`: canonical domain IDs and descriptions.
- `region_catalog.py`: Bharat and global education-system overlays.
- `catalog.py`: ecosystem identity and capability metadata.
- `contracts.py`: typed query/result contracts.
- `policy.py`: allowed and prohibited operations.
- `service.py`: read-only discovery and search.
- `orchestrator.py`: dependencies and health metadata.
- `manager.py`: public Python entry point (`get_manager()`).
- `manager.php`: PHP metadata facade.
- `tests/`: executable unit tests.

Commercial providers and revenue models belong to the sibling Global Bada Business Service Work Business CORE. This package does not modify the backend 2468 master catalog and does not execute enrollment, credential issuance, accreditation or student-record processing.
