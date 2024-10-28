# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAipicExotics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_options(self, client: Czlai) -> None:
        aipic_exotic = client.aipic_exotics.options()
        assert aipic_exotic is None

    @parametrize
    def test_method_options_with_all_params(self, client: Czlai) -> None:
        aipic_exotic = client.aipic_exotics.options(
            pet_profile_id=0,
            question="question",
            session_id="session_id",
        )
        assert aipic_exotic is None

    @parametrize
    def test_raw_response_options(self, client: Czlai) -> None:
        response = client.aipic_exotics.with_raw_response.options()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic_exotic = response.parse()
        assert aipic_exotic is None

    @parametrize
    def test_streaming_response_options(self, client: Czlai) -> None:
        with client.aipic_exotics.with_streaming_response.options() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic_exotic = response.parse()
            assert aipic_exotic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_pic_result(self, client: Czlai) -> None:
        aipic_exotic = client.aipic_exotics.pic_result()
        assert aipic_exotic is None

    @parametrize
    def test_method_pic_result_with_all_params(self, client: Czlai) -> None:
        aipic_exotic = client.aipic_exotics.pic_result(
            img_belong=0,
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
        )
        assert aipic_exotic is None

    @parametrize
    def test_raw_response_pic_result(self, client: Czlai) -> None:
        response = client.aipic_exotics.with_raw_response.pic_result()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic_exotic = response.parse()
        assert aipic_exotic is None

    @parametrize
    def test_streaming_response_pic_result(self, client: Czlai) -> None:
        with client.aipic_exotics.with_streaming_response.pic_result() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic_exotic = response.parse()
            assert aipic_exotic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_question(self, client: Czlai) -> None:
        aipic_exotic = client.aipic_exotics.question()
        assert aipic_exotic is None

    @parametrize
    def test_method_question_with_all_params(self, client: Czlai) -> None:
        aipic_exotic = client.aipic_exotics.question(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert aipic_exotic is None

    @parametrize
    def test_raw_response_question(self, client: Czlai) -> None:
        response = client.aipic_exotics.with_raw_response.question()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic_exotic = response.parse()
        assert aipic_exotic is None

    @parametrize
    def test_streaming_response_question(self, client: Czlai) -> None:
        with client.aipic_exotics.with_streaming_response.question() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic_exotic = response.parse()
            assert aipic_exotic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_report(self, client: Czlai) -> None:
        aipic_exotic = client.aipic_exotics.report(
            session_id="session_id",
        )
        assert aipic_exotic is None

    @parametrize
    def test_method_report_with_all_params(self, client: Czlai) -> None:
        aipic_exotic = client.aipic_exotics.report(
            session_id="session_id",
            img_url="img_url",
            pet_profile_id=0,
            sub_module_type=0,
        )
        assert aipic_exotic is None

    @parametrize
    def test_raw_response_report(self, client: Czlai) -> None:
        response = client.aipic_exotics.with_raw_response.report(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic_exotic = response.parse()
        assert aipic_exotic is None

    @parametrize
    def test_streaming_response_report(self, client: Czlai) -> None:
        with client.aipic_exotics.with_streaming_response.report(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic_exotic = response.parse()
            assert aipic_exotic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_report_task(self, client: Czlai) -> None:
        aipic_exotic = client.aipic_exotics.report_task(
            session_id="session_id",
        )
        assert aipic_exotic is None

    @parametrize
    def test_method_report_task_with_all_params(self, client: Czlai) -> None:
        aipic_exotic = client.aipic_exotics.report_task(
            session_id="session_id",
            img_url="img_url",
            report_type=0,
        )
        assert aipic_exotic is None

    @parametrize
    def test_raw_response_report_task(self, client: Czlai) -> None:
        response = client.aipic_exotics.with_raw_response.report_task(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic_exotic = response.parse()
        assert aipic_exotic is None

    @parametrize
    def test_streaming_response_report_task(self, client: Czlai) -> None:
        with client.aipic_exotics.with_streaming_response.report_task(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic_exotic = response.parse()
            assert aipic_exotic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_summary(self, client: Czlai) -> None:
        aipic_exotic = client.aipic_exotics.summary()
        assert aipic_exotic is None

    @parametrize
    def test_method_summary_with_all_params(self, client: Czlai) -> None:
        aipic_exotic = client.aipic_exotics.summary(
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
            sub_module_type=0,
        )
        assert aipic_exotic is None

    @parametrize
    def test_raw_response_summary(self, client: Czlai) -> None:
        response = client.aipic_exotics.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic_exotic = response.parse()
        assert aipic_exotic is None

    @parametrize
    def test_streaming_response_summary(self, client: Czlai) -> None:
        with client.aipic_exotics.with_streaming_response.summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic_exotic = response.parse()
            assert aipic_exotic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_validate(self, client: Czlai) -> None:
        aipic_exotic = client.aipic_exotics.validate()
        assert aipic_exotic is None

    @parametrize
    def test_method_validate_with_all_params(self, client: Czlai) -> None:
        aipic_exotic = client.aipic_exotics.validate(
            answer="answer",
            pet_profile_id=0,
            question="question",
            session_id="session_id",
        )
        assert aipic_exotic is None

    @parametrize
    def test_raw_response_validate(self, client: Czlai) -> None:
        response = client.aipic_exotics.with_raw_response.validate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic_exotic = response.parse()
        assert aipic_exotic is None

    @parametrize
    def test_streaming_response_validate(self, client: Czlai) -> None:
        with client.aipic_exotics.with_streaming_response.validate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic_exotic = response.parse()
            assert aipic_exotic is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAipicExotics:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_options(self, async_client: AsyncCzlai) -> None:
        aipic_exotic = await async_client.aipic_exotics.options()
        assert aipic_exotic is None

    @parametrize
    async def test_method_options_with_all_params(self, async_client: AsyncCzlai) -> None:
        aipic_exotic = await async_client.aipic_exotics.options(
            pet_profile_id=0,
            question="question",
            session_id="session_id",
        )
        assert aipic_exotic is None

    @parametrize
    async def test_raw_response_options(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aipic_exotics.with_raw_response.options()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic_exotic = await response.parse()
        assert aipic_exotic is None

    @parametrize
    async def test_streaming_response_options(self, async_client: AsyncCzlai) -> None:
        async with async_client.aipic_exotics.with_streaming_response.options() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic_exotic = await response.parse()
            assert aipic_exotic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_pic_result(self, async_client: AsyncCzlai) -> None:
        aipic_exotic = await async_client.aipic_exotics.pic_result()
        assert aipic_exotic is None

    @parametrize
    async def test_method_pic_result_with_all_params(self, async_client: AsyncCzlai) -> None:
        aipic_exotic = await async_client.aipic_exotics.pic_result(
            img_belong=0,
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
        )
        assert aipic_exotic is None

    @parametrize
    async def test_raw_response_pic_result(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aipic_exotics.with_raw_response.pic_result()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic_exotic = await response.parse()
        assert aipic_exotic is None

    @parametrize
    async def test_streaming_response_pic_result(self, async_client: AsyncCzlai) -> None:
        async with async_client.aipic_exotics.with_streaming_response.pic_result() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic_exotic = await response.parse()
            assert aipic_exotic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_question(self, async_client: AsyncCzlai) -> None:
        aipic_exotic = await async_client.aipic_exotics.question()
        assert aipic_exotic is None

    @parametrize
    async def test_method_question_with_all_params(self, async_client: AsyncCzlai) -> None:
        aipic_exotic = await async_client.aipic_exotics.question(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert aipic_exotic is None

    @parametrize
    async def test_raw_response_question(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aipic_exotics.with_raw_response.question()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic_exotic = await response.parse()
        assert aipic_exotic is None

    @parametrize
    async def test_streaming_response_question(self, async_client: AsyncCzlai) -> None:
        async with async_client.aipic_exotics.with_streaming_response.question() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic_exotic = await response.parse()
            assert aipic_exotic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_report(self, async_client: AsyncCzlai) -> None:
        aipic_exotic = await async_client.aipic_exotics.report(
            session_id="session_id",
        )
        assert aipic_exotic is None

    @parametrize
    async def test_method_report_with_all_params(self, async_client: AsyncCzlai) -> None:
        aipic_exotic = await async_client.aipic_exotics.report(
            session_id="session_id",
            img_url="img_url",
            pet_profile_id=0,
            sub_module_type=0,
        )
        assert aipic_exotic is None

    @parametrize
    async def test_raw_response_report(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aipic_exotics.with_raw_response.report(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic_exotic = await response.parse()
        assert aipic_exotic is None

    @parametrize
    async def test_streaming_response_report(self, async_client: AsyncCzlai) -> None:
        async with async_client.aipic_exotics.with_streaming_response.report(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic_exotic = await response.parse()
            assert aipic_exotic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_report_task(self, async_client: AsyncCzlai) -> None:
        aipic_exotic = await async_client.aipic_exotics.report_task(
            session_id="session_id",
        )
        assert aipic_exotic is None

    @parametrize
    async def test_method_report_task_with_all_params(self, async_client: AsyncCzlai) -> None:
        aipic_exotic = await async_client.aipic_exotics.report_task(
            session_id="session_id",
            img_url="img_url",
            report_type=0,
        )
        assert aipic_exotic is None

    @parametrize
    async def test_raw_response_report_task(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aipic_exotics.with_raw_response.report_task(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic_exotic = await response.parse()
        assert aipic_exotic is None

    @parametrize
    async def test_streaming_response_report_task(self, async_client: AsyncCzlai) -> None:
        async with async_client.aipic_exotics.with_streaming_response.report_task(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic_exotic = await response.parse()
            assert aipic_exotic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_summary(self, async_client: AsyncCzlai) -> None:
        aipic_exotic = await async_client.aipic_exotics.summary()
        assert aipic_exotic is None

    @parametrize
    async def test_method_summary_with_all_params(self, async_client: AsyncCzlai) -> None:
        aipic_exotic = await async_client.aipic_exotics.summary(
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
            sub_module_type=0,
        )
        assert aipic_exotic is None

    @parametrize
    async def test_raw_response_summary(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aipic_exotics.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic_exotic = await response.parse()
        assert aipic_exotic is None

    @parametrize
    async def test_streaming_response_summary(self, async_client: AsyncCzlai) -> None:
        async with async_client.aipic_exotics.with_streaming_response.summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic_exotic = await response.parse()
            assert aipic_exotic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_validate(self, async_client: AsyncCzlai) -> None:
        aipic_exotic = await async_client.aipic_exotics.validate()
        assert aipic_exotic is None

    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncCzlai) -> None:
        aipic_exotic = await async_client.aipic_exotics.validate(
            answer="answer",
            pet_profile_id=0,
            question="question",
            session_id="session_id",
        )
        assert aipic_exotic is None

    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aipic_exotics.with_raw_response.validate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic_exotic = await response.parse()
        assert aipic_exotic is None

    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncCzlai) -> None:
        async with async_client.aipic_exotics.with_streaming_response.validate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic_exotic = await response.parse()
            assert aipic_exotic is None

        assert cast(Any, response.is_closed) is True
