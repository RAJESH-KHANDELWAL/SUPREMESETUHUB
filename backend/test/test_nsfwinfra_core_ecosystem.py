"""Root NSF Winfra Core and package manager contract tests."""
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem import NSFWinfraCoreManager, get_manager
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.manager import get_ecosystem, list_ecosystems
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_account_limits_core_ecosystem import get_manager as account_limits_manager
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_anime_generation_core_ecosystem import get_manager as anime_manager
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_async_jobs_core_ecosystem import get_manager as async_jobs_manager
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_image_editing_core_ecosystem import get_manager as image_editing_manager
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_image_generation_core_ecosystem import get_manager as image_generation_manager
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_image_to_video_core_ecosystem import get_manager as image_to_video_manager
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_image_video_effects_core_ecosystem import get_manager as effects_manager
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_signed_uploads_core_ecosystem import get_manager as signed_uploads_manager
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_text_to_video_core_ecosystem import get_manager as text_to_video_manager
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_webhooks_core_ecosystem import get_manager as webhooks_manager
PACKAGE_MANAGERS = (account_limits_manager, anime_manager, async_jobs_manager, image_editing_manager, image_generation_manager, image_to_video_manager, effects_manager, signed_uploads_manager, text_to_video_manager, webhooks_manager)
def test_catalog_has_ten_unique_ecosystems():
    listed = get_manager().list_ecosystems()
    ids = [item["ecosystem_id"] for item in listed["ecosystems"]]
    assert listed["success"] is True
    assert listed["count"] == 10
    assert len(ids) == len(set(ids))
def test_health_and_status_do_not_claim_live_execution():
    manager = NSFWinfraCoreManager()
    assert manager.health()["success"] is True
    status = manager.status()
    assert status["live_connection_verified"] is False
    assert status["execution_performed"] is False
def test_lookup_by_id_and_package_name():
    manager = get_manager()
    assert manager.get_ecosystem("NSFW-INFRA-ASYNC-JOBS-CORE") is not None
    assert manager.get_ecosystem("nsfwinfra_async_jobs_core_ecosystem") is not None
    assert manager.get_ecosystem("not-registered") is None
def test_all_ten_package_managers_have_capabilities_and_non_live_status():
    assert len(PACKAGE_MANAGERS) == 10
    for factory in PACKAGE_MANAGERS:
        manager = factory()
        status = manager.status()
        capability_inventory = manager.capabilities()
        assert status["success"] is True
        assert status["status"] == "CORE_CATALOG_ONLY"
        assert capability_inventory["count"] > 0
        assert capability_inventory["live_connection_verified"] is False
        assert capability_inventory["execution_performed"] is False
def test_master_catalog_reference_is_read_only_and_correct_target():
    reference = get_manager().master_catalog_reference(load_summary=True)
    assert reference["catalog_id"] == "GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM"
    assert reference["target_unique_entries"] == 2468
    assert reference["access_mode"] == "READ_ONLY_ON_DEMAND"
    assert reference["loaded"] is True
    assert reference["catalog_id_verified"] is True
    assert reference["current_unique_entries"] == 246

def test_catalog_helpers_are_owned_by_manager_and_return_defensive_copies():
    first = list_ecosystems()
    assert len(first) == 10
    first[0]["capabilities"].append("MUTATION_SENTINEL")
    assert "MUTATION_SENTINEL" not in list_ecosystems()[0]["capabilities"]
    assert get_ecosystem("NSFW-INFRA-ASYNC-JOBS-CORE") is not None
    assert get_ecosystem("not-registered") is None
