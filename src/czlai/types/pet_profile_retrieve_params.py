# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PetProfileRetrieveParams"]


class PetProfileRetrieveParams(TypedDict, total=False):
    pet_profile_id: Required[int]
