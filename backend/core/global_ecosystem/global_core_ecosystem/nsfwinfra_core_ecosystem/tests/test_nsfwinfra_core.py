"""Root NSF Winfra Core catalog and manager tests."""
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem import NSFWinfraCoreManager, get_manager

def test_catalog_has_ten_unique_ecosystems():
    listed = get_manager().list_ecosystems()
    ids = [item["ecosystem_id"] for item in listed["ecosystems"]]
    assert listed["success"] is True
    assert listed["count"] == 10
    assert len(ids) == len(set(ids))

def test_health_status_do_not_claim_live_execution():
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
