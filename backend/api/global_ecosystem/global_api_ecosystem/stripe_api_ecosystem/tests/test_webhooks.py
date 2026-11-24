import pytest
import stripe

from stripe_api_ecosystem.config import StripeConfig
from stripe_api_ecosystem.webhooks import verify_webhook


def test_webhook_requires_secret():
    config = StripeConfig(secret_key="sk_test_example")
    with pytest.raises(ValueError, match="STRIPE_WEBHOOK_SECRET"):
        verify_webhook(b"{}", "t=0,v1=invalid", config)


def test_webhook_rejects_invalid_signature():
    config = StripeConfig(secret_key="sk_test_example", webhook_secret="whsec_example")
    with pytest.raises(ValueError, match="Invalid Stripe webhook"):
        verify_webhook(b'{"id":"evt_test"}', "t=0,v1=invalid", config)
