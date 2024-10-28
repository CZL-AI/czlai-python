# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PetInfoRetrieveParams"]


class PetInfoRetrieveParams(TypedDict, total=False):
    pets_type: Required[Literal["dog", "cat"]]
    """dog cat"""

    is_sort: Literal[0, 1]
    """0-分组 1-不分组"""
