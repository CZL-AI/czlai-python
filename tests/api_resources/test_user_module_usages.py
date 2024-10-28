# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai
from czlai.types import (
    UserModuleUsageGetAddWecomeBonusResponse,
    UserModuleUsageGetWechatMiniQrcodeResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserModuleUsages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_checkin(self, client: Czlai) -> None:
        user_module_usage = client.user_module_usages.checkin()
        assert user_module_usage is None

    @parametrize
    def test_raw_response_checkin(self, client: Czlai) -> None:
        response = client.user_module_usages.with_raw_response.checkin()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_module_usage = response.parse()
        assert user_module_usage is None

    @parametrize
    def test_streaming_response_checkin(self, client: Czlai) -> None:
        with client.user_module_usages.with_streaming_response.checkin() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_module_usage = response.parse()
            assert user_module_usage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_add_wecome_bonus(self, client: Czlai) -> None:
        user_module_usage = client.user_module_usages.get_add_wecome_bonus()
        assert_matches_type(UserModuleUsageGetAddWecomeBonusResponse, user_module_usage, path=["response"])

    @parametrize
    def test_method_get_add_wecome_bonus_with_all_params(self, client: Czlai) -> None:
        user_module_usage = client.user_module_usages.get_add_wecome_bonus(
            module_type=0,
        )
        assert_matches_type(UserModuleUsageGetAddWecomeBonusResponse, user_module_usage, path=["response"])

    @parametrize
    def test_raw_response_get_add_wecome_bonus(self, client: Czlai) -> None:
        response = client.user_module_usages.with_raw_response.get_add_wecome_bonus()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_module_usage = response.parse()
        assert_matches_type(UserModuleUsageGetAddWecomeBonusResponse, user_module_usage, path=["response"])

    @parametrize
    def test_streaming_response_get_add_wecome_bonus(self, client: Czlai) -> None:
        with client.user_module_usages.with_streaming_response.get_add_wecome_bonus() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_module_usage = response.parse()
            assert_matches_type(UserModuleUsageGetAddWecomeBonusResponse, user_module_usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_wechat_mini_qrcode(self, client: Czlai) -> None:
        user_module_usage = client.user_module_usages.get_wechat_mini_qrcode()
        assert_matches_type(UserModuleUsageGetWechatMiniQrcodeResponse, user_module_usage, path=["response"])

    @parametrize
    def test_raw_response_get_wechat_mini_qrcode(self, client: Czlai) -> None:
        response = client.user_module_usages.with_raw_response.get_wechat_mini_qrcode()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_module_usage = response.parse()
        assert_matches_type(UserModuleUsageGetWechatMiniQrcodeResponse, user_module_usage, path=["response"])

    @parametrize
    def test_streaming_response_get_wechat_mini_qrcode(self, client: Czlai) -> None:
        with client.user_module_usages.with_streaming_response.get_wechat_mini_qrcode() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_module_usage = response.parse()
            assert_matches_type(UserModuleUsageGetWechatMiniQrcodeResponse, user_module_usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUserModuleUsages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_checkin(self, async_client: AsyncCzlai) -> None:
        user_module_usage = await async_client.user_module_usages.checkin()
        assert user_module_usage is None

    @parametrize
    async def test_raw_response_checkin(self, async_client: AsyncCzlai) -> None:
        response = await async_client.user_module_usages.with_raw_response.checkin()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_module_usage = await response.parse()
        assert user_module_usage is None

    @parametrize
    async def test_streaming_response_checkin(self, async_client: AsyncCzlai) -> None:
        async with async_client.user_module_usages.with_streaming_response.checkin() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_module_usage = await response.parse()
            assert user_module_usage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_add_wecome_bonus(self, async_client: AsyncCzlai) -> None:
        user_module_usage = await async_client.user_module_usages.get_add_wecome_bonus()
        assert_matches_type(UserModuleUsageGetAddWecomeBonusResponse, user_module_usage, path=["response"])

    @parametrize
    async def test_method_get_add_wecome_bonus_with_all_params(self, async_client: AsyncCzlai) -> None:
        user_module_usage = await async_client.user_module_usages.get_add_wecome_bonus(
            module_type=0,
        )
        assert_matches_type(UserModuleUsageGetAddWecomeBonusResponse, user_module_usage, path=["response"])

    @parametrize
    async def test_raw_response_get_add_wecome_bonus(self, async_client: AsyncCzlai) -> None:
        response = await async_client.user_module_usages.with_raw_response.get_add_wecome_bonus()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_module_usage = await response.parse()
        assert_matches_type(UserModuleUsageGetAddWecomeBonusResponse, user_module_usage, path=["response"])

    @parametrize
    async def test_streaming_response_get_add_wecome_bonus(self, async_client: AsyncCzlai) -> None:
        async with async_client.user_module_usages.with_streaming_response.get_add_wecome_bonus() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_module_usage = await response.parse()
            assert_matches_type(UserModuleUsageGetAddWecomeBonusResponse, user_module_usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_wechat_mini_qrcode(self, async_client: AsyncCzlai) -> None:
        user_module_usage = await async_client.user_module_usages.get_wechat_mini_qrcode()
        assert_matches_type(UserModuleUsageGetWechatMiniQrcodeResponse, user_module_usage, path=["response"])

    @parametrize
    async def test_raw_response_get_wechat_mini_qrcode(self, async_client: AsyncCzlai) -> None:
        response = await async_client.user_module_usages.with_raw_response.get_wechat_mini_qrcode()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_module_usage = await response.parse()
        assert_matches_type(UserModuleUsageGetWechatMiniQrcodeResponse, user_module_usage, path=["response"])

    @parametrize
    async def test_streaming_response_get_wechat_mini_qrcode(self, async_client: AsyncCzlai) -> None:
        async with async_client.user_module_usages.with_streaming_response.get_wechat_mini_qrcode() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_module_usage = await response.parse()
            assert_matches_type(UserModuleUsageGetWechatMiniQrcodeResponse, user_module_usage, path=["response"])

        assert cast(Any, response.is_closed) is True
