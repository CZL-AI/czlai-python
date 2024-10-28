# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAipics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_summary(self, client: Czlai) -> None:
        aipic = client.aipics.summary()
        assert aipic is None

    @parametrize
    def test_method_summary_with_all_params(self, client: Czlai) -> None:
        aipic = client.aipics.summary(
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
            sub_module_type=0,
        )
        assert aipic is None

    @parametrize
    def test_raw_response_summary(self, client: Czlai) -> None:
        response = client.aipics.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic = response.parse()
        assert aipic is None

    @parametrize
    def test_streaming_response_summary(self, client: Czlai) -> None:
        with client.aipics.with_streaming_response.summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic = response.parse()
            assert aipic is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAipics:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_summary(self, async_client: AsyncCzlai) -> None:
        aipic = await async_client.aipics.summary()
        assert aipic is None

    @parametrize
    async def test_method_summary_with_all_params(self, async_client: AsyncCzlai) -> None:
        aipic = await async_client.aipics.summary(
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
            sub_module_type=0,
        )
        assert aipic is None

    @parametrize
    async def test_raw_response_summary(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aipics.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic = await response.parse()
        assert aipic is None

    @parametrize
    async def test_streaming_response_summary(self, async_client: AsyncCzlai) -> None:
        async with async_client.aipics.with_streaming_response.summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic = await response.parse()
            assert aipic is None

        assert cast(Any, response.is_closed) is True
