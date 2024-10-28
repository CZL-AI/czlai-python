# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMagnumKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_key(self, client: Czlai) -> None:
        magnum_key = client.magnum_keys.get_key()
        assert magnum_key is None

    @parametrize
    def test_method_get_key_with_all_params(self, client: Czlai) -> None:
        magnum_key = client.magnum_keys.get_key(
            context="context",
        )
        assert magnum_key is None

    @parametrize
    def test_raw_response_get_key(self, client: Czlai) -> None:
        response = client.magnum_keys.with_raw_response.get_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        magnum_key = response.parse()
        assert magnum_key is None

    @parametrize
    def test_streaming_response_get_key(self, client: Czlai) -> None:
        with client.magnum_keys.with_streaming_response.get_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            magnum_key = response.parse()
            assert magnum_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_picture_choice(self, client: Czlai) -> None:
        magnum_key = client.magnum_keys.picture_choice(
            img_url="img_url",
        )
        assert magnum_key is None

    @parametrize
    def test_method_picture_choice_with_all_params(self, client: Czlai) -> None:
        magnum_key = client.magnum_keys.picture_choice(
            img_url="img_url",
            key_usage_id="key_usage_id",
            user_uuid="user_uuid",
        )
        assert magnum_key is None

    @parametrize
    def test_raw_response_picture_choice(self, client: Czlai) -> None:
        response = client.magnum_keys.with_raw_response.picture_choice(
            img_url="img_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        magnum_key = response.parse()
        assert magnum_key is None

    @parametrize
    def test_streaming_response_picture_choice(self, client: Czlai) -> None:
        with client.magnum_keys.with_streaming_response.picture_choice(
            img_url="img_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            magnum_key = response.parse()
            assert magnum_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_picture_question(self, client: Czlai) -> None:
        magnum_key = client.magnum_keys.picture_question(
            img_url="img_url",
        )
        assert magnum_key is None

    @parametrize
    def test_method_picture_question_with_all_params(self, client: Czlai) -> None:
        magnum_key = client.magnum_keys.picture_question(
            img_url="img_url",
            key_usage_id="key_usage_id",
            user_uuid="user_uuid",
        )
        assert magnum_key is None

    @parametrize
    def test_raw_response_picture_question(self, client: Czlai) -> None:
        response = client.magnum_keys.with_raw_response.picture_question(
            img_url="img_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        magnum_key = response.parse()
        assert magnum_key is None

    @parametrize
    def test_streaming_response_picture_question(self, client: Czlai) -> None:
        with client.magnum_keys.with_streaming_response.picture_question(
            img_url="img_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            magnum_key = response.parse()
            assert magnum_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_voice_choice(self, client: Czlai) -> None:
        magnum_key = client.magnum_keys.voice_choice(
            message="message",
        )
        assert magnum_key is None

    @parametrize
    def test_method_voice_choice_with_all_params(self, client: Czlai) -> None:
        magnum_key = client.magnum_keys.voice_choice(
            message="message",
            key_usage_id="key_usage_id",
            user_uuid="user_uuid",
        )
        assert magnum_key is None

    @parametrize
    def test_raw_response_voice_choice(self, client: Czlai) -> None:
        response = client.magnum_keys.with_raw_response.voice_choice(
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        magnum_key = response.parse()
        assert magnum_key is None

    @parametrize
    def test_streaming_response_voice_choice(self, client: Czlai) -> None:
        with client.magnum_keys.with_streaming_response.voice_choice(
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            magnum_key = response.parse()
            assert magnum_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_voice_question(self, client: Czlai) -> None:
        magnum_key = client.magnum_keys.voice_question(
            message="message",
        )
        assert magnum_key is None

    @parametrize
    def test_method_voice_question_with_all_params(self, client: Czlai) -> None:
        magnum_key = client.magnum_keys.voice_question(
            message="message",
            key_usage_id="key_usage_id",
            pet_id=0,
            user_uuid="user_uuid",
        )
        assert magnum_key is None

    @parametrize
    def test_raw_response_voice_question(self, client: Czlai) -> None:
        response = client.magnum_keys.with_raw_response.voice_question(
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        magnum_key = response.parse()
        assert magnum_key is None

    @parametrize
    def test_streaming_response_voice_question(self, client: Czlai) -> None:
        with client.magnum_keys.with_streaming_response.voice_question(
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            magnum_key = response.parse()
            assert magnum_key is None

        assert cast(Any, response.is_closed) is True


class TestAsyncMagnumKeys:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_key(self, async_client: AsyncCzlai) -> None:
        magnum_key = await async_client.magnum_keys.get_key()
        assert magnum_key is None

    @parametrize
    async def test_method_get_key_with_all_params(self, async_client: AsyncCzlai) -> None:
        magnum_key = await async_client.magnum_keys.get_key(
            context="context",
        )
        assert magnum_key is None

    @parametrize
    async def test_raw_response_get_key(self, async_client: AsyncCzlai) -> None:
        response = await async_client.magnum_keys.with_raw_response.get_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        magnum_key = await response.parse()
        assert magnum_key is None

    @parametrize
    async def test_streaming_response_get_key(self, async_client: AsyncCzlai) -> None:
        async with async_client.magnum_keys.with_streaming_response.get_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            magnum_key = await response.parse()
            assert magnum_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_picture_choice(self, async_client: AsyncCzlai) -> None:
        magnum_key = await async_client.magnum_keys.picture_choice(
            img_url="img_url",
        )
        assert magnum_key is None

    @parametrize
    async def test_method_picture_choice_with_all_params(self, async_client: AsyncCzlai) -> None:
        magnum_key = await async_client.magnum_keys.picture_choice(
            img_url="img_url",
            key_usage_id="key_usage_id",
            user_uuid="user_uuid",
        )
        assert magnum_key is None

    @parametrize
    async def test_raw_response_picture_choice(self, async_client: AsyncCzlai) -> None:
        response = await async_client.magnum_keys.with_raw_response.picture_choice(
            img_url="img_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        magnum_key = await response.parse()
        assert magnum_key is None

    @parametrize
    async def test_streaming_response_picture_choice(self, async_client: AsyncCzlai) -> None:
        async with async_client.magnum_keys.with_streaming_response.picture_choice(
            img_url="img_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            magnum_key = await response.parse()
            assert magnum_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_picture_question(self, async_client: AsyncCzlai) -> None:
        magnum_key = await async_client.magnum_keys.picture_question(
            img_url="img_url",
        )
        assert magnum_key is None

    @parametrize
    async def test_method_picture_question_with_all_params(self, async_client: AsyncCzlai) -> None:
        magnum_key = await async_client.magnum_keys.picture_question(
            img_url="img_url",
            key_usage_id="key_usage_id",
            user_uuid="user_uuid",
        )
        assert magnum_key is None

    @parametrize
    async def test_raw_response_picture_question(self, async_client: AsyncCzlai) -> None:
        response = await async_client.magnum_keys.with_raw_response.picture_question(
            img_url="img_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        magnum_key = await response.parse()
        assert magnum_key is None

    @parametrize
    async def test_streaming_response_picture_question(self, async_client: AsyncCzlai) -> None:
        async with async_client.magnum_keys.with_streaming_response.picture_question(
            img_url="img_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            magnum_key = await response.parse()
            assert magnum_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_voice_choice(self, async_client: AsyncCzlai) -> None:
        magnum_key = await async_client.magnum_keys.voice_choice(
            message="message",
        )
        assert magnum_key is None

    @parametrize
    async def test_method_voice_choice_with_all_params(self, async_client: AsyncCzlai) -> None:
        magnum_key = await async_client.magnum_keys.voice_choice(
            message="message",
            key_usage_id="key_usage_id",
            user_uuid="user_uuid",
        )
        assert magnum_key is None

    @parametrize
    async def test_raw_response_voice_choice(self, async_client: AsyncCzlai) -> None:
        response = await async_client.magnum_keys.with_raw_response.voice_choice(
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        magnum_key = await response.parse()
        assert magnum_key is None

    @parametrize
    async def test_streaming_response_voice_choice(self, async_client: AsyncCzlai) -> None:
        async with async_client.magnum_keys.with_streaming_response.voice_choice(
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            magnum_key = await response.parse()
            assert magnum_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_voice_question(self, async_client: AsyncCzlai) -> None:
        magnum_key = await async_client.magnum_keys.voice_question(
            message="message",
        )
        assert magnum_key is None

    @parametrize
    async def test_method_voice_question_with_all_params(self, async_client: AsyncCzlai) -> None:
        magnum_key = await async_client.magnum_keys.voice_question(
            message="message",
            key_usage_id="key_usage_id",
            pet_id=0,
            user_uuid="user_uuid",
        )
        assert magnum_key is None

    @parametrize
    async def test_raw_response_voice_question(self, async_client: AsyncCzlai) -> None:
        response = await async_client.magnum_keys.with_raw_response.voice_question(
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        magnum_key = await response.parse()
        assert magnum_key is None

    @parametrize
    async def test_streaming_response_voice_question(self, async_client: AsyncCzlai) -> None:
        async with async_client.magnum_keys.with_streaming_response.voice_question(
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            magnum_key = await response.parse()
            assert magnum_key is None

        assert cast(Any, response.is_closed) is True
