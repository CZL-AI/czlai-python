# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LoginResponse", "AuthTokens"]


class AuthTokens(BaseModel):
    access_token: str = FieldInfo(alias="accessToken")

    refresh_token: str = FieldInfo(alias="refreshToken")


class LoginResponse(BaseModel):
    auth_tokens: Optional[AuthTokens] = FieldInfo(alias="authTokens", default=None)

    message: Optional[str] = None

    success: Optional[bool] = None
