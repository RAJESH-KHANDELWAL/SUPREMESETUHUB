"""Public manager for Bada Business program persistence."""

from .service import BadaBusinessProgramPersistenceService


class BadaBusinessProgramDatabaseManager:
    def __init__(self, service=None):
        self.service = service or BadaBusinessProgramPersistenceService()

    def sync_canonical_catalog(self, owner_user_id: str, *, source_version: str = ""):
        return self.service.sync_canonical_catalog(owner_user_id, source_version=source_version)

    def save_snapshot(self, owner_user_id: str, program: dict, *, source_version: str = ""):
        return self.service.save_snapshot(owner_user_id, program, source_version=source_version)

    def get_program(self, owner_user_id: str, program_id: str):
        return self.service.get_program(owner_user_id, program_id)

    def list_programs(self, owner_user_id: str, *, program_status: str | None = None, limit: int = 100):
        return self.service.list_programs(owner_user_id, program_status=program_status, limit=limit)

    def delete_program(self, owner_user_id: str, program_id: str):
        return self.service.delete_program(owner_user_id, program_id)
