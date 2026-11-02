from __future__ import annotations

import pytest
from fastapi import HTTPException


def test_master_id_only_authentication_is_rejected():
    from backend.api.auth import AuthenticateRequest, authenticate

    with pytest.raises(HTTPException) as error:
        authenticate(AuthenticateRequest(master_id="public-or-guessed-id"))

    assert error.value.status_code == 403
    assert error.value.detail == "MASTER_ID_ONLY_AUTHENTICATION_DISABLED_USE_PASSWORD_SIGNIN"



def test_signin_rejects_master_id_without_password():
    from fastapi import HTTPException

    from backend.api.auth import SignInRequest, signin

    try:
        signin(SignInRequest(master_id="public-or-guessed-id"))
    except HTTPException as error:
        assert error.status_code == 403
        assert error.detail == "PASSWORD_SIGNIN_REQUIRED"
    else:
        raise AssertionError("Master-ID-only sign-in must be rejected")
