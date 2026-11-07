"""Reusable request and response schemas for user accounts."""

from __future__ import annotations

import re
from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator


class UserCreateRequest(BaseModel):
    full_name: str = Field(min_length=1, max_length=120)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    confirm_password: str = Field(min_length=8, max_length=128)

    @field_validator("full_name")
    @classmethod
    def clean_full_name(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("FULL_NAME_REQUIRED")
        return value

    @field_validator("email")
    @classmethod
    def normalize_gmail(cls, value: EmailStr) -> str:
        email = str(value).strip().lower()
        if not re.fullmatch(r"[a-zA-Z0-9._%+-]+@gmail\.com", email):
            raise ValueError("VALID_GMAIL_ADDRESS_REQUIRED")
        return email

    @model_validator(mode="after")
    def passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("PASSWORDS_DO_NOT_MATCH")
        return self


class UserUpdateRequest(BaseModel):
    full_name: str | None = Field(default=None, min_length=1, max_length=120)
    username: str | None = Field(default=None, min_length=1, max_length=100)
    email: EmailStr | None = None
    phone: str | None = Field(default=None, max_length=32)
    phone_no: str | None = Field(default=None, max_length=32)
    mobile_no: str | None = Field(default=None, max_length=32)
    whatsapp_no: str | None = Field(default=None, max_length=32)
    password: str | None = Field(default=None, min_length=8, max_length=128)
    role: str | None = Field(default=None, max_length=32)
    status: str | None = Field(default=None, max_length=32)


class PasswordVerifyRequest(BaseModel):
    username: str = Field(min_length=1, max_length=100)
    password: str = Field(min_length=1, max_length=128)
