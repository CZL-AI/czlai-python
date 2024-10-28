# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["PetProfile"]


class PetProfile(BaseModel):
    id: Optional[int] = None

    allergy_history: Optional[str] = None
    """过敏史"""

    avatar: Optional[str] = None
    """头像"""

    birthday: Optional[str] = None
    """生日"""

    created_at: Optional[datetime] = None

    disease_history: Optional[str] = None
    """疾病史"""

    family_history: Optional[str] = None
    """家族史"""

    gender: Optional[int] = None
    """性别 1-公 2-母"""

    is_neutered: Optional[int] = None
    """是否已绝育 0-否 1-是"""

    is_vaccination: Optional[int] = None
    """是否已接种疫苗 0-否 1-是"""

    name: Optional[str] = None
    """宠物名字"""

    pet_type: Optional[int] = None
    """宠物类型"""

    pet_variety: Optional[str] = None
    """宠物品种"""

    updated_at: Optional[datetime] = None

    vaccination_date: Optional[str] = None
    """疫苗时间"""

    weight: Optional[str] = None
    """重量"""
