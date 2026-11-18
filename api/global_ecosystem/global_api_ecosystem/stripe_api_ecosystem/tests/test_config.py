import pytest

from stripe_api_ecosystem.config import StripeConfig


def test_config_requires_secret_key():
    with pytest.raises(ValueError, match="STRIPE_SECRET_KEY"):
        StripeConfig.from_env({})


def test_config_requires_https():
    with pytest.raises(ValueError, match="HTTPS"):
        StripeConfig.from_env({
            "STRIPE_SECRET_KEY": "sk_test_example",
            "STRIPE_API_BASE_URL": "http://localhost",
        })


def test_headers_use_bearer_auth():
    config = StripeConfig.from_env({
        "STRIPE_SECRET_KEY": "sk_test_example",
        "STRIPE_API_VERSION": "2025-01-27.acacia",
    })
    assert config.headers()["Authorization"] == "Bearer sk_test_example"
    assert config.headers()["Stripe-Version"] == "2025-01-27.acacia"
