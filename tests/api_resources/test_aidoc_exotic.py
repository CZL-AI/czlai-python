# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai
from czlai.types import (
    AidocExoticKeywordsResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAidocExotic:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_ask_continue(self, client: Czlai) -> None:
        aidoc_exotic = client.aidoc_exotic.ask_continue()
        assert_matches_type(str, aidoc_exotic, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_ask_continue_with_all_params(self, client: Czlai) -> None:
        aidoc_exotic = client.aidoc_exotic.ask_continue(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert_matches_type(str, aidoc_exotic, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_ask_continue(self, client: Czlai) -> None:
        response = client.aidoc_exotic.with_raw_response.ask_continue()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc_exotic = response.parse()
        assert_matches_type(str, aidoc_exotic, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_ask_continue(self, client: Czlai) -> None:
        with client.aidoc_exotic.with_streaming_response.ask_continue() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc_exotic = response.parse()
            assert_matches_type(str, aidoc_exotic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_if_need_image(self, client: Czlai) -> None:
        aidoc_exotic = client.aidoc_exotic.if_need_image()
        assert_matches_type(object, aidoc_exotic, path=["response"])

    @parametrize
    def test_method_if_need_image_with_all_params(self, client: Czlai) -> None:
        aidoc_exotic = client.aidoc_exotic.if_need_image(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert_matches_type(object, aidoc_exotic, path=["response"])

    @parametrize
    def test_raw_response_if_need_image(self, client: Czlai) -> None:
        response = client.aidoc_exotic.with_raw_response.if_need_image()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc_exotic = response.parse()
        assert_matches_type(object, aidoc_exotic, path=["response"])

    @parametrize
    def test_streaming_response_if_need_image(self, client: Czlai) -> None:
        with client.aidoc_exotic.with_streaming_response.if_need_image() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc_exotic = response.parse()
            assert_matches_type(object, aidoc_exotic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_keywords(self, client: Czlai) -> None:
        aidoc_exotic = client.aidoc_exotic.keywords()
        assert_matches_type(AidocExoticKeywordsResponse, aidoc_exotic, path=["response"])

    @parametrize
    def test_method_keywords_with_all_params(self, client: Czlai) -> None:
        aidoc_exotic = client.aidoc_exotic.keywords(
            content="content",
            pet_profile_id=0,
            session_id="session_id",
        )
        assert_matches_type(AidocExoticKeywordsResponse, aidoc_exotic, path=["response"])

    @parametrize
    def test_raw_response_keywords(self, client: Czlai) -> None:
        response = client.aidoc_exotic.with_raw_response.keywords()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc_exotic = response.parse()
        assert_matches_type(AidocExoticKeywordsResponse, aidoc_exotic, path=["response"])

    @parametrize
    def test_streaming_response_keywords(self, client: Czlai) -> None:
        with client.aidoc_exotic.with_streaming_response.keywords() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc_exotic = response.parse()
            assert_matches_type(AidocExoticKeywordsResponse, aidoc_exotic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_options(self, client: Czlai) -> None:
        aidoc_exotic = client.aidoc_exotic.options()
        assert_matches_type(str, aidoc_exotic, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_options_with_all_params(self, client: Czlai) -> None:
        aidoc_exotic = client.aidoc_exotic.options(
            pet_profile_id=0,
            question="question",
            session_id="session_id",
        )
        assert_matches_type(str, aidoc_exotic, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_options(self, client: Czlai) -> None:
        response = client.aidoc_exotic.with_raw_response.options()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc_exotic = response.parse()
        assert_matches_type(str, aidoc_exotic, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_options(self, client: Czlai) -> None:
        with client.aidoc_exotic.with_streaming_response.options() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc_exotic = response.parse()
            assert_matches_type(str, aidoc_exotic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_pic_result(self, client: Czlai) -> None:
        aidoc_exotic = client.aidoc_exotic.pic_result()
        assert aidoc_exotic is None

    @parametrize
    def test_method_pic_result_with_all_params(self, client: Czlai) -> None:
        aidoc_exotic = client.aidoc_exotic.pic_result(
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
        )
        assert aidoc_exotic is None

    @parametrize
    def test_raw_response_pic_result(self, client: Czlai) -> None:
        response = client.aidoc_exotic.with_raw_response.pic_result()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc_exotic = response.parse()
        assert aidoc_exotic is None

    @parametrize
    def test_streaming_response_pic_result(self, client: Czlai) -> None:
        with client.aidoc_exotic.with_streaming_response.pic_result() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc_exotic = response.parse()
            assert aidoc_exotic is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_question(self, client: Czlai) -> None:
        aidoc_exotic = client.aidoc_exotic.question()
        assert_matches_type(str, aidoc_exotic, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_question_with_all_params(self, client: Czlai) -> None:
        aidoc_exotic = client.aidoc_exotic.question(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert_matches_type(str, aidoc_exotic, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_question(self, client: Czlai) -> None:
        response = client.aidoc_exotic.with_raw_response.question()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc_exotic = response.parse()
        assert_matches_type(str, aidoc_exotic, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_question(self, client: Czlai) -> None:
        with client.aidoc_exotic.with_streaming_response.question() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc_exotic = response.parse()
            assert_matches_type(str, aidoc_exotic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_report(self, client: Czlai) -> None:
        aidoc_exotic = client.aidoc_exotic.report(
            session_id="session_id",
        )
        assert aidoc_exotic is None

    @parametrize
    def test_raw_response_report(self, client: Czlai) -> None:
        response = client.aidoc_exotic.with_raw_response.report(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc_exotic = response.parse()
        assert aidoc_exotic is None

    @parametrize
    def test_streaming_response_report(self, client: Czlai) -> None:
        with client.aidoc_exotic.with_streaming_response.report(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc_exotic = response.parse()
            assert aidoc_exotic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_report_task(self, client: Czlai) -> None:
        aidoc_exotic = client.aidoc_exotic.report_task(
            session_id="session_id",
        )
        assert aidoc_exotic is None

    @parametrize
    def test_method_report_task_with_all_params(self, client: Czlai) -> None:
        aidoc_exotic = client.aidoc_exotic.report_task(
            session_id="session_id",
            report_type=0,
        )
        assert aidoc_exotic is None

    @parametrize
    def test_raw_response_report_task(self, client: Czlai) -> None:
        response = client.aidoc_exotic.with_raw_response.report_task(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc_exotic = response.parse()
        assert aidoc_exotic is None

    @parametrize
    def test_streaming_response_report_task(self, client: Czlai) -> None:
        with client.aidoc_exotic.with_streaming_response.report_task(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc_exotic = response.parse()
            assert aidoc_exotic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_summarize(self, client: Czlai) -> None:
        aidoc_exotic = client.aidoc_exotic.summarize()
        assert aidoc_exotic is None

    @parametrize
    def test_method_summarize_with_all_params(self, client: Czlai) -> None:
        aidoc_exotic = client.aidoc_exotic.summarize(
            image_url="image_url",
            pet_profile_id=0,
            session_id="session_id",
        )
        assert aidoc_exotic is None

    @parametrize
    def test_raw_response_summarize(self, client: Czlai) -> None:
        response = client.aidoc_exotic.with_raw_response.summarize()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc_exotic = response.parse()
        assert aidoc_exotic is None

    @parametrize
    def test_streaming_response_summarize(self, client: Czlai) -> None:
        with client.aidoc_exotic.with_streaming_response.summarize() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc_exotic = response.parse()
            assert aidoc_exotic is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAidocExotic:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_ask_continue(self, async_client: AsyncCzlai) -> None:
        aidoc_exotic = await async_client.aidoc_exotic.ask_continue()
        assert_matches_type(str, aidoc_exotic, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_ask_continue_with_all_params(self, async_client: AsyncCzlai) -> None:
        aidoc_exotic = await async_client.aidoc_exotic.ask_continue(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert_matches_type(str, aidoc_exotic, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_ask_continue(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aidoc_exotic.with_raw_response.ask_continue()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc_exotic = await response.parse()
        assert_matches_type(str, aidoc_exotic, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_ask_continue(self, async_client: AsyncCzlai) -> None:
        async with async_client.aidoc_exotic.with_streaming_response.ask_continue() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc_exotic = await response.parse()
            assert_matches_type(str, aidoc_exotic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_if_need_image(self, async_client: AsyncCzlai) -> None:
        aidoc_exotic = await async_client.aidoc_exotic.if_need_image()
        assert_matches_type(object, aidoc_exotic, path=["response"])

    @parametrize
    async def test_method_if_need_image_with_all_params(self, async_client: AsyncCzlai) -> None:
        aidoc_exotic = await async_client.aidoc_exotic.if_need_image(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert_matches_type(object, aidoc_exotic, path=["response"])

    @parametrize
    async def test_raw_response_if_need_image(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aidoc_exotic.with_raw_response.if_need_image()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc_exotic = await response.parse()
        assert_matches_type(object, aidoc_exotic, path=["response"])

    @parametrize
    async def test_streaming_response_if_need_image(self, async_client: AsyncCzlai) -> None:
        async with async_client.aidoc_exotic.with_streaming_response.if_need_image() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc_exotic = await response.parse()
            assert_matches_type(object, aidoc_exotic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_keywords(self, async_client: AsyncCzlai) -> None:
        aidoc_exotic = await async_client.aidoc_exotic.keywords()
        assert_matches_type(AidocExoticKeywordsResponse, aidoc_exotic, path=["response"])

    @parametrize
    async def test_method_keywords_with_all_params(self, async_client: AsyncCzlai) -> None:
        aidoc_exotic = await async_client.aidoc_exotic.keywords(
            content="content",
            pet_profile_id=0,
            session_id="session_id",
        )
        assert_matches_type(AidocExoticKeywordsResponse, aidoc_exotic, path=["response"])

    @parametrize
    async def test_raw_response_keywords(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aidoc_exotic.with_raw_response.keywords()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc_exotic = await response.parse()
        assert_matches_type(AidocExoticKeywordsResponse, aidoc_exotic, path=["response"])

    @parametrize
    async def test_streaming_response_keywords(self, async_client: AsyncCzlai) -> None:
        async with async_client.aidoc_exotic.with_streaming_response.keywords() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc_exotic = await response.parse()
            assert_matches_type(AidocExoticKeywordsResponse, aidoc_exotic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_options(self, async_client: AsyncCzlai) -> None:
        aidoc_exotic = await async_client.aidoc_exotic.options()
        assert_matches_type(str, aidoc_exotic, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_options_with_all_params(self, async_client: AsyncCzlai) -> None:
        aidoc_exotic = await async_client.aidoc_exotic.options(
            pet_profile_id=0,
            question="question",
            session_id="session_id",
        )
        assert_matches_type(str, aidoc_exotic, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_options(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aidoc_exotic.with_raw_response.options()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc_exotic = await response.parse()
        assert_matches_type(str, aidoc_exotic, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_options(self, async_client: AsyncCzlai) -> None:
        async with async_client.aidoc_exotic.with_streaming_response.options() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc_exotic = await response.parse()
            assert_matches_type(str, aidoc_exotic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_pic_result(self, async_client: AsyncCzlai) -> None:
        aidoc_exotic = await async_client.aidoc_exotic.pic_result()
        assert aidoc_exotic is None

    @parametrize
    async def test_method_pic_result_with_all_params(self, async_client: AsyncCzlai) -> None:
        aidoc_exotic = await async_client.aidoc_exotic.pic_result(
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
        )
        assert aidoc_exotic is None

    @parametrize
    async def test_raw_response_pic_result(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aidoc_exotic.with_raw_response.pic_result()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc_exotic = await response.parse()
        assert aidoc_exotic is None

    @parametrize
    async def test_streaming_response_pic_result(self, async_client: AsyncCzlai) -> None:
        async with async_client.aidoc_exotic.with_streaming_response.pic_result() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc_exotic = await response.parse()
            assert aidoc_exotic is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_question(self, async_client: AsyncCzlai) -> None:
        aidoc_exotic = await async_client.aidoc_exotic.question()
        assert_matches_type(str, aidoc_exotic, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_question_with_all_params(self, async_client: AsyncCzlai) -> None:
        aidoc_exotic = await async_client.aidoc_exotic.question(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert_matches_type(str, aidoc_exotic, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_question(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aidoc_exotic.with_raw_response.question()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc_exotic = await response.parse()
        assert_matches_type(str, aidoc_exotic, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_question(self, async_client: AsyncCzlai) -> None:
        async with async_client.aidoc_exotic.with_streaming_response.question() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc_exotic = await response.parse()
            assert_matches_type(str, aidoc_exotic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_report(self, async_client: AsyncCzlai) -> None:
        aidoc_exotic = await async_client.aidoc_exotic.report(
            session_id="session_id",
        )
        assert aidoc_exotic is None

    @parametrize
    async def test_raw_response_report(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aidoc_exotic.with_raw_response.report(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc_exotic = await response.parse()
        assert aidoc_exotic is None

    @parametrize
    async def test_streaming_response_report(self, async_client: AsyncCzlai) -> None:
        async with async_client.aidoc_exotic.with_streaming_response.report(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc_exotic = await response.parse()
            assert aidoc_exotic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_report_task(self, async_client: AsyncCzlai) -> None:
        aidoc_exotic = await async_client.aidoc_exotic.report_task(
            session_id="session_id",
        )
        assert aidoc_exotic is None

    @parametrize
    async def test_method_report_task_with_all_params(self, async_client: AsyncCzlai) -> None:
        aidoc_exotic = await async_client.aidoc_exotic.report_task(
            session_id="session_id",
            report_type=0,
        )
        assert aidoc_exotic is None

    @parametrize
    async def test_raw_response_report_task(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aidoc_exotic.with_raw_response.report_task(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc_exotic = await response.parse()
        assert aidoc_exotic is None

    @parametrize
    async def test_streaming_response_report_task(self, async_client: AsyncCzlai) -> None:
        async with async_client.aidoc_exotic.with_streaming_response.report_task(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc_exotic = await response.parse()
            assert aidoc_exotic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_summarize(self, async_client: AsyncCzlai) -> None:
        aidoc_exotic = await async_client.aidoc_exotic.summarize()
        assert aidoc_exotic is None

    @parametrize
    async def test_method_summarize_with_all_params(self, async_client: AsyncCzlai) -> None:
        aidoc_exotic = await async_client.aidoc_exotic.summarize(
            image_url="image_url",
            pet_profile_id=0,
            session_id="session_id",
        )
        assert aidoc_exotic is None

    @parametrize
    async def test_raw_response_summarize(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aidoc_exotic.with_raw_response.summarize()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc_exotic = await response.parse()
        assert aidoc_exotic is None

    @parametrize
    async def test_streaming_response_summarize(self, async_client: AsyncCzlai) -> None:
        async with async_client.aidoc_exotic.with_streaming_response.summarize() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc_exotic = await response.parse()
            assert aidoc_exotic is None

        assert cast(Any, response.is_closed) is True
