# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AICheckupSessionStartResponse", "Data"]


class Data(BaseModel):
    session_id: Optional[str] = None


class AICheckupSessionStartResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    success: Optional[bool] = None
