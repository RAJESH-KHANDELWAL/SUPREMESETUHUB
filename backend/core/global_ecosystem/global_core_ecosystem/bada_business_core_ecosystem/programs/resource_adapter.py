"""Read-only adapter to the canonical Bada Business resource catalog."""

from backend.global_ecosystem.global_bada_business_ecosystem.platform_resources.catalog import (
    get_catalog,
    get_program,
    list_programs,
)


class BadaBusinessProgramResourceAdapter:
    """Expose canonical program facts without copying provider data."""

    def get_catalog(self):
        return get_catalog()

    def list_programs(self):
        return list_programs()

    def get_program(self, program_id: str):
        return get_program(program_id)
