# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pet_profile import PetProfile

__all__ = ["PetProfileListResponse"]


class PetProfileListResponse(BaseModel):
    data: Optional[List[PetProfile]] = None

    message: Optional[str] = None

    success: Optional[bool] = None
