# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAIConv:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_answer(self, client: Czlai) -> None:
        ai_conv = client.ai_conv.answer()
        assert_matches_type(str, ai_conv, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_answer_with_all_params(self, client: Czlai) -> None:
        ai_conv = client.ai_conv.answer(
            session_id="session_id",
            user_input="user_input",
        )
        assert_matches_type(str, ai_conv, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_answer(self, client: Czlai) -> None:
        response = client.ai_conv.with_raw_response.answer()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_conv = response.parse()
        assert_matches_type(str, ai_conv, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_answer(self, client: Czlai) -> None:
        with client.ai_conv.with_streaming_response.answer() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_conv = response.parse()
            assert_matches_type(str, ai_conv, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_relation(self, client: Czlai) -> None:
        ai_conv = client.ai_conv.relation()
        assert ai_conv is None

    @parametrize
    def test_method_relation_with_all_params(self, client: Czlai) -> None:
        ai_conv = client.ai_conv.relation(
            session_id="session_id",
            user_input="user_input",
        )
        assert ai_conv is None

    @parametrize
    def test_raw_response_relation(self, client: Czlai) -> None:
        response = client.ai_conv.with_raw_response.relation()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_conv = response.parse()
        assert ai_conv is None

    @parametrize
    def test_streaming_response_relation(self, client: Czlai) -> None:
        with client.ai_conv.with_streaming_response.relation() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_conv = response.parse()
            assert ai_conv is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_validate(self, client: Czlai) -> None:
        ai_conv = client.ai_conv.validate()
        assert ai_conv is None

    @parametrize
    def test_method_validate_with_all_params(self, client: Czlai) -> None:
        ai_conv = client.ai_conv.validate(
            session_id="session_id",
            user_input="user_input",
        )
        assert ai_conv is None

    @parametrize
    def test_raw_response_validate(self, client: Czlai) -> None:
        response = client.ai_conv.with_raw_response.validate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_conv = response.parse()
        assert ai_conv is None

    @parametrize
    def test_streaming_response_validate(self, client: Czlai) -> None:
        with client.ai_conv.with_streaming_response.validate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_conv = response.parse()
            assert ai_conv is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAIConv:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_answer(self, async_client: AsyncCzlai) -> None:
        ai_conv = await async_client.ai_conv.answer()
        assert_matches_type(str, ai_conv, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_answer_with_all_params(self, async_client: AsyncCzlai) -> None:
        ai_conv = await async_client.ai_conv.answer(
            session_id="session_id",
            user_input="user_input",
        )
        assert_matches_type(str, ai_conv, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_answer(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_conv.with_raw_response.answer()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_conv = await response.parse()
        assert_matches_type(str, ai_conv, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_answer(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_conv.with_streaming_response.answer() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_conv = await response.parse()
            assert_matches_type(str, ai_conv, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_relation(self, async_client: AsyncCzlai) -> None:
        ai_conv = await async_client.ai_conv.relation()
        assert ai_conv is None

    @parametrize
    async def test_method_relation_with_all_params(self, async_client: AsyncCzlai) -> None:
        ai_conv = await async_client.ai_conv.relation(
            session_id="session_id",
            user_input="user_input",
        )
        assert ai_conv is None

    @parametrize
    async def test_raw_response_relation(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_conv.with_raw_response.relation()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_conv = await response.parse()
        assert ai_conv is None

    @parametrize
    async def test_streaming_response_relation(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_conv.with_streaming_response.relation() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_conv = await response.parse()
            assert ai_conv is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_validate(self, async_client: AsyncCzlai) -> None:
        ai_conv = await async_client.ai_conv.validate()
        assert ai_conv is None

    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncCzlai) -> None:
        ai_conv = await async_client.ai_conv.validate(
            session_id="session_id",
            user_input="user_input",
        )
        assert ai_conv is None

    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_conv.with_raw_response.validate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_conv = await response.parse()
        assert ai_conv is None

    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_conv.with_streaming_response.validate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_conv = await response.parse()
            assert ai_conv is None

        assert cast(Any, response.is_closed) is True
