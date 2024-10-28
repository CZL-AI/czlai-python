# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PetProfileCreateParams"]


class PetProfileCreateParams(TypedDict, total=False):
    allergy_history: Optional[str]
    """过敏史"""

    avatar: Optional[str]
    """头像"""

    birthday: str
    """生日"""

    disease_history: Optional[str]
    """疾病史"""

    family_history: Optional[str]
    """家族史"""

    gender: int
    """性别 1-公 2-母"""

    is_neutered: Optional[int]
    """是否已绝育 0-否 1-是"""

    is_vaccination: int
    """是否已接种疫苗 0-否 1-是"""

    name: str
    """宠物名字"""

    pet_type: int
    """宠物类型"""

    pet_variety: Optional[str]
    """宠物品种"""

    vaccination_date: Optional[str]
    """疫苗时间"""

    weight: Optional[str]
    """重量"""
