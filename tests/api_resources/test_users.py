# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_chat_v(self, client: Czlai) -> None:
        user = client.users.chat_v()
        assert user is None

    @parametrize
    def test_method_chat_v_with_all_params(self, client: Czlai) -> None:
        user = client.users.chat_v(
            content="content",
            session_id="session_id",
        )
        assert user is None

    @parametrize
    def test_raw_response_chat_v(self, client: Czlai) -> None:
        response = client.users.with_raw_response.chat_v()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_chat_v(self, client: Czlai) -> None:
        with client.users.with_streaming_response.chat_v() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_logout(self, client: Czlai) -> None:
        user = client.users.logout()
        assert user is None

    @parametrize
    def test_raw_response_logout(self, client: Czlai) -> None:
        response = client.users.with_raw_response.logout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_logout(self, client: Czlai) -> None:
        with client.users.with_streaming_response.logout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_send_sms(self, client: Czlai) -> None:
        user = client.users.send_sms()
        assert user is None

    @parametrize
    def test_method_send_sms_with_all_params(self, client: Czlai) -> None:
        user = client.users.send_sms(
            phone="phone",
        )
        assert user is None

    @parametrize
    def test_raw_response_send_sms(self, client: Czlai) -> None:
        response = client.users.with_raw_response.send_sms()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_send_sms(self, client: Czlai) -> None:
        with client.users.with_streaming_response.send_sms() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_chat_v(self, async_client: AsyncCzlai) -> None:
        user = await async_client.users.chat_v()
        assert user is None

    @parametrize
    async def test_method_chat_v_with_all_params(self, async_client: AsyncCzlai) -> None:
        user = await async_client.users.chat_v(
            content="content",
            session_id="session_id",
        )
        assert user is None

    @parametrize
    async def test_raw_response_chat_v(self, async_client: AsyncCzlai) -> None:
        response = await async_client.users.with_raw_response.chat_v()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_chat_v(self, async_client: AsyncCzlai) -> None:
        async with async_client.users.with_streaming_response.chat_v() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_logout(self, async_client: AsyncCzlai) -> None:
        user = await async_client.users.logout()
        assert user is None

    @parametrize
    async def test_raw_response_logout(self, async_client: AsyncCzlai) -> None:
        response = await async_client.users.with_raw_response.logout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_logout(self, async_client: AsyncCzlai) -> None:
        async with async_client.users.with_streaming_response.logout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_send_sms(self, async_client: AsyncCzlai) -> None:
        user = await async_client.users.send_sms()
        assert user is None

    @parametrize
    async def test_method_send_sms_with_all_params(self, async_client: AsyncCzlai) -> None:
        user = await async_client.users.send_sms(
            phone="phone",
        )
        assert user is None

    @parametrize
    async def test_raw_response_send_sms(self, async_client: AsyncCzlai) -> None:
        response = await async_client.users.with_raw_response.send_sms()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_send_sms(self, async_client: AsyncCzlai) -> None:
        async with async_client.users.with_streaming_response.send_sms() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True
