# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["MedicalRecordCreateListParams"]


class MedicalRecordCreateListParams(TypedDict, total=False):
    limit: int
    """每页数量"""

    module_type: Iterable[int]

    page: int
    """页码"""

    pet_profile_id: Iterable[int]
    """宠物档案 id"""
