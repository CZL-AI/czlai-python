# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserInfo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Czlai) -> None:
        user_info = client.users.user_info.retrieve(
            uuid="uuid",
        )
        assert user_info is None

    @parametrize
    def test_raw_response_retrieve(self, client: Czlai) -> None:
        response = client.users.user_info.with_raw_response.retrieve(
            uuid="uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_info = response.parse()
        assert user_info is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Czlai) -> None:
        with client.users.user_info.with_streaming_response.retrieve(
            uuid="uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_info = response.parse()
            assert user_info is None

        assert cast(Any, response.is_closed) is True


class TestAsyncUserInfo:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCzlai) -> None:
        user_info = await async_client.users.user_info.retrieve(
            uuid="uuid",
        )
        assert user_info is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCzlai) -> None:
        response = await async_client.users.user_info.with_raw_response.retrieve(
            uuid="uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_info = await response.parse()
        assert user_info is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCzlai) -> None:
        async with async_client.users.user_info.with_streaming_response.retrieve(
            uuid="uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_info = await response.parse()
            assert user_info is None

        assert cast(Any, response.is_closed) is True
