# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_put_evaluation(self, client: Czlai) -> None:
        evaluation = client.evaluation.put_evaluation(
            content="content",
            evaluation=0,
            session_id="session_id",
        )
        assert evaluation is None

    @parametrize
    def test_raw_response_put_evaluation(self, client: Czlai) -> None:
        response = client.evaluation.with_raw_response.put_evaluation(
            content="content",
            evaluation=0,
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = response.parse()
        assert evaluation is None

    @parametrize
    def test_streaming_response_put_evaluation(self, client: Czlai) -> None:
        with client.evaluation.with_streaming_response.put_evaluation(
            content="content",
            evaluation=0,
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = response.parse()
            assert evaluation is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEvaluation:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_put_evaluation(self, async_client: AsyncCzlai) -> None:
        evaluation = await async_client.evaluation.put_evaluation(
            content="content",
            evaluation=0,
            session_id="session_id",
        )
        assert evaluation is None

    @parametrize
    async def test_raw_response_put_evaluation(self, async_client: AsyncCzlai) -> None:
        response = await async_client.evaluation.with_raw_response.put_evaluation(
            content="content",
            evaluation=0,
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = await response.parse()
        assert evaluation is None

    @parametrize
    async def test_streaming_response_put_evaluation(self, async_client: AsyncCzlai) -> None:
        async with async_client.evaluation.with_streaming_response.put_evaluation(
            content="content",
            evaluation=0,
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = await response.parse()
            assert evaluation is None

        assert cast(Any, response.is_closed) is True
