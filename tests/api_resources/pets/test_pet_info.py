# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPetInfo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Czlai) -> None:
        pet_info = client.pets.pet_info.retrieve(
            pets_type="dog",
        )
        assert pet_info is None

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Czlai) -> None:
        pet_info = client.pets.pet_info.retrieve(
            pets_type="dog",
            is_sort=0,
        )
        assert pet_info is None

    @parametrize
    def test_raw_response_retrieve(self, client: Czlai) -> None:
        response = client.pets.pet_info.with_raw_response.retrieve(
            pets_type="dog",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet_info = response.parse()
        assert pet_info is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Czlai) -> None:
        with client.pets.pet_info.with_streaming_response.retrieve(
            pets_type="dog",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet_info = response.parse()
            assert pet_info is None

        assert cast(Any, response.is_closed) is True


class TestAsyncPetInfo:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCzlai) -> None:
        pet_info = await async_client.pets.pet_info.retrieve(
            pets_type="dog",
        )
        assert pet_info is None

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncCzlai) -> None:
        pet_info = await async_client.pets.pet_info.retrieve(
            pets_type="dog",
            is_sort=0,
        )
        assert pet_info is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCzlai) -> None:
        response = await async_client.pets.pet_info.with_raw_response.retrieve(
            pets_type="dog",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet_info = await response.parse()
        assert pet_info is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCzlai) -> None:
        async with async_client.pets.pet_info.with_streaming_response.retrieve(
            pets_type="dog",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet_info = await response.parse()
            assert pet_info is None

        assert cast(Any, response.is_closed) is True
