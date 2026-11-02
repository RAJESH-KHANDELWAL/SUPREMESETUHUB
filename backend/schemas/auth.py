"""Authentication request schemas.

A master ID is an identifier only; password sign-in remains mandatory.
"""

from pydantic import BaseModel, Field


class SignInRequest(BaseModel):
    username: str | None = Field(default=None, min_length=1, max_length=100)
    password: str | None = Field(default=None, min_length=1, max_length=128)
    master_id: str | None = Field(default=None, min_length=1, max_length=128)


class AuthenticateRequest(BaseModel):
    master_id: str = Field(min_length=1, max_length=128)


class TokenRequest(BaseModel):
    token: str | None = Field(default=None, min_length=1, max_length=4096)
    session_id: str | None = Field(default=None, min_length=1, max_length=256)


class SignOutRequest(TokenRequest):
    pass
