# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAipic:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_options(self, client: Czlai) -> None:
        aipic = client.aipic.options()
        assert aipic is None

    @parametrize
    def test_method_options_with_all_params(self, client: Czlai) -> None:
        aipic = client.aipic.options(
            pet_profile_id=0,
            question="question",
            session_id="session_id",
        )
        assert aipic is None

    @parametrize
    def test_raw_response_options(self, client: Czlai) -> None:
        response = client.aipic.with_raw_response.options()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic = response.parse()
        assert aipic is None

    @parametrize
    def test_streaming_response_options(self, client: Czlai) -> None:
        with client.aipic.with_streaming_response.options() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic = response.parse()
            assert aipic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_pic_result(self, client: Czlai) -> None:
        aipic = client.aipic.pic_result()
        assert aipic is None

    @parametrize
    def test_method_pic_result_with_all_params(self, client: Czlai) -> None:
        aipic = client.aipic.pic_result(
            img_belong=0,
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
        )
        assert aipic is None

    @parametrize
    def test_raw_response_pic_result(self, client: Czlai) -> None:
        response = client.aipic.with_raw_response.pic_result()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic = response.parse()
        assert aipic is None

    @parametrize
    def test_streaming_response_pic_result(self, client: Czlai) -> None:
        with client.aipic.with_streaming_response.pic_result() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic = response.parse()
            assert aipic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_question(self, client: Czlai) -> None:
        aipic = client.aipic.question()
        assert aipic is None

    @parametrize
    def test_method_question_with_all_params(self, client: Czlai) -> None:
        aipic = client.aipic.question(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert aipic is None

    @parametrize
    def test_raw_response_question(self, client: Czlai) -> None:
        response = client.aipic.with_raw_response.question()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic = response.parse()
        assert aipic is None

    @parametrize
    def test_streaming_response_question(self, client: Czlai) -> None:
        with client.aipic.with_streaming_response.question() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic = response.parse()
            assert aipic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_report(self, client: Czlai) -> None:
        aipic = client.aipic.report(
            session_id="session_id",
        )
        assert aipic is None

    @parametrize
    def test_method_report_with_all_params(self, client: Czlai) -> None:
        aipic = client.aipic.report(
            session_id="session_id",
            img_url="img_url",
            pet_profile_id=0,
            sub_module_type=0,
        )
        assert aipic is None

    @parametrize
    def test_raw_response_report(self, client: Czlai) -> None:
        response = client.aipic.with_raw_response.report(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic = response.parse()
        assert aipic is None

    @parametrize
    def test_streaming_response_report(self, client: Czlai) -> None:
        with client.aipic.with_streaming_response.report(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic = response.parse()
            assert aipic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_report_task(self, client: Czlai) -> None:
        aipic = client.aipic.report_task(
            session_id="session_id",
        )
        assert aipic is None

    @parametrize
    def test_method_report_task_with_all_params(self, client: Czlai) -> None:
        aipic = client.aipic.report_task(
            session_id="session_id",
            img_url="img_url",
            report_type=0,
        )
        assert aipic is None

    @parametrize
    def test_raw_response_report_task(self, client: Czlai) -> None:
        response = client.aipic.with_raw_response.report_task(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic = response.parse()
        assert aipic is None

    @parametrize
    def test_streaming_response_report_task(self, client: Czlai) -> None:
        with client.aipic.with_streaming_response.report_task(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic = response.parse()
            assert aipic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_validate(self, client: Czlai) -> None:
        aipic = client.aipic.validate()
        assert aipic is None

    @parametrize
    def test_method_validate_with_all_params(self, client: Czlai) -> None:
        aipic = client.aipic.validate(
            answer="answer",
            pet_profile_id=0,
            question="question",
            session_id="session_id",
        )
        assert aipic is None

    @parametrize
    def test_raw_response_validate(self, client: Czlai) -> None:
        response = client.aipic.with_raw_response.validate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic = response.parse()
        assert aipic is None

    @parametrize
    def test_streaming_response_validate(self, client: Czlai) -> None:
        with client.aipic.with_streaming_response.validate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic = response.parse()
            assert aipic is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAipic:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_options(self, async_client: AsyncCzlai) -> None:
        aipic = await async_client.aipic.options()
        assert aipic is None

    @parametrize
    async def test_method_options_with_all_params(self, async_client: AsyncCzlai) -> None:
        aipic = await async_client.aipic.options(
            pet_profile_id=0,
            question="question",
            session_id="session_id",
        )
        assert aipic is None

    @parametrize
    async def test_raw_response_options(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aipic.with_raw_response.options()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic = await response.parse()
        assert aipic is None

    @parametrize
    async def test_streaming_response_options(self, async_client: AsyncCzlai) -> None:
        async with async_client.aipic.with_streaming_response.options() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic = await response.parse()
            assert aipic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_pic_result(self, async_client: AsyncCzlai) -> None:
        aipic = await async_client.aipic.pic_result()
        assert aipic is None

    @parametrize
    async def test_method_pic_result_with_all_params(self, async_client: AsyncCzlai) -> None:
        aipic = await async_client.aipic.pic_result(
            img_belong=0,
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
        )
        assert aipic is None

    @parametrize
    async def test_raw_response_pic_result(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aipic.with_raw_response.pic_result()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic = await response.parse()
        assert aipic is None

    @parametrize
    async def test_streaming_response_pic_result(self, async_client: AsyncCzlai) -> None:
        async with async_client.aipic.with_streaming_response.pic_result() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic = await response.parse()
            assert aipic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_question(self, async_client: AsyncCzlai) -> None:
        aipic = await async_client.aipic.question()
        assert aipic is None

    @parametrize
    async def test_method_question_with_all_params(self, async_client: AsyncCzlai) -> None:
        aipic = await async_client.aipic.question(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert aipic is None

    @parametrize
    async def test_raw_response_question(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aipic.with_raw_response.question()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic = await response.parse()
        assert aipic is None

    @parametrize
    async def test_streaming_response_question(self, async_client: AsyncCzlai) -> None:
        async with async_client.aipic.with_streaming_response.question() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic = await response.parse()
            assert aipic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_report(self, async_client: AsyncCzlai) -> None:
        aipic = await async_client.aipic.report(
            session_id="session_id",
        )
        assert aipic is None

    @parametrize
    async def test_method_report_with_all_params(self, async_client: AsyncCzlai) -> None:
        aipic = await async_client.aipic.report(
            session_id="session_id",
            img_url="img_url",
            pet_profile_id=0,
            sub_module_type=0,
        )
        assert aipic is None

    @parametrize
    async def test_raw_response_report(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aipic.with_raw_response.report(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic = await response.parse()
        assert aipic is None

    @parametrize
    async def test_streaming_response_report(self, async_client: AsyncCzlai) -> None:
        async with async_client.aipic.with_streaming_response.report(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic = await response.parse()
            assert aipic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_report_task(self, async_client: AsyncCzlai) -> None:
        aipic = await async_client.aipic.report_task(
            session_id="session_id",
        )
        assert aipic is None

    @parametrize
    async def test_method_report_task_with_all_params(self, async_client: AsyncCzlai) -> None:
        aipic = await async_client.aipic.report_task(
            session_id="session_id",
            img_url="img_url",
            report_type=0,
        )
        assert aipic is None

    @parametrize
    async def test_raw_response_report_task(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aipic.with_raw_response.report_task(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic = await response.parse()
        assert aipic is None

    @parametrize
    async def test_streaming_response_report_task(self, async_client: AsyncCzlai) -> None:
        async with async_client.aipic.with_streaming_response.report_task(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic = await response.parse()
            assert aipic is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_validate(self, async_client: AsyncCzlai) -> None:
        aipic = await async_client.aipic.validate()
        assert aipic is None

    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncCzlai) -> None:
        aipic = await async_client.aipic.validate(
            answer="answer",
            pet_profile_id=0,
            question="question",
            session_id="session_id",
        )
        assert aipic is None

    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aipic.with_raw_response.validate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aipic = await response.parse()
        assert aipic is None

    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncCzlai) -> None:
        async with async_client.aipic.with_streaming_response.validate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aipic = await response.parse()
            assert aipic is None

        assert cast(Any, response.is_closed) is True
