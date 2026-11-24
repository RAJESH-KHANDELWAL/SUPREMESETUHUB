"""Security regression tests for the universal profiles API."""
from backend.api import profiles as profiles_api
from backend.security.dependencies import require_admin


def test_profiles_router_requires_admin_for_all_routes():
    """Private profiles and metadata must not be anonymously enumerable or mutable."""
    assert profiles_api.router.dependencies
    assert any(
        dependency.dependency is require_admin
        for dependency in profiles_api.router.dependencies
    )


def test_profile_routes_are_not_publicly_exposed_without_router_guard():
    """Every profile route inherits the router-wide admin dependency."""
    routes = [route for route in profiles_api.router.routes if getattr(route, "methods", None)]
    assert routes
    for route in routes:
        assert any(
            dependency.call is require_admin
            for dependency in route.dependant.dependencies
        ), f"Missing admin guard on {route.path}"
