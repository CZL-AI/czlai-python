# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai
from czlai.types import (
    AIMemeCreateResponse,
    AIMemeGenerateResponse,
    AIMemeRetrieveResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAIMemes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Czlai) -> None:
        ai_meme = client.ai_memes.create()
        assert_matches_type(AIMemeCreateResponse, ai_meme, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Czlai) -> None:
        ai_meme = client.ai_memes.create(
            image_url="image_url",
            session_id="session_id",
        )
        assert_matches_type(AIMemeCreateResponse, ai_meme, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Czlai) -> None:
        response = client.ai_memes.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_meme = response.parse()
        assert_matches_type(AIMemeCreateResponse, ai_meme, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Czlai) -> None:
        with client.ai_memes.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_meme = response.parse()
            assert_matches_type(AIMemeCreateResponse, ai_meme, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Czlai) -> None:
        ai_meme = client.ai_memes.retrieve()
        assert_matches_type(AIMemeRetrieveResponse, ai_meme, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Czlai) -> None:
        ai_meme = client.ai_memes.retrieve(
            limit=1,
            page=1,
        )
        assert_matches_type(AIMemeRetrieveResponse, ai_meme, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Czlai) -> None:
        response = client.ai_memes.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_meme = response.parse()
        assert_matches_type(AIMemeRetrieveResponse, ai_meme, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Czlai) -> None:
        with client.ai_memes.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_meme = response.parse()
            assert_matches_type(AIMemeRetrieveResponse, ai_meme, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_generate(self, client: Czlai) -> None:
        ai_meme = client.ai_memes.generate()
        assert_matches_type(AIMemeGenerateResponse, ai_meme, path=["response"])

    @parametrize
    def test_method_generate_with_all_params(self, client: Czlai) -> None:
        ai_meme = client.ai_memes.generate(
            context_index=0,
            meme_id=0,
        )
        assert_matches_type(AIMemeGenerateResponse, ai_meme, path=["response"])

    @parametrize
    def test_raw_response_generate(self, client: Czlai) -> None:
        response = client.ai_memes.with_raw_response.generate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_meme = response.parse()
        assert_matches_type(AIMemeGenerateResponse, ai_meme, path=["response"])

    @parametrize
    def test_streaming_response_generate(self, client: Czlai) -> None:
        with client.ai_memes.with_streaming_response.generate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_meme = response.parse()
            assert_matches_type(AIMemeGenerateResponse, ai_meme, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAIMemes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCzlai) -> None:
        ai_meme = await async_client.ai_memes.create()
        assert_matches_type(AIMemeCreateResponse, ai_meme, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCzlai) -> None:
        ai_meme = await async_client.ai_memes.create(
            image_url="image_url",
            session_id="session_id",
        )
        assert_matches_type(AIMemeCreateResponse, ai_meme, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_memes.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_meme = await response.parse()
        assert_matches_type(AIMemeCreateResponse, ai_meme, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_memes.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_meme = await response.parse()
            assert_matches_type(AIMemeCreateResponse, ai_meme, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCzlai) -> None:
        ai_meme = await async_client.ai_memes.retrieve()
        assert_matches_type(AIMemeRetrieveResponse, ai_meme, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncCzlai) -> None:
        ai_meme = await async_client.ai_memes.retrieve(
            limit=1,
            page=1,
        )
        assert_matches_type(AIMemeRetrieveResponse, ai_meme, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_memes.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_meme = await response.parse()
        assert_matches_type(AIMemeRetrieveResponse, ai_meme, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_memes.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_meme = await response.parse()
            assert_matches_type(AIMemeRetrieveResponse, ai_meme, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_generate(self, async_client: AsyncCzlai) -> None:
        ai_meme = await async_client.ai_memes.generate()
        assert_matches_type(AIMemeGenerateResponse, ai_meme, path=["response"])

    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncCzlai) -> None:
        ai_meme = await async_client.ai_memes.generate(
            context_index=0,
            meme_id=0,
        )
        assert_matches_type(AIMemeGenerateResponse, ai_meme, path=["response"])

    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncCzlai) -> None:
        response = await async_client.ai_memes.with_raw_response.generate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_meme = await response.parse()
        assert_matches_type(AIMemeGenerateResponse, ai_meme, path=["response"])

    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncCzlai) -> None:
        async with async_client.ai_memes.with_streaming_response.generate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_meme = await response.parse()
            assert_matches_type(AIMemeGenerateResponse, ai_meme, path=["response"])

        assert cast(Any, response.is_closed) is True
