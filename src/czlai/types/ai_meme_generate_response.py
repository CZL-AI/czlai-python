# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AIMemeGenerateResponse", "Data"]


class Data(BaseModel):
    meme_url: Optional[str] = None
    """表情包地址"""


class AIMemeGenerateResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    success: Optional[bool] = None
