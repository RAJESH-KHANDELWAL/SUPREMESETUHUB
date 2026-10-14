
"""User API routes for MAIN-BASE-FOUNDATION."""

from __future__ import annotations

import sqlite3
from typing import Optional

from fastapi import APIRouter, HTTPException

from backend.users.controller import UserController
from backend.schemas.user import PasswordVerifyRequest, UserCreateRequest, UserUpdateRequest


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

controller = UserController()


@router.get("/")
def get_users():
    users = controller.list()

    return {
        "message": "Users retrieved successfully",
        "data": [user.to_dict() for user in users],
    }


@router.get("/search")
def search_user(username: str):
    user = controller.search(username)

    return {
        "message": "User found" if user else "User not found",
        "data": user.to_dict() if user else None,
    }


@router.post("/signup", status_code=201)
@router.post("/register", status_code=201, include_in_schema=False)
def signup_user(payload: UserCreateRequest):
    """Sign up for an account using full name, Gmail, and password."""

    try:
        user = controller.signup(
            full_name=payload.full_name,
            email=str(payload.email),
            password=payload.password,
        )

        return {
            "message": (
                "Sign-up successful. "
                "Email verification is not yet enabled."
            ),
            "data": user.to_dict(),
        }

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    except sqlite3.IntegrityError as exc:
        raise HTTPException(
            status_code=409,
            detail="Account already exists or a unique field conflicts.",
        ) from exc


@router.post("/")
def create_user(payload: UserCreateRequest):
    """Compatibility endpoint for account creation."""
    return signup_user(payload)


@router.post("/verify-password")
def verify_password(payload: PasswordVerifyRequest):
    authenticated = controller.verify_password(
        payload.username,
        payload.password,
    )

    return {
        "authenticated": authenticated,
        "username": payload.username,
    }


@router.get("/{user_id}")
def get_user(user_id: str):
    user = controller.get(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="USER_NOT_FOUND",
        )

    return {
        "message": "User retrieved successfully",
        "data": user.to_dict(),
    }


@router.put("/{user_id}")
def update_user(
    user_id: str,
    payload: UserUpdateRequest,
):
    try:
        user = controller.update(
            user_id=user_id,
            full_name=payload.full_name,
            username=payload.username,
            email=str(payload.email) if payload.email else None,
            phone=payload.phone,
            phone_no=payload.phone_no,
            mobile_no=payload.mobile_no,
            whatsapp_no=payload.whatsapp_no,
            password=payload.password,
            role=payload.role,
            status=payload.status,
        )

        if user is None:
            raise HTTPException(
                status_code=404,
                detail="USER_NOT_FOUND",
            )

        return {
            "message": "User updated successfully",
            "data": user.to_dict(),
        }

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    except sqlite3.IntegrityError as exc:
        raise HTTPException(
            status_code=409,
            detail="Username or email already exists.",
        ) from exc


@router.delete("/{user_id}")
def delete_user(user_id: str):
    deleted = controller.delete(user_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="USER_NOT_FOUND",
        )

    return {
        "message": "User deleted successfully",
        "data": {
            "user_id": user_id,
            "deleted": True,
        },
    }
