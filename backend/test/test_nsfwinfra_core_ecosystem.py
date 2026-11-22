"""NSFWinfra Core regression tests for the canonical backend/test suite."""
from __future__ import annotations

from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem import (
    NSFWinfraCoreManager,
    get_manager,
)
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_account_limits_core_ecosystem import get_manager as account_limits
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_anime_generation_core_ecosystem import get_manager as anime
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_async_jobs_core_ecosystem import get_manager as async_jobs
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_image_editing_core_ecosystem import get_manager as image_editing
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_image_generation_core_ecosystem import get_manager as image_generation
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_image_to_video_core_ecosystem import get_manager as image_to_video
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_image_video_effects_core_ecosystem import get_manager as image_video_effects
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_signed_uploads_core_ecosystem import get_manager as signed_uploads
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_text_to_video_core_ecosystem import get_manager as text_to_video
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.nsfwinfra_webhooks_core_ecosystem import get_manager as webhooks

PACKAGE_MANAGERS = (
    account_limits, anime, async_jobs, image_editing, image_generation,
    image_to_video, image_video_effects, signed_uploads, text_to_video, webhooks,
)


def test_root_manager_and_catalog_identity():
    manager = get_manager()
    assert isinstance(manager, NSFWinfraCoreManager)
    listed = manager.list_ecosystems()
    assert listed["success"] is True
    assert listed["count"] == 10
    ids = [item["ecosystem_id"] for item in listed["ecosystems"]]
    assert len(ids) == len(set(ids))
    assert manager.get_ecosystem("NSFW-INFRA-ASYNC-JOBS-CORE") is not None
    assert manager.get_ecosystem("nsfwinfra_async_jobs_core_ecosystem") is not None
    assert manager.get_ecosystem("not-registered") is None


def test_all_ten_package_managers_expose_metadata_without_live_execution():
    assert len(PACKAGE_MANAGERS) == 10
    for factory in PACKAGE_MANAGERS:
        manager = factory()
        status = manager.status()
        capabilities = manager.capabilities()
        assert status["success"] is True
        assert status["status"] == "CORE_CATALOG_ONLY"
        assert capabilities["count"] > 0
        assert capabilities["live_connection_verified"] is False
        assert capabilities["execution_performed"] is False


def test_health_and_status_never_claim_live_connectivity():
    manager = NSFWinfraCoreManager()
    health = manager.health()
    status = manager.status()
    assert health["success"] is True
    assert health["registered_ecosystems"] == 10
    assert health["live_connections_verified"] == 0
    assert status["live_connection_verified"] is False
    assert status["execution_performed"] is False
    assert status["api_calls_performed"] == 0


def test_master_catalog_is_read_only_and_uses_canonical_target():
    reference = get_manager().master_catalog_reference(load_summary=True)
    assert reference["catalog_id"] == "GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM"
    assert reference["target_unique_entries"] == 2468
    assert reference["access_mode"] == "READ_ONLY_ON_DEMAND"
    assert reference["loaded"] is True
    assert reference["catalog_id_verified"] is True
    assert reference["current_unique_entries"] == 246


def test_dependency_map_is_metadata_only():
    dependencies = get_manager().dependency_map()
    assert dependencies["root"] == "NSFW-INFRA-CORE-ECOSYSTEM"
    assert len(dependencies["dependencies"]) == 10
    assert dependencies["execution_performed"] is False
