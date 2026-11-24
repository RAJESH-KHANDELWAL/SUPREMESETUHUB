"""Tests for the six provider metadata descriptors in Global Software Core."""

from backend.core.global_ecosystem.global_core_ecosystem.global_software_core_ecosystem.adobe_software_core_ecosystem.service import describe as describe_adobe
from backend.core.global_ecosystem.global_core_ecosystem.global_software_core_ecosystem.apple_software_core_ecosystem.service import describe as describe_apple
from backend.core.global_ecosystem.global_core_ecosystem.global_software_core_ecosystem.aws_software_core_ecosystem.service import describe as describe_aws
from backend.core.global_ecosystem.global_core_ecosystem.global_software_core_ecosystem.github_software_core_ecosystem.service import describe as describe_github
from backend.core.global_ecosystem.global_core_ecosystem.global_software_core_ecosystem.global_atlassian_core_ecosystem.service import describe as describe_atlassian
from backend.core.global_ecosystem.global_core_ecosystem.global_software_core_ecosystem.microsoft_software_core_ecosystem.service import describe as describe_microsoft


def test_provider_descriptors_are_catalog_only_and_non_executable():
    descriptors = [
        describe_adobe(), describe_apple(), describe_aws(),
        describe_github(), describe_atlassian(), describe_microsoft(),
    ]
    assert {item["provider_id"] for item in descriptors} == {
        "adobe", "apple", "aws", "github", "atlassian", "microsoft"
    }
    assert all(item["status"] == "CATALOG_ONLY" for item in descriptors)
    assert all(item["live_connection_verified"] is False for item in descriptors)
    assert all(item["execution_enabled"] is False for item in descriptors)


def test_provider_descriptors_expose_nonempty_domains_and_capabilities():
    for describe in (
        describe_adobe, describe_apple, describe_aws,
        describe_github, describe_atlassian, describe_microsoft,
    ):
        descriptor = describe()
        assert descriptor["domains"]
        assert descriptor["capabilities"]
