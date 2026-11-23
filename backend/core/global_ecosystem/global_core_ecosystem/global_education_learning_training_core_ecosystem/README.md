# Global Education Learning Training CORE Ecosystem

Canonical, vendor-neutral taxonomy for education and learning: early childhood, school, higher education, vocational, professional, digital learning, skills, educator development, research, assessment, inclusion, career learning, language, citizenship and governance.

## Architecture
- `domain_catalog.py`: stable canonical domain IDs and descriptions.
- `catalog.py`: ecosystem identity and capability metadata.
- `contracts.py`: typed query/result contracts.
- `policy.py`: allowed and prohibited operations.
- `service.py`: read-only discovery and search.
- `orchestrator.py`: dependencies and health metadata.
- `manager.py`: public Python entry point (`get_manager()`).
- `manager.php`: PHP metadata facade.
- `tests/`: executable unit tests.

Commercial tutoring, coaching, training delivery, education consulting and learning businesses belong to the sibling Global Bada Business service/work/business CORE. The 2468 master catalog is not modified by this package.
