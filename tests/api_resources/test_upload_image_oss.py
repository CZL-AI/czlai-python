# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUploadImageOss:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Czlai) -> None:
        upload_image_oss = client.upload_image_oss.create(
            upload_type=1,
            image=b"raw file contents",
        )
        assert upload_image_oss is None

    @parametrize
    def test_method_create_with_all_params(self, client: Czlai) -> None:
        upload_image_oss = client.upload_image_oss.create(
            upload_type=1,
            image=b"raw file contents",
            upload_to_local=0,
        )
        assert upload_image_oss is None

    @parametrize
    def test_raw_response_create(self, client: Czlai) -> None:
        response = client.upload_image_oss.with_raw_response.create(
            upload_type=1,
            image=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload_image_oss = response.parse()
        assert upload_image_oss is None

    @parametrize
    def test_streaming_response_create(self, client: Czlai) -> None:
        with client.upload_image_oss.with_streaming_response.create(
            upload_type=1,
            image=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload_image_oss = response.parse()
            assert upload_image_oss is None

        assert cast(Any, response.is_closed) is True


class TestAsyncUploadImageOss:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCzlai) -> None:
        upload_image_oss = await async_client.upload_image_oss.create(
            upload_type=1,
            image=b"raw file contents",
        )
        assert upload_image_oss is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCzlai) -> None:
        upload_image_oss = await async_client.upload_image_oss.create(
            upload_type=1,
            image=b"raw file contents",
            upload_to_local=0,
        )
        assert upload_image_oss is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCzlai) -> None:
        response = await async_client.upload_image_oss.with_raw_response.create(
            upload_type=1,
            image=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload_image_oss = await response.parse()
        assert upload_image_oss is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCzlai) -> None:
        async with async_client.upload_image_oss.with_streaming_response.create(
            upload_type=1,
            image=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload_image_oss = await response.parse()
            assert upload_image_oss is None

        assert cast(Any, response.is_closed) is True
