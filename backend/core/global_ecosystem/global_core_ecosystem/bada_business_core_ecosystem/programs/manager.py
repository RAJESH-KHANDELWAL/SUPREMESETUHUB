"""Facade for the Bada Business CORE programs domain."""

from .service import BadaBusinessProgramsService


class BadaBusinessProgramsManager:
    def __init__(self, service=None):
        self.service = service or BadaBusinessProgramsService()

    def status(self):
        return self.service.get_status()

    def list_programs(self):
        return self.service.list_programs()

    def get_program(self, program_id: str):
        return self.service.get_program(program_id)

    def search_programs(self, query: str):
        return self.service.search_programs(query)

    def prepare_enrollment_request(self, program_id: str, applicant: dict):
        return self.service.prepare_enrollment_request(program_id, applicant)
