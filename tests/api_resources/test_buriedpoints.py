# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBuriedpoints:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Czlai) -> None:
        buriedpoint = client.buriedpoints.create(
            point="point",
        )
        assert buriedpoint is None

    @parametrize
    def test_method_create_with_all_params(self, client: Czlai) -> None:
        buriedpoint = client.buriedpoints.create(
            point="point",
            code="code",
        )
        assert buriedpoint is None

    @parametrize
    def test_raw_response_create(self, client: Czlai) -> None:
        response = client.buriedpoints.with_raw_response.create(
            point="point",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        buriedpoint = response.parse()
        assert buriedpoint is None

    @parametrize
    def test_streaming_response_create(self, client: Czlai) -> None:
        with client.buriedpoints.with_streaming_response.create(
            point="point",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            buriedpoint = response.parse()
            assert buriedpoint is None

        assert cast(Any, response.is_closed) is True


class TestAsyncBuriedpoints:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCzlai) -> None:
        buriedpoint = await async_client.buriedpoints.create(
            point="point",
        )
        assert buriedpoint is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCzlai) -> None:
        buriedpoint = await async_client.buriedpoints.create(
            point="point",
            code="code",
        )
        assert buriedpoint is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCzlai) -> None:
        response = await async_client.buriedpoints.with_raw_response.create(
            point="point",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        buriedpoint = await response.parse()
        assert buriedpoint is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCzlai) -> None:
        async with async_client.buriedpoints.with_streaming_response.create(
            point="point",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            buriedpoint = await response.parse()
            assert buriedpoint is None

        assert cast(Any, response.is_closed) is True
