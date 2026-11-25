"""Tests for the isolated iDigitalPreneur CORE ecosystem boundary."""
import unittest

from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_affiliate_marketing_business_core_ecosystem.platforms.i_digitalpreneur import (
    ECOSYSTEM_ID,
    IDigitalPreneurCoreManager,
    IDigitalPreneurCoreService,
    IDigitalPreneurModuleService,
    PLATFORM_ID,
    validate_platform_program,
)

class MemoryAffiliateRepository:
    def __init__(self):
        self.programs = {}
        self.referrals = {}

    def upsert_program(self, **record):
        self.programs[record["program_id"]] = dict(record)
        return dict(record)

    def list_programs(self, platform_id=None):
        return [
            dict(record) for record in self.programs.values()
            if platform_id is None or record["platform_id"] == platform_id
        ]

    def get_program(self, program_id):
        record = self.programs.get(program_id)
        return dict(record) if record else None

    def create_referral(self, **record):
        self.referrals[record["referral_code"]] = dict(record)
        return dict(record)

    def get_referral(self, referral_id):
        record = self.referrals.get(referral_id)
        return dict(record) if record else None

    def record_event(self, **record):
        return dict(record)

class IDigitalPreneurCoreTests(unittest.TestCase):
    def test_manager_exposes_isolated_unverified_identity(self):
        status = IDigitalPreneurCoreManager().status()
        self.assertEqual(status["ecosystem_id"], ECOSYSTEM_ID)
        self.assertEqual(status["platform_id"], PLATFORM_ID)
        self.assertFalse(status["program_terms_verified"])
        self.assertFalse(status["live_connection_verified"])

    def test_module_service_is_read_only_and_identity_scoped(self):
        identity = IDigitalPreneurModuleService().identity()
        self.assertEqual(identity["platform_id"], PLATFORM_ID)
        self.assertEqual(identity["parent_ecosystem_id"], "GLOBAL-AFFILIATE-MARKETING-BUSINESS-CORE-ECOSYSTEM")

    def test_policy_rejects_other_platform_identity(self):
        with self.assertRaisesRegex(ValueError, "PLATFORM_ID_MISMATCH"):
            validate_platform_program(
                platform_id="LEADSGURU",
                program_status="PENDING_VERIFICATION",
                verification_status="UNVERIFIED",
                terms_url=None,
            )

    def test_service_forces_idigitalpreneur_platform_id(self):
        service = IDigitalPreneurCoreService(MemoryAffiliateRepository())
        result = service.register_program(
            program_id="idp-program-1",
            program_name="Unverified program record",
        )
        self.assertEqual(result["platform_id"], PLATFORM_ID)
        self.assertEqual(result["verification_status"], "UNVERIFIED")

    def test_service_rejects_leadsguru_program_in_idigitalpreneur_adapter(self):
        repository = MemoryAffiliateRepository()
        repository.programs["leadsguru-program"] = {
            "program_id": "leadsguru-program",
            "platform_id": "LEADSGURU",
            "program_status": "ACTIVE",
        }
        service = IDigitalPreneurCoreService(repository)
        with self.assertRaisesRegex(ValueError, "PLATFORM_ID_MISMATCH"):
            service.create_referral(
                owner_user_id="user-1",
                program_id="leadsguru-program",
                referral_code="ref-1",
                destination_url="https://example.com",
                disclosure_text="This is an affiliate link and I may earn a commission.",
            )

if __name__ == "__main__":
    unittest.main()
