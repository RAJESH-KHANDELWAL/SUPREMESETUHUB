from __future__ import annotations

import pytest
from fastapi import HTTPException


def test_master_id_only_authentication_is_rejected():
    from backend.api.auth import AuthenticateRequest, authenticate

    with pytest.raises(HTTPException) as error:
        authenticate(AuthenticateRequest(master_id="public-or-guessed-id"))

    assert error.value.status_code == 403
    assert error.value.detail == "MASTER_ID_ONLY_AUTHENTICATION_DISABLED_USE_PASSWORD_SIGNIN"
