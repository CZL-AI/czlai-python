# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWhitelist:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_filtering_data(self, client: Czlai) -> None:
        whitelist = client.whitelist.filtering_data()
        assert whitelist is None

    @parametrize
    def test_method_filtering_data_with_all_params(self, client: Czlai) -> None:
        whitelist = client.whitelist.filtering_data(
            filtering_data="filtering_data",
        )
        assert whitelist is None

    @parametrize
    def test_raw_response_filtering_data(self, client: Czlai) -> None:
        response = client.whitelist.with_raw_response.filtering_data()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whitelist = response.parse()
        assert whitelist is None

    @parametrize
    def test_streaming_response_filtering_data(self, client: Czlai) -> None:
        with client.whitelist.with_streaming_response.filtering_data() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whitelist = response.parse()
            assert whitelist is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_save_data(self, client: Czlai) -> None:
        whitelist = client.whitelist.save_data()
        assert whitelist is None

    @parametrize
    def test_method_save_data_with_all_params(self, client: Czlai) -> None:
        whitelist = client.whitelist.save_data(
            save_data=["string", "string", "string"],
        )
        assert whitelist is None

    @parametrize
    def test_raw_response_save_data(self, client: Czlai) -> None:
        response = client.whitelist.with_raw_response.save_data()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whitelist = response.parse()
        assert whitelist is None

    @parametrize
    def test_streaming_response_save_data(self, client: Czlai) -> None:
        with client.whitelist.with_streaming_response.save_data() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whitelist = response.parse()
            assert whitelist is None

        assert cast(Any, response.is_closed) is True


class TestAsyncWhitelist:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_filtering_data(self, async_client: AsyncCzlai) -> None:
        whitelist = await async_client.whitelist.filtering_data()
        assert whitelist is None

    @parametrize
    async def test_method_filtering_data_with_all_params(self, async_client: AsyncCzlai) -> None:
        whitelist = await async_client.whitelist.filtering_data(
            filtering_data="filtering_data",
        )
        assert whitelist is None

    @parametrize
    async def test_raw_response_filtering_data(self, async_client: AsyncCzlai) -> None:
        response = await async_client.whitelist.with_raw_response.filtering_data()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whitelist = await response.parse()
        assert whitelist is None

    @parametrize
    async def test_streaming_response_filtering_data(self, async_client: AsyncCzlai) -> None:
        async with async_client.whitelist.with_streaming_response.filtering_data() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whitelist = await response.parse()
            assert whitelist is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_save_data(self, async_client: AsyncCzlai) -> None:
        whitelist = await async_client.whitelist.save_data()
        assert whitelist is None

    @parametrize
    async def test_method_save_data_with_all_params(self, async_client: AsyncCzlai) -> None:
        whitelist = await async_client.whitelist.save_data(
            save_data=["string", "string", "string"],
        )
        assert whitelist is None

    @parametrize
    async def test_raw_response_save_data(self, async_client: AsyncCzlai) -> None:
        response = await async_client.whitelist.with_raw_response.save_data()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whitelist = await response.parse()
        assert whitelist is None

    @parametrize
    async def test_streaming_response_save_data(self, async_client: AsyncCzlai) -> None:
        async with async_client.whitelist.with_streaming_response.save_data() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whitelist = await response.parse()
            assert whitelist is None

        assert cast(Any, response.is_closed) is True
