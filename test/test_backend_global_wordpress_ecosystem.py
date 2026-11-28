from __future__ import annotations

from backend.wordpress.global_ecosystem import (
    GlobalWordPressEcosystemManager,
    get_manager,
)


def test_global_wordpress_manager_identity_and_layer():
    manager = GlobalWordPressEcosystemManager()

    status = manager.status()

    assert status["ecosystem_id"] == "GLOBAL-WORDPRESS-ECOSYSTEM"
    assert status["name"] == "GLOBAL WORDPRESS ECOSYSTEM"
    assert status["layer"] == "BACKEND"
    assert status["implementation_path"] == "backend/wordpress"
    assert status["live_connection_verified"] is False
    assert status["remote_operations_enabled"] is False


def test_global_wordpress_manager_health_checks_backend_files():
    result = GlobalWordPressEcosystemManager().health()

    assert result["success"] is True
    assert result["status"] == "STRUCTURE_READY"
    assert result["checks"] == {
        "controller.py": True,
        "service.py": True,
        "registry.py": True,
        "connection.py": True,
    }


def test_get_manager_returns_shared_instance():
    assert get_manager() is get_manager()
