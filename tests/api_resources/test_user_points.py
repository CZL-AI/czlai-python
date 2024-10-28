# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai
from czlai.types import UserPointRetrieveResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserPoints:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Czlai) -> None:
        user_point = client.user_points.retrieve()
        assert_matches_type(UserPointRetrieveResponse, user_point, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Czlai) -> None:
        response = client.user_points.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_point = response.parse()
        assert_matches_type(UserPointRetrieveResponse, user_point, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Czlai) -> None:
        with client.user_points.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_point = response.parse()
            assert_matches_type(UserPointRetrieveResponse, user_point, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cost_report(self, client: Czlai) -> None:
        user_point = client.user_points.cost_report()
        assert user_point is None

    @parametrize
    def test_method_cost_report_with_all_params(self, client: Czlai) -> None:
        user_point = client.user_points.cost_report(
            item_key="item_key",
            medical_record_id=0,
        )
        assert user_point is None

    @parametrize
    def test_raw_response_cost_report(self, client: Czlai) -> None:
        response = client.user_points.with_raw_response.cost_report()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_point = response.parse()
        assert user_point is None

    @parametrize
    def test_streaming_response_cost_report(self, client: Czlai) -> None:
        with client.user_points.with_streaming_response.cost_report() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_point = response.parse()
            assert user_point is None

        assert cast(Any, response.is_closed) is True


class TestAsyncUserPoints:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCzlai) -> None:
        user_point = await async_client.user_points.retrieve()
        assert_matches_type(UserPointRetrieveResponse, user_point, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCzlai) -> None:
        response = await async_client.user_points.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_point = await response.parse()
        assert_matches_type(UserPointRetrieveResponse, user_point, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCzlai) -> None:
        async with async_client.user_points.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_point = await response.parse()
            assert_matches_type(UserPointRetrieveResponse, user_point, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cost_report(self, async_client: AsyncCzlai) -> None:
        user_point = await async_client.user_points.cost_report()
        assert user_point is None

    @parametrize
    async def test_method_cost_report_with_all_params(self, async_client: AsyncCzlai) -> None:
        user_point = await async_client.user_points.cost_report(
            item_key="item_key",
            medical_record_id=0,
        )
        assert user_point is None

    @parametrize
    async def test_raw_response_cost_report(self, async_client: AsyncCzlai) -> None:
        response = await async_client.user_points.with_raw_response.cost_report()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_point = await response.parse()
        assert user_point is None

    @parametrize
    async def test_streaming_response_cost_report(self, async_client: AsyncCzlai) -> None:
        async with async_client.user_points.with_streaming_response.cost_report() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_point = await response.parse()
            assert user_point is None

        assert cast(Any, response.is_closed) is True
