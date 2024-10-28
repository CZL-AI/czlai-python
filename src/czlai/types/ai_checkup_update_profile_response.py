# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AICheckupUpdateProfileResponse"]


class AICheckupUpdateProfileResponse(BaseModel):
    data: Optional[object] = None

    message: Optional[str] = None

    success: Optional[bool] = None
