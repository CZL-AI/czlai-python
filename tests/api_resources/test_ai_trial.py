# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAITrial:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_answer(self, client: Czlai) -> None:
        ai_trial = client.ai_trial.answer()
        assert_matches_type(str, ai_trial, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_answer_with_all_params(self, client: Czlai) -> None:
        ai_trial = client.ai_trial.answer(
            service_type=0,
            session_id="session_id",
            user_input="user_input",
        )
        assert_matches_type(str, ai_trial, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_answer(self, client: Czlai) -> None:
        response = client.ai_trial.with_raw_response.answer()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_trial = response.parse()
        assert_matches_type(str, ai_trial, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_answer(self, client: Czlai) -> None:
        with client.ai_trial.with_streaming_response.answer() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_trial = response.parse()
            assert_matches_type(str, ai_trial, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_history(self, client: Czlai) -> None:
        ai_trial = client.ai_trial.history(
            content="content",
            role="role",
            session_id="session_id",
        )
        assert ai_trial is None

    @parametrize
    def test_method_history_with_all_params(self, client: Czlai) -> None:
        ai_trial = client.ai_trial.history(
            content="content",
            role="role",
            session_id="session_id",
            content_type=0,
            module_type=0,
            stage=0,
        )
        assert ai_trial is None

    @parametrize
    def test_raw_response_history(self, client: Czlai) -> None:
        response = client.ai_trial.with_raw_response.history(
            content="content",
            role="role",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_trial = response.parse()
        assert ai_trial is None

    @parametrize
    def test_streaming_response_history(self, client: Czlai) -> None:
        with client.ai_trial.with_streaming_response.history(
            content="content",
            role="role",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_trial = response.parse()
            assert ai_trial is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_relation(self, client: Czlai) -> None:
        ai_trial = client.ai_trial.relation()
        assert ai_trial is None

    @parametrize
    def test_method_relation_with_all_params(self, client: Czlai) -> None:
        ai_trial = client.ai_trial.relation(
            service_type=1,
            session_id="session_id",
        )
        assert ai_trial is None

    @parametrize
    def test_raw_response_relation(self, client: Czlai) -> None:
        response = client.ai_trial.with_raw_response.relation()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_trial = response.parse()
        assert ai_trial is None

    @parametrize
    def test_streaming_response_relation(self, client: Czlai) -> None:
        with client.ai_trial.with_streaming_response.relation() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_trial = response.parse()
            assert ai_trial is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_report(self, client: Czlai) -> None:
        ai_trial = client.ai_trial.report(
            service_type=0,
            session_id="session_id",
        )
        assert ai_trial is None

    @parametrize
    def test_raw_response_report(self, client: Czlai) -> None:
        response = client.ai_trial.with_raw_response.report(
            service_type=0,
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_trial = response.parse()
        assert ai_trial is None

    @parametrize
    def test_streaming_response_report(self, client: Czlai) -> None:
        with client.ai_trial.with_streaming_response.report(
            service_type=0,
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_trial = response.parse()
            assert ai_trial is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_session_start(self, client: Czlai) -> None:
        ai_trial = client.ai_trial.session_start()
        assert ai_trial is None

    @parametrize
    def test_method_session_start_with_all_params(self, client: Czlai) -> None:
        ai_trial = client.ai_trial.session_start(
            content="content",
            service_type=0,
        )
        assert ai_trial is None

    @parametrize
    def test_raw_response_session_start(self, client: Czlai) -> None:
        response = client.ai_trial.with_raw_response.session_start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_trial = response.parse()
        assert ai_trial is None

    @parametrize
    def test_streaming_response_session_start(self, client: Czlai) -> None:
        with client.ai_trial.with_streaming_response.session_start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_trial = response.parse()
            assert ai_trial is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_summary(self, client: Czlai) -> None:
        ai_trial = client.ai_trial.summary()
        assert ai_trial is None

    @parametrize
    def test_method_summary_with_all_params(self, client: Czlai) -> None:
        ai_trial = client.ai_trial.summary(
            service_type=0,
            session_id="session_id",
        )
        assert ai_trial is None

    @parametrize
    def test_raw_response_summary(self, client: Czlai) -> None:
        response = client.ai_trial.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_trial = response.parse()
        assert ai_trial is None

    @parametrize
    def test_streaming_response_summary(self, client: Czlai) -> None:
        with client.ai_trial.with_streaming_response.summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_trial = response.parse()
            assert ai_trial is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAITrial:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_answer(self, async_client: AsyncCzlai) -> None:
        ai_trial = await async_client.ai_trial.answer()
        assert_matches_type(str, ai_trial, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_answer_with_all_params(self, async_client: AsyncCzlai) -> None:
        ai_trial = await async_client.ai_trial.answer(
            service_type=0,
            session_id="session_id",
            user_input="user_input",
        )
        assert_matches_type(str, ai_trial, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_answer(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_trial.with_raw_response.answer()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_trial = await response.parse()
        assert_matches_type(str, ai_trial, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_answer(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_trial.with_streaming_response.answer() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_trial = await response.parse()
            assert_matches_type(str, ai_trial, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_history(self, async_client: AsyncCzlai) -> None:
        ai_trial = await async_client.ai_trial.history(
            content="content",
            role="role",
            session_id="session_id",
        )
        assert ai_trial is None

    @parametrize
    async def test_method_history_with_all_params(self, async_client: AsyncCzlai) -> None:
        ai_trial = await async_client.ai_trial.history(
            content="content",
            role="role",
            session_id="session_id",
            content_type=0,
            module_type=0,
            stage=0,
        )
        assert ai_trial is None

    @parametrize
    async def test_raw_response_history(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_trial.with_raw_response.history(
            content="content",
            role="role",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_trial = await response.parse()
        assert ai_trial is None

    @parametrize
    async def test_streaming_response_history(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_trial.with_streaming_response.history(
            content="content",
            role="role",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_trial = await response.parse()
            assert ai_trial is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_relation(self, async_client: AsyncCzlai) -> None:
        ai_trial = await async_client.ai_trial.relation()
        assert ai_trial is None

    @parametrize
    async def test_method_relation_with_all_params(self, async_client: AsyncCzlai) -> None:
        ai_trial = await async_client.ai_trial.relation(
            service_type=1,
            session_id="session_id",
        )
        assert ai_trial is None

    @parametrize
    async def test_raw_response_relation(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_trial.with_raw_response.relation()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_trial = await response.parse()
        assert ai_trial is None

    @parametrize
    async def test_streaming_response_relation(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_trial.with_streaming_response.relation() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_trial = await response.parse()
            assert ai_trial is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_report(self, async_client: AsyncCzlai) -> None:
        ai_trial = await async_client.ai_trial.report(
            service_type=0,
            session_id="session_id",
        )
        assert ai_trial is None

    @parametrize
    async def test_raw_response_report(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_trial.with_raw_response.report(
            service_type=0,
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_trial = await response.parse()
        assert ai_trial is None

    @parametrize
    async def test_streaming_response_report(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_trial.with_streaming_response.report(
            service_type=0,
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_trial = await response.parse()
            assert ai_trial is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_session_start(self, async_client: AsyncCzlai) -> None:
        ai_trial = await async_client.ai_trial.session_start()
        assert ai_trial is None

    @parametrize
    async def test_method_session_start_with_all_params(self, async_client: AsyncCzlai) -> None:
        ai_trial = await async_client.ai_trial.session_start(
            content="content",
            service_type=0,
        )
        assert ai_trial is None

    @parametrize
    async def test_raw_response_session_start(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_trial.with_raw_response.session_start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_trial = await response.parse()
        assert ai_trial is None

    @parametrize
    async def test_streaming_response_session_start(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_trial.with_streaming_response.session_start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_trial = await response.parse()
            assert ai_trial is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_summary(self, async_client: AsyncCzlai) -> None:
        ai_trial = await async_client.ai_trial.summary()
        assert ai_trial is None

    @parametrize
    async def test_method_summary_with_all_params(self, async_client: AsyncCzlai) -> None:
        ai_trial = await async_client.ai_trial.summary(
            service_type=0,
            session_id="session_id",
        )
        assert ai_trial is None

    @parametrize
    async def test_raw_response_summary(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_trial.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_trial = await response.parse()
        assert ai_trial is None

    @parametrize
    async def test_streaming_response_summary(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_trial.with_streaming_response.summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_trial = await response.parse()
            assert ai_trial is None

        assert cast(Any, response.is_closed) is True
