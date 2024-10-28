# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .ai_meme import AIMeme
from .._models import BaseModel

__all__ = ["AIMemeRetrieveResponse"]


class AIMemeRetrieveResponse(BaseModel):
    data: Optional[List[AIMeme]] = None

    message: Optional[str] = None

    success: Optional[bool] = None
