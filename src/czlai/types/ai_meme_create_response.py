# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .ai_meme import AIMeme
from .._models import BaseModel

__all__ = ["AIMemeCreateResponse"]


class AIMemeCreateResponse(BaseModel):
    data: Optional[AIMeme] = None

    message: Optional[str] = None

    success: Optional[bool] = None
