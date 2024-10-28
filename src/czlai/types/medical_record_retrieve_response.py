# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .medical_record import MedicalRecord

__all__ = ["MedicalRecordRetrieveResponse"]


class MedicalRecordRetrieveResponse(BaseModel):
    data: Optional[MedicalRecord] = None

    message: Optional[str] = None

    success: Optional[bool] = None
