# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSummary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Czlai) -> None:
        summary = client.users.summary.create()
        assert summary is None

    @parametrize
    def test_method_create_with_all_params(self, client: Czlai) -> None:
        summary = client.users.summary.create(
            session_id="session_id",
        )
        assert summary is None

    @parametrize
    def test_raw_response_create(self, client: Czlai) -> None:
        response = client.users.summary.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert summary is None

    @parametrize
    def test_streaming_response_create(self, client: Czlai) -> None:
        with client.users.summary.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert summary is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSummary:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCzlai) -> None:
        summary = await async_client.users.summary.create()
        assert summary is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCzlai) -> None:
        summary = await async_client.users.summary.create(
            session_id="session_id",
        )
        assert summary is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCzlai) -> None:
        response = await async_client.users.summary.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert summary is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCzlai) -> None:
        async with async_client.users.summary.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert summary is None

        assert cast(Any, response.is_closed) is True
