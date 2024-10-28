# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessionRecords:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_history(self, client: Czlai) -> None:
        session_record = client.session_records.history(
            content="content",
            module_type=0,
            role="role",
            session_id="session_id",
        )
        assert session_record is None

    @parametrize
    def test_method_history_with_all_params(self, client: Czlai) -> None:
        session_record = client.session_records.history(
            content="content",
            module_type=0,
            role="role",
            session_id="session_id",
            content_type=0,
            stage=0,
        )
        assert session_record is None

    @parametrize
    def test_raw_response_history(self, client: Czlai) -> None:
        response = client.session_records.with_raw_response.history(
            content="content",
            module_type=0,
            role="role",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session_record = response.parse()
        assert session_record is None

    @parametrize
    def test_streaming_response_history(self, client: Czlai) -> None:
        with client.session_records.with_streaming_response.history(
            content="content",
            module_type=0,
            role="role",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session_record = response.parse()
            assert session_record is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSessionRecords:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_history(self, async_client: AsyncCzlai) -> None:
        session_record = await async_client.session_records.history(
            content="content",
            module_type=0,
            role="role",
            session_id="session_id",
        )
        assert session_record is None

    @parametrize
    async def test_method_history_with_all_params(self, async_client: AsyncCzlai) -> None:
        session_record = await async_client.session_records.history(
            content="content",
            module_type=0,
            role="role",
            session_id="session_id",
            content_type=0,
            stage=0,
        )
        assert session_record is None

    @parametrize
    async def test_raw_response_history(self, async_client: AsyncCzlai) -> None:
        response = await async_client.session_records.with_raw_response.history(
            content="content",
            module_type=0,
            role="role",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session_record = await response.parse()
        assert session_record is None

    @parametrize
    async def test_streaming_response_history(self, async_client: AsyncCzlai) -> None:
        async with async_client.session_records.with_streaming_response.history(
            content="content",
            module_type=0,
            role="role",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session_record = await response.parse()
            assert session_record is None

        assert cast(Any, response.is_closed) is True
