# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserAdvices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Czlai) -> None:
        user_advice = client.user_advices.create(
            advice_type="advice_type",
            description="description",
            image_list=["string", "string", "string"],
        )
        assert user_advice is None

    @parametrize
    def test_raw_response_create(self, client: Czlai) -> None:
        response = client.user_advices.with_raw_response.create(
            advice_type="advice_type",
            description="description",
            image_list=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_advice = response.parse()
        assert user_advice is None

    @parametrize
    def test_streaming_response_create(self, client: Czlai) -> None:
        with client.user_advices.with_streaming_response.create(
            advice_type="advice_type",
            description="description",
            image_list=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_advice = response.parse()
            assert user_advice is None

        assert cast(Any, response.is_closed) is True


class TestAsyncUserAdvices:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCzlai) -> None:
        user_advice = await async_client.user_advices.create(
            advice_type="advice_type",
            description="description",
            image_list=["string", "string", "string"],
        )
        assert user_advice is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCzlai) -> None:
        response = await async_client.user_advices.with_raw_response.create(
            advice_type="advice_type",
            description="description",
            image_list=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_advice = await response.parse()
        assert user_advice is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCzlai) -> None:
        async with async_client.user_advices.with_streaming_response.create(
            advice_type="advice_type",
            description="description",
            image_list=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_advice = await response.parse()
            assert user_advice is None

        assert cast(Any, response.is_closed) is True
