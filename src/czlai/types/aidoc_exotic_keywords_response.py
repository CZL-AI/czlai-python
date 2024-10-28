# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AidocExoticKeywordsResponse", "Data"]


class Data(BaseModel):
    keywords: Optional[str] = None
    """关键词"""

    unit: Optional[str] = None
    """科室"""


class AidocExoticKeywordsResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    success: Optional[bool] = None
