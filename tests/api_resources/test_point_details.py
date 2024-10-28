# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai
from czlai.types import PointDetailRetrieveResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPointDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Czlai) -> None:
        point_detail = client.point_details.retrieve()
        assert_matches_type(PointDetailRetrieveResponse, point_detail, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Czlai) -> None:
        point_detail = client.point_details.retrieve(
            is_add=0,
            limit=1,
            page=1,
        )
        assert_matches_type(PointDetailRetrieveResponse, point_detail, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Czlai) -> None:
        response = client.point_details.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        point_detail = response.parse()
        assert_matches_type(PointDetailRetrieveResponse, point_detail, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Czlai) -> None:
        with client.point_details.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            point_detail = response.parse()
            assert_matches_type(PointDetailRetrieveResponse, point_detail, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPointDetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCzlai) -> None:
        point_detail = await async_client.point_details.retrieve()
        assert_matches_type(PointDetailRetrieveResponse, point_detail, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncCzlai) -> None:
        point_detail = await async_client.point_details.retrieve(
            is_add=0,
            limit=1,
            page=1,
        )
        assert_matches_type(PointDetailRetrieveResponse, point_detail, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCzlai) -> None:
        response = await async_client.point_details.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        point_detail = await response.parse()
        assert_matches_type(PointDetailRetrieveResponse, point_detail, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCzlai) -> None:
        async with async_client.point_details.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            point_detail = await response.parse()
            assert_matches_type(PointDetailRetrieveResponse, point_detail, path=["response"])

        assert cast(Any, response.is_closed) is True
