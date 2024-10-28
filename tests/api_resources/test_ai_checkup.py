# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai
from czlai.types import (
    AICheckupIsFirstResponse,
    AICheckupSessionStartResponse,
    AICheckupUpdateProfileResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAICheckup:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_is_first(self, client: Czlai) -> None:
        ai_checkup = client.ai_checkup.is_first(
            pet_profile_id=0,
        )
        assert_matches_type(AICheckupIsFirstResponse, ai_checkup, path=["response"])

    @parametrize
    def test_raw_response_is_first(self, client: Czlai) -> None:
        response = client.ai_checkup.with_raw_response.is_first(
            pet_profile_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_checkup = response.parse()
        assert_matches_type(AICheckupIsFirstResponse, ai_checkup, path=["response"])

    @parametrize
    def test_streaming_response_is_first(self, client: Czlai) -> None:
        with client.ai_checkup.with_streaming_response.is_first(
            pet_profile_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_checkup = response.parse()
            assert_matches_type(AICheckupIsFirstResponse, ai_checkup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_pic_result(self, client: Czlai) -> None:
        ai_checkup = client.ai_checkup.pic_result(
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
        )
        assert ai_checkup is None

    @parametrize
    def test_raw_response_pic_result(self, client: Czlai) -> None:
        response = client.ai_checkup.with_raw_response.pic_result(
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_checkup = response.parse()
        assert ai_checkup is None

    @parametrize
    def test_streaming_response_pic_result(self, client: Czlai) -> None:
        with client.ai_checkup.with_streaming_response.pic_result(
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_checkup = response.parse()
            assert ai_checkup is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_question(self, client: Czlai) -> None:
        ai_checkup = client.ai_checkup.question(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert ai_checkup is None

    @parametrize
    def test_raw_response_question(self, client: Czlai) -> None:
        response = client.ai_checkup.with_raw_response.question(
            pet_profile_id=0,
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_checkup = response.parse()
        assert ai_checkup is None

    @parametrize
    def test_streaming_response_question(self, client: Czlai) -> None:
        with client.ai_checkup.with_streaming_response.question(
            pet_profile_id=0,
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_checkup = response.parse()
            assert ai_checkup is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_question_result(self, client: Czlai) -> None:
        ai_checkup = client.ai_checkup.question_result(
            index=0,
            pet_profile_id=0,
            question_id="question_id",
            round="round",
            session_id="session_id",
        )
        assert ai_checkup is None

    @parametrize
    def test_raw_response_question_result(self, client: Czlai) -> None:
        response = client.ai_checkup.with_raw_response.question_result(
            index=0,
            pet_profile_id=0,
            question_id="question_id",
            round="round",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_checkup = response.parse()
        assert ai_checkup is None

    @parametrize
    def test_streaming_response_question_result(self, client: Czlai) -> None:
        with client.ai_checkup.with_streaming_response.question_result(
            index=0,
            pet_profile_id=0,
            question_id="question_id",
            round="round",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_checkup = response.parse()
            assert ai_checkup is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_report(self, client: Czlai) -> None:
        ai_checkup = client.ai_checkup.report(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert ai_checkup is None

    @parametrize
    def test_raw_response_report(self, client: Czlai) -> None:
        response = client.ai_checkup.with_raw_response.report(
            pet_profile_id=0,
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_checkup = response.parse()
        assert ai_checkup is None

    @parametrize
    def test_streaming_response_report(self, client: Czlai) -> None:
        with client.ai_checkup.with_streaming_response.report(
            pet_profile_id=0,
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_checkup = response.parse()
            assert ai_checkup is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_report_task(self, client: Czlai) -> None:
        ai_checkup = client.ai_checkup.report_task(
            session_id="session_id",
        )
        assert ai_checkup is None

    @parametrize
    def test_method_report_task_with_all_params(self, client: Czlai) -> None:
        ai_checkup = client.ai_checkup.report_task(
            session_id="session_id",
            img_url="img_url",
            report_type=0,
        )
        assert ai_checkup is None

    @parametrize
    def test_raw_response_report_task(self, client: Czlai) -> None:
        response = client.ai_checkup.with_raw_response.report_task(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_checkup = response.parse()
        assert ai_checkup is None

    @parametrize
    def test_streaming_response_report_task(self, client: Czlai) -> None:
        with client.ai_checkup.with_streaming_response.report_task(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_checkup = response.parse()
            assert ai_checkup is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_session_start(self, client: Czlai) -> None:
        ai_checkup = client.ai_checkup.session_start()
        assert_matches_type(AICheckupSessionStartResponse, ai_checkup, path=["response"])

    @parametrize
    def test_raw_response_session_start(self, client: Czlai) -> None:
        response = client.ai_checkup.with_raw_response.session_start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_checkup = response.parse()
        assert_matches_type(AICheckupSessionStartResponse, ai_checkup, path=["response"])

    @parametrize
    def test_streaming_response_session_start(self, client: Czlai) -> None:
        with client.ai_checkup.with_streaming_response.session_start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_checkup = response.parse()
            assert_matches_type(AICheckupSessionStartResponse, ai_checkup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_summary(self, client: Czlai) -> None:
        ai_checkup = client.ai_checkup.summary()
        assert_matches_type(str, ai_checkup, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_summary_with_all_params(self, client: Czlai) -> None:
        ai_checkup = client.ai_checkup.summary(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert_matches_type(str, ai_checkup, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_summary(self, client: Czlai) -> None:
        response = client.ai_checkup.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_checkup = response.parse()
        assert_matches_type(str, ai_checkup, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_summary(self, client: Czlai) -> None:
        with client.ai_checkup.with_streaming_response.summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_checkup = response.parse()
            assert_matches_type(str, ai_checkup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_profile(self, client: Czlai) -> None:
        ai_checkup = client.ai_checkup.update_profile()
        assert_matches_type(AICheckupUpdateProfileResponse, ai_checkup, path=["response"])

    @parametrize
    def test_method_update_profile_with_all_params(self, client: Czlai) -> None:
        ai_checkup = client.ai_checkup.update_profile(
            pet_profile_id=0,
            session_id="session_id",
            update_type=0,
        )
        assert_matches_type(AICheckupUpdateProfileResponse, ai_checkup, path=["response"])

    @parametrize
    def test_raw_response_update_profile(self, client: Czlai) -> None:
        response = client.ai_checkup.with_raw_response.update_profile()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_checkup = response.parse()
        assert_matches_type(AICheckupUpdateProfileResponse, ai_checkup, path=["response"])

    @parametrize
    def test_streaming_response_update_profile(self, client: Czlai) -> None:
        with client.ai_checkup.with_streaming_response.update_profile() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_checkup = response.parse()
            assert_matches_type(AICheckupUpdateProfileResponse, ai_checkup, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAICheckup:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_is_first(self, async_client: AsyncCzlai) -> None:
        ai_checkup = await async_client.ai_checkup.is_first(
            pet_profile_id=0,
        )
        assert_matches_type(AICheckupIsFirstResponse, ai_checkup, path=["response"])

    @parametrize
    async def test_raw_response_is_first(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_checkup.with_raw_response.is_first(
            pet_profile_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_checkup = await response.parse()
        assert_matches_type(AICheckupIsFirstResponse, ai_checkup, path=["response"])

    @parametrize
    async def test_streaming_response_is_first(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_checkup.with_streaming_response.is_first(
            pet_profile_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_checkup = await response.parse()
            assert_matches_type(AICheckupIsFirstResponse, ai_checkup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_pic_result(self, async_client: AsyncCzlai) -> None:
        ai_checkup = await async_client.ai_checkup.pic_result(
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
        )
        assert ai_checkup is None

    @parametrize
    async def test_raw_response_pic_result(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_checkup.with_raw_response.pic_result(
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_checkup = await response.parse()
        assert ai_checkup is None

    @parametrize
    async def test_streaming_response_pic_result(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_checkup.with_streaming_response.pic_result(
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_checkup = await response.parse()
            assert ai_checkup is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_question(self, async_client: AsyncCzlai) -> None:
        ai_checkup = await async_client.ai_checkup.question(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert ai_checkup is None

    @parametrize
    async def test_raw_response_question(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_checkup.with_raw_response.question(
            pet_profile_id=0,
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_checkup = await response.parse()
        assert ai_checkup is None

    @parametrize
    async def test_streaming_response_question(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_checkup.with_streaming_response.question(
            pet_profile_id=0,
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_checkup = await response.parse()
            assert ai_checkup is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_question_result(self, async_client: AsyncCzlai) -> None:
        ai_checkup = await async_client.ai_checkup.question_result(
            index=0,
            pet_profile_id=0,
            question_id="question_id",
            round="round",
            session_id="session_id",
        )
        assert ai_checkup is None

    @parametrize
    async def test_raw_response_question_result(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_checkup.with_raw_response.question_result(
            index=0,
            pet_profile_id=0,
            question_id="question_id",
            round="round",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_checkup = await response.parse()
        assert ai_checkup is None

    @parametrize
    async def test_streaming_response_question_result(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_checkup.with_streaming_response.question_result(
            index=0,
            pet_profile_id=0,
            question_id="question_id",
            round="round",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_checkup = await response.parse()
            assert ai_checkup is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_report(self, async_client: AsyncCzlai) -> None:
        ai_checkup = await async_client.ai_checkup.report(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert ai_checkup is None

    @parametrize
    async def test_raw_response_report(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_checkup.with_raw_response.report(
            pet_profile_id=0,
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_checkup = await response.parse()
        assert ai_checkup is None

    @parametrize
    async def test_streaming_response_report(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_checkup.with_streaming_response.report(
            pet_profile_id=0,
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_checkup = await response.parse()
            assert ai_checkup is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_report_task(self, async_client: AsyncCzlai) -> None:
        ai_checkup = await async_client.ai_checkup.report_task(
            session_id="session_id",
        )
        assert ai_checkup is None

    @parametrize
    async def test_method_report_task_with_all_params(self, async_client: AsyncCzlai) -> None:
        ai_checkup = await async_client.ai_checkup.report_task(
            session_id="session_id",
            img_url="img_url",
            report_type=0,
        )
        assert ai_checkup is None

    @parametrize
    async def test_raw_response_report_task(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_checkup.with_raw_response.report_task(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_checkup = await response.parse()
        assert ai_checkup is None

    @parametrize
    async def test_streaming_response_report_task(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_checkup.with_streaming_response.report_task(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_checkup = await response.parse()
            assert ai_checkup is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_session_start(self, async_client: AsyncCzlai) -> None:
        ai_checkup = await async_client.ai_checkup.session_start()
        assert_matches_type(AICheckupSessionStartResponse, ai_checkup, path=["response"])

    @parametrize
    async def test_raw_response_session_start(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_checkup.with_raw_response.session_start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_checkup = await response.parse()
        assert_matches_type(AICheckupSessionStartResponse, ai_checkup, path=["response"])

    @parametrize
    async def test_streaming_response_session_start(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_checkup.with_streaming_response.session_start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_checkup = await response.parse()
            assert_matches_type(AICheckupSessionStartResponse, ai_checkup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_summary(self, async_client: AsyncCzlai) -> None:
        ai_checkup = await async_client.ai_checkup.summary()
        assert_matches_type(str, ai_checkup, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_summary_with_all_params(self, async_client: AsyncCzlai) -> None:
        ai_checkup = await async_client.ai_checkup.summary(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert_matches_type(str, ai_checkup, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_summary(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_checkup.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_checkup = await response.parse()
        assert_matches_type(str, ai_checkup, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_summary(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_checkup.with_streaming_response.summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_checkup = await response.parse()
            assert_matches_type(str, ai_checkup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_profile(self, async_client: AsyncCzlai) -> None:
        ai_checkup = await async_client.ai_checkup.update_profile()
        assert_matches_type(AICheckupUpdateProfileResponse, ai_checkup, path=["response"])

    @parametrize
    async def test_method_update_profile_with_all_params(self, async_client: AsyncCzlai) -> None:
        ai_checkup = await async_client.ai_checkup.update_profile(
            pet_profile_id=0,
            session_id="session_id",
            update_type=0,
        )
        assert_matches_type(AICheckupUpdateProfileResponse, ai_checkup, path=["response"])

    @parametrize
    async def test_raw_response_update_profile(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_checkup.with_raw_response.update_profile()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_checkup = await response.parse()
        assert_matches_type(AICheckupUpdateProfileResponse, ai_checkup, path=["response"])

    @parametrize
    async def test_streaming_response_update_profile(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_checkup.with_streaming_response.update_profile() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_checkup = await response.parse()
            assert_matches_type(AICheckupUpdateProfileResponse, ai_checkup, path=["response"])

        assert cast(Any, response.is_closed) is True
