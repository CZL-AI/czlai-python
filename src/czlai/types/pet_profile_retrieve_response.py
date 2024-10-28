# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .pet_profile import PetProfile

__all__ = ["PetProfileRetrieveResponse"]


class PetProfileRetrieveResponse(BaseModel):
    data: Optional[PetProfile] = None

    message: Optional[str] = None

    success: Optional[bool] = None
