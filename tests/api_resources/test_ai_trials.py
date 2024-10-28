# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAITrials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_options(self, client: Czlai) -> None:
        ai_trial = client.ai_trials.options()
        assert ai_trial is None

    @parametrize
    def test_method_options_with_all_params(self, client: Czlai) -> None:
        ai_trial = client.ai_trials.options(
            question="question",
            service_type=0,
            session_id="session_id",
        )
        assert ai_trial is None

    @parametrize
    def test_raw_response_options(self, client: Czlai) -> None:
        response = client.ai_trials.with_raw_response.options()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_trial = response.parse()
        assert ai_trial is None

    @parametrize
    def test_streaming_response_options(self, client: Czlai) -> None:
        with client.ai_trials.with_streaming_response.options() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_trial = response.parse()
            assert ai_trial is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_question(self, client: Czlai) -> None:
        ai_trial = client.ai_trials.question()
        assert ai_trial is None

    @parametrize
    def test_method_question_with_all_params(self, client: Czlai) -> None:
        ai_trial = client.ai_trials.question(
            service_type=0,
            session_id="session_id",
        )
        assert ai_trial is None

    @parametrize
    def test_raw_response_question(self, client: Czlai) -> None:
        response = client.ai_trials.with_raw_response.question()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_trial = response.parse()
        assert ai_trial is None

    @parametrize
    def test_streaming_response_question(self, client: Czlai) -> None:
        with client.ai_trials.with_streaming_response.question() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_trial = response.parse()
            assert ai_trial is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAITrials:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_options(self, async_client: AsyncCzlai) -> None:
        ai_trial = await async_client.ai_trials.options()
        assert ai_trial is None

    @parametrize
    async def test_method_options_with_all_params(self, async_client: AsyncCzlai) -> None:
        ai_trial = await async_client.ai_trials.options(
            question="question",
            service_type=0,
            session_id="session_id",
        )
        assert ai_trial is None

    @parametrize
    async def test_raw_response_options(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_trials.with_raw_response.options()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_trial = await response.parse()
        assert ai_trial is None

    @parametrize
    async def test_streaming_response_options(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_trials.with_streaming_response.options() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_trial = await response.parse()
            assert ai_trial is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_question(self, async_client: AsyncCzlai) -> None:
        ai_trial = await async_client.ai_trials.question()
        assert ai_trial is None

    @parametrize
    async def test_method_question_with_all_params(self, async_client: AsyncCzlai) -> None:
        ai_trial = await async_client.ai_trials.question(
            service_type=0,
            session_id="session_id",
        )
        assert ai_trial is None

    @parametrize
    async def test_raw_response_question(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_trials.with_raw_response.question()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_trial = await response.parse()
        assert ai_trial is None

    @parametrize
    async def test_streaming_response_question(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_trials.with_streaming_response.question() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_trial = await response.parse()
            assert ai_trial is None

        assert cast(Any, response.is_closed) is True
