# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai
from czlai.types import PointTaskListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPointTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Czlai) -> None:
        point_task = client.point_tasks.list()
        assert_matches_type(PointTaskListResponse, point_task, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Czlai) -> None:
        response = client.point_tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        point_task = response.parse()
        assert_matches_type(PointTaskListResponse, point_task, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Czlai) -> None:
        with client.point_tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            point_task = response.parse()
            assert_matches_type(PointTaskListResponse, point_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_bonus(self, client: Czlai) -> None:
        point_task = client.point_tasks.bonus()
        assert point_task is None

    @parametrize
    def test_method_bonus_with_all_params(self, client: Czlai) -> None:
        point_task = client.point_tasks.bonus(
            task_id=0,
        )
        assert point_task is None

    @parametrize
    def test_raw_response_bonus(self, client: Czlai) -> None:
        response = client.point_tasks.with_raw_response.bonus()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        point_task = response.parse()
        assert point_task is None

    @parametrize
    def test_streaming_response_bonus(self, client: Czlai) -> None:
        with client.point_tasks.with_streaming_response.bonus() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            point_task = response.parse()
            assert point_task is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_confirm(self, client: Czlai) -> None:
        point_task = client.point_tasks.confirm()
        assert point_task is None

    @parametrize
    def test_method_confirm_with_all_params(self, client: Czlai) -> None:
        point_task = client.point_tasks.confirm(
            task_id=0,
        )
        assert point_task is None

    @parametrize
    def test_raw_response_confirm(self, client: Czlai) -> None:
        response = client.point_tasks.with_raw_response.confirm()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        point_task = response.parse()
        assert point_task is None

    @parametrize
    def test_streaming_response_confirm(self, client: Czlai) -> None:
        with client.point_tasks.with_streaming_response.confirm() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            point_task = response.parse()
            assert point_task is None

        assert cast(Any, response.is_closed) is True


class TestAsyncPointTasks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCzlai) -> None:
        point_task = await async_client.point_tasks.list()
        assert_matches_type(PointTaskListResponse, point_task, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCzlai) -> None:
        response = await async_client.point_tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        point_task = await response.parse()
        assert_matches_type(PointTaskListResponse, point_task, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCzlai) -> None:
        async with async_client.point_tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            point_task = await response.parse()
            assert_matches_type(PointTaskListResponse, point_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_bonus(self, async_client: AsyncCzlai) -> None:
        point_task = await async_client.point_tasks.bonus()
        assert point_task is None

    @parametrize
    async def test_method_bonus_with_all_params(self, async_client: AsyncCzlai) -> None:
        point_task = await async_client.point_tasks.bonus(
            task_id=0,
        )
        assert point_task is None

    @parametrize
    async def test_raw_response_bonus(self, async_client: AsyncCzlai) -> None:
        response = await async_client.point_tasks.with_raw_response.bonus()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        point_task = await response.parse()
        assert point_task is None

    @parametrize
    async def test_streaming_response_bonus(self, async_client: AsyncCzlai) -> None:
        async with async_client.point_tasks.with_streaming_response.bonus() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            point_task = await response.parse()
            assert point_task is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_confirm(self, async_client: AsyncCzlai) -> None:
        point_task = await async_client.point_tasks.confirm()
        assert point_task is None

    @parametrize
    async def test_method_confirm_with_all_params(self, async_client: AsyncCzlai) -> None:
        point_task = await async_client.point_tasks.confirm(
            task_id=0,
        )
        assert point_task is None

    @parametrize
    async def test_raw_response_confirm(self, async_client: AsyncCzlai) -> None:
        response = await async_client.point_tasks.with_raw_response.confirm()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        point_task = await response.parse()
        assert point_task is None

    @parametrize
    async def test_streaming_response_confirm(self, async_client: AsyncCzlai) -> None:
        async with async_client.point_tasks.with_streaming_response.confirm() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            point_task = await response.parse()
            assert point_task is None

        assert cast(Any, response.is_closed) is True
