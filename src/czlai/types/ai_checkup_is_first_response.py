# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AICheckupIsFirstResponse", "Data"]


class Data(BaseModel):
    is_first: Optional[bool] = None
    """是否为当月首检"""


class AICheckupIsFirstResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    success: Optional[bool] = None
