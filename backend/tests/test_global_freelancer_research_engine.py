from __future__ import annotations

from backend.freelancer.global_freelancer_ecosystem.research_engine import (
    FreelancerResearchEngine,
    _host,
    _relevance_score,
    _safe_http_url,
)


def test_status_does_not_claim_search_is_enabled_without_credentials(monkeypatch):
    monkeypatch.delenv("BRAVE_SEARCH_API_KEY", raising=False)
    monkeypatch.delenv("GOOGLE_CSE_API_KEY", raising=False)
    monkeypatch.delenv("GOOGLE_CSE_CX", raising=False)
    status = FreelancerResearchEngine().status()
    assert status["search_enabled"] is False
    assert all(not provider["configured"] for provider in status["providers"])


def test_search_reports_missing_provider_configuration(monkeypatch):
    monkeypatch.delenv("BRAVE_SEARCH_API_KEY", raising=False)
    monkeypatch.delenv("GOOGLE_CSE_API_KEY", raising=False)
    monkeypatch.delenv("GOOGLE_CSE_CX", raising=False)
    result = FreelancerResearchEngine().search("translation", market="bharat")
    assert result["success"] is False
    assert result["status"] == "SEARCH_PROVIDER_CONFIGURATION_REQUIRED"
    assert result["results"] == []


def test_search_validates_market_and_category():
    engine = FreelancerResearchEngine()
    try:
        engine.search("writer", market="mars")
    except ValueError as exc:
        assert str(exc) == "MARKET_MUST_BE_BHARAT_OR_GLOBAL"
    else:
        raise AssertionError("invalid market should fail")

    try:
        engine.search("writer", category="unknown")
    except ValueError as exc:
        assert str(exc) == "UNSUPPORTED_RESEARCH_CATEGORY"
    else:
        raise AssertionError("invalid category should fail")


def test_url_and_relevance_helpers():
    assert _host("https://www.example.com/jobs/1") == "example.com"
    assert _safe_http_url("https://example.com/jobs")
    assert not _safe_http_url("javascript:alert(1)")
    assert _relevance_score("Translation freelancer", "Remote writing work", "translation") == 100
