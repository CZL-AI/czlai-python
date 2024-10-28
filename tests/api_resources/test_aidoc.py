# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAidoc:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_if_continue_ask(self, client: Czlai) -> None:
        aidoc = client.aidoc.if_continue_ask()
        assert_matches_type(str, aidoc, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_if_continue_ask_with_all_params(self, client: Czlai) -> None:
        aidoc = client.aidoc.if_continue_ask(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert_matches_type(str, aidoc, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_if_continue_ask(self, client: Czlai) -> None:
        response = client.aidoc.with_raw_response.if_continue_ask()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc = response.parse()
        assert_matches_type(str, aidoc, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_if_continue_ask(self, client: Czlai) -> None:
        with client.aidoc.with_streaming_response.if_continue_ask() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc = response.parse()
            assert_matches_type(str, aidoc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_if_need_image(self, client: Czlai) -> None:
        aidoc = client.aidoc.if_need_image()
        assert_matches_type(object, aidoc, path=["response"])

    @parametrize
    def test_method_if_need_image_with_all_params(self, client: Czlai) -> None:
        aidoc = client.aidoc.if_need_image(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert_matches_type(object, aidoc, path=["response"])

    @parametrize
    def test_raw_response_if_need_image(self, client: Czlai) -> None:
        response = client.aidoc.with_raw_response.if_need_image()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc = response.parse()
        assert_matches_type(object, aidoc, path=["response"])

    @parametrize
    def test_streaming_response_if_need_image(self, client: Czlai) -> None:
        with client.aidoc.with_streaming_response.if_need_image() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc = response.parse()
            assert_matches_type(object, aidoc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_pic_result(self, client: Czlai) -> None:
        aidoc = client.aidoc.pic_result()
        assert aidoc is None

    @parametrize
    def test_method_pic_result_with_all_params(self, client: Czlai) -> None:
        aidoc = client.aidoc.pic_result(
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
        )
        assert aidoc is None

    @parametrize
    def test_raw_response_pic_result(self, client: Czlai) -> None:
        response = client.aidoc.with_raw_response.pic_result()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc = response.parse()
        assert aidoc is None

    @parametrize
    def test_streaming_response_pic_result(self, client: Czlai) -> None:
        with client.aidoc.with_streaming_response.pic_result() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc = response.parse()
            assert aidoc is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_report(self, client: Czlai) -> None:
        aidoc = client.aidoc.report(
            session_id="session_id",
        )
        assert aidoc is None

    @parametrize
    def test_raw_response_report(self, client: Czlai) -> None:
        response = client.aidoc.with_raw_response.report(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc = response.parse()
        assert aidoc is None

    @parametrize
    def test_streaming_response_report(self, client: Czlai) -> None:
        with client.aidoc.with_streaming_response.report(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc = response.parse()
            assert aidoc is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_report_task(self, client: Czlai) -> None:
        aidoc = client.aidoc.report_task(
            session_id="session_id",
        )
        assert aidoc is None

    @parametrize
    def test_method_report_task_with_all_params(self, client: Czlai) -> None:
        aidoc = client.aidoc.report_task(
            session_id="session_id",
            report_type=0,
        )
        assert aidoc is None

    @parametrize
    def test_raw_response_report_task(self, client: Czlai) -> None:
        response = client.aidoc.with_raw_response.report_task(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc = response.parse()
        assert aidoc is None

    @parametrize
    def test_streaming_response_report_task(self, client: Czlai) -> None:
        with client.aidoc.with_streaming_response.report_task(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc = response.parse()
            assert aidoc is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAidoc:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_if_continue_ask(self, async_client: AsyncCzlai) -> None:
        aidoc = await async_client.aidoc.if_continue_ask()
        assert_matches_type(str, aidoc, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_if_continue_ask_with_all_params(self, async_client: AsyncCzlai) -> None:
        aidoc = await async_client.aidoc.if_continue_ask(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert_matches_type(str, aidoc, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_if_continue_ask(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aidoc.with_raw_response.if_continue_ask()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc = await response.parse()
        assert_matches_type(str, aidoc, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_if_continue_ask(self, async_client: AsyncCzlai) -> None:
        async with async_client.aidoc.with_streaming_response.if_continue_ask() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc = await response.parse()
            assert_matches_type(str, aidoc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_if_need_image(self, async_client: AsyncCzlai) -> None:
        aidoc = await async_client.aidoc.if_need_image()
        assert_matches_type(object, aidoc, path=["response"])

    @parametrize
    async def test_method_if_need_image_with_all_params(self, async_client: AsyncCzlai) -> None:
        aidoc = await async_client.aidoc.if_need_image(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert_matches_type(object, aidoc, path=["response"])

    @parametrize
    async def test_raw_response_if_need_image(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aidoc.with_raw_response.if_need_image()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc = await response.parse()
        assert_matches_type(object, aidoc, path=["response"])

    @parametrize
    async def test_streaming_response_if_need_image(self, async_client: AsyncCzlai) -> None:
        async with async_client.aidoc.with_streaming_response.if_need_image() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc = await response.parse()
            assert_matches_type(object, aidoc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_pic_result(self, async_client: AsyncCzlai) -> None:
        aidoc = await async_client.aidoc.pic_result()
        assert aidoc is None

    @parametrize
    async def test_method_pic_result_with_all_params(self, async_client: AsyncCzlai) -> None:
        aidoc = await async_client.aidoc.pic_result(
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
        )
        assert aidoc is None

    @parametrize
    async def test_raw_response_pic_result(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aidoc.with_raw_response.pic_result()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc = await response.parse()
        assert aidoc is None

    @parametrize
    async def test_streaming_response_pic_result(self, async_client: AsyncCzlai) -> None:
        async with async_client.aidoc.with_streaming_response.pic_result() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc = await response.parse()
            assert aidoc is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_report(self, async_client: AsyncCzlai) -> None:
        aidoc = await async_client.aidoc.report(
            session_id="session_id",
        )
        assert aidoc is None

    @parametrize
    async def test_raw_response_report(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aidoc.with_raw_response.report(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc = await response.parse()
        assert aidoc is None

    @parametrize
    async def test_streaming_response_report(self, async_client: AsyncCzlai) -> None:
        async with async_client.aidoc.with_streaming_response.report(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc = await response.parse()
            assert aidoc is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_report_task(self, async_client: AsyncCzlai) -> None:
        aidoc = await async_client.aidoc.report_task(
            session_id="session_id",
        )
        assert aidoc is None

    @parametrize
    async def test_method_report_task_with_all_params(self, async_client: AsyncCzlai) -> None:
        aidoc = await async_client.aidoc.report_task(
            session_id="session_id",
            report_type=0,
        )
        assert aidoc is None

    @parametrize
    async def test_raw_response_report_task(self, async_client: AsyncCzlai) -> None:
        response = await async_client.aidoc.with_raw_response.report_task(
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aidoc = await response.parse()
        assert aidoc is None

    @parametrize
    async def test_streaming_response_report_task(self, async_client: AsyncCzlai) -> None:
        async with async_client.aidoc.with_streaming_response.report_task(
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aidoc = await response.parse()
            assert aidoc is None

        assert cast(Any, response.is_closed) is True
