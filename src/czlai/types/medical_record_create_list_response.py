# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .medical_record import MedicalRecord

__all__ = ["MedicalRecordCreateListResponse"]


class MedicalRecordCreateListResponse(BaseModel):
    data: Optional[List[MedicalRecord]] = None

    message: Optional[str] = None

    success: Optional[bool] = None
