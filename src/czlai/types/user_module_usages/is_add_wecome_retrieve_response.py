# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["IsAddWecomeRetrieveResponse", "Data"]


class Data(BaseModel):
    is_add_wecome: Optional[int] = None


class IsAddWecomeRetrieveResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    success: Optional[bool] = None
