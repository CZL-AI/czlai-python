# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai
from czlai.types import LoginResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogins:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_sms(self, client: Czlai) -> None:
        login = client.logins.sms(
            code="123456",
            phone="phone",
        )
        assert_matches_type(LoginResponse, login, path=["response"])

    @parametrize
    def test_method_sms_with_all_params(self, client: Czlai) -> None:
        login = client.logins.sms(
            code="123456",
            phone="phone",
            login_from=0,
        )
        assert_matches_type(LoginResponse, login, path=["response"])

    @parametrize
    def test_raw_response_sms(self, client: Czlai) -> None:
        response = client.logins.with_raw_response.sms(
            code="123456",
            phone="phone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = response.parse()
        assert_matches_type(LoginResponse, login, path=["response"])

    @parametrize
    def test_streaming_response_sms(self, client: Czlai) -> None:
        with client.logins.with_streaming_response.sms(
            code="123456",
            phone="phone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = response.parse()
            assert_matches_type(LoginResponse, login, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_wechat(self, client: Czlai) -> None:
        login = client.logins.wechat(
            wechat_code="wechat_code",
        )
        assert login is None

    @parametrize
    def test_method_wechat_with_all_params(self, client: Czlai) -> None:
        login = client.logins.wechat(
            wechat_code="wechat_code",
            encrypted_data="encryptedData",
            iv="iv",
            module_type=0,
            phone_number="phone_number",
            spread_id=0,
        )
        assert login is None

    @parametrize
    def test_raw_response_wechat(self, client: Czlai) -> None:
        response = client.logins.with_raw_response.wechat(
            wechat_code="wechat_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = response.parse()
        assert login is None

    @parametrize
    def test_streaming_response_wechat(self, client: Czlai) -> None:
        with client.logins.with_streaming_response.wechat(
            wechat_code="wechat_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = response.parse()
            assert login is None

        assert cast(Any, response.is_closed) is True


class TestAsyncLogins:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_sms(self, async_client: AsyncCzlai) -> None:
        login = await async_client.logins.sms(
            code="123456",
            phone="phone",
        )
        assert_matches_type(LoginResponse, login, path=["response"])

    @parametrize
    async def test_method_sms_with_all_params(self, async_client: AsyncCzlai) -> None:
        login = await async_client.logins.sms(
            code="123456",
            phone="phone",
            login_from=0,
        )
        assert_matches_type(LoginResponse, login, path=["response"])

    @parametrize
    async def test_raw_response_sms(self, async_client: AsyncCzlai) -> None:
        response = await async_client.logins.with_raw_response.sms(
            code="123456",
            phone="phone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = await response.parse()
        assert_matches_type(LoginResponse, login, path=["response"])

    @parametrize
    async def test_streaming_response_sms(self, async_client: AsyncCzlai) -> None:
        async with async_client.logins.with_streaming_response.sms(
            code="123456",
            phone="phone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = await response.parse()
            assert_matches_type(LoginResponse, login, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_wechat(self, async_client: AsyncCzlai) -> None:
        login = await async_client.logins.wechat(
            wechat_code="wechat_code",
        )
        assert login is None

    @parametrize
    async def test_method_wechat_with_all_params(self, async_client: AsyncCzlai) -> None:
        login = await async_client.logins.wechat(
            wechat_code="wechat_code",
            encrypted_data="encryptedData",
            iv="iv",
            module_type=0,
            phone_number="phone_number",
            spread_id=0,
        )
        assert login is None

    @parametrize
    async def test_raw_response_wechat(self, async_client: AsyncCzlai) -> None:
        response = await async_client.logins.with_raw_response.wechat(
            wechat_code="wechat_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = await response.parse()
        assert login is None

    @parametrize
    async def test_streaming_response_wechat(self, async_client: AsyncCzlai) -> None:
        async with async_client.logins.with_streaming_response.wechat(
            wechat_code="wechat_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = await response.parse()
            assert login is None

        assert cast(Any, response.is_closed) is True
