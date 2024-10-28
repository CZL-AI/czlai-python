# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMedicationAnalysis:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_pic_result(self, client: Czlai) -> None:
        medication_analysis = client.medication_analysis.pic_result()
        assert medication_analysis is None

    @parametrize
    def test_method_pic_result_with_all_params(self, client: Czlai) -> None:
        medication_analysis = client.medication_analysis.pic_result(
            img_belong=0,
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
        )
        assert medication_analysis is None

    @parametrize
    def test_raw_response_pic_result(self, client: Czlai) -> None:
        response = client.medication_analysis.with_raw_response.pic_result()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        medication_analysis = response.parse()
        assert medication_analysis is None

    @parametrize
    def test_streaming_response_pic_result(self, client: Czlai) -> None:
        with client.medication_analysis.with_streaming_response.pic_result() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            medication_analysis = response.parse()
            assert medication_analysis is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_report(self, client: Czlai) -> None:
        medication_analysis = client.medication_analysis.report()
        assert medication_analysis is None

    @parametrize
    def test_method_report_with_all_params(self, client: Czlai) -> None:
        medication_analysis = client.medication_analysis.report(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert medication_analysis is None

    @parametrize
    def test_raw_response_report(self, client: Czlai) -> None:
        response = client.medication_analysis.with_raw_response.report()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        medication_analysis = response.parse()
        assert medication_analysis is None

    @parametrize
    def test_streaming_response_report(self, client: Czlai) -> None:
        with client.medication_analysis.with_streaming_response.report() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            medication_analysis = response.parse()
            assert medication_analysis is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_summary(self, client: Czlai) -> None:
        medication_analysis = client.medication_analysis.summary()
        assert medication_analysis is None

    @parametrize
    def test_method_summary_with_all_params(self, client: Czlai) -> None:
        medication_analysis = client.medication_analysis.summary(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert medication_analysis is None

    @parametrize
    def test_raw_response_summary(self, client: Czlai) -> None:
        response = client.medication_analysis.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        medication_analysis = response.parse()
        assert medication_analysis is None

    @parametrize
    def test_streaming_response_summary(self, client: Czlai) -> None:
        with client.medication_analysis.with_streaming_response.summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            medication_analysis = response.parse()
            assert medication_analysis is None

        assert cast(Any, response.is_closed) is True


class TestAsyncMedicationAnalysis:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_pic_result(self, async_client: AsyncCzlai) -> None:
        medication_analysis = await async_client.medication_analysis.pic_result()
        assert medication_analysis is None

    @parametrize
    async def test_method_pic_result_with_all_params(self, async_client: AsyncCzlai) -> None:
        medication_analysis = await async_client.medication_analysis.pic_result(
            img_belong=0,
            img_url="img_url",
            pet_profile_id=0,
            session_id="session_id",
        )
        assert medication_analysis is None

    @parametrize
    async def test_raw_response_pic_result(self, async_client: AsyncCzlai) -> None:
        response = await async_client.medication_analysis.with_raw_response.pic_result()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        medication_analysis = await response.parse()
        assert medication_analysis is None

    @parametrize
    async def test_streaming_response_pic_result(self, async_client: AsyncCzlai) -> None:
        async with async_client.medication_analysis.with_streaming_response.pic_result() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            medication_analysis = await response.parse()
            assert medication_analysis is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_report(self, async_client: AsyncCzlai) -> None:
        medication_analysis = await async_client.medication_analysis.report()
        assert medication_analysis is None

    @parametrize
    async def test_method_report_with_all_params(self, async_client: AsyncCzlai) -> None:
        medication_analysis = await async_client.medication_analysis.report(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert medication_analysis is None

    @parametrize
    async def test_raw_response_report(self, async_client: AsyncCzlai) -> None:
        response = await async_client.medication_analysis.with_raw_response.report()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        medication_analysis = await response.parse()
        assert medication_analysis is None

    @parametrize
    async def test_streaming_response_report(self, async_client: AsyncCzlai) -> None:
        async with async_client.medication_analysis.with_streaming_response.report() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            medication_analysis = await response.parse()
            assert medication_analysis is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_summary(self, async_client: AsyncCzlai) -> None:
        medication_analysis = await async_client.medication_analysis.summary()
        assert medication_analysis is None

    @parametrize
    async def test_method_summary_with_all_params(self, async_client: AsyncCzlai) -> None:
        medication_analysis = await async_client.medication_analysis.summary(
            pet_profile_id=0,
            session_id="session_id",
        )
        assert medication_analysis is None

    @parametrize
    async def test_raw_response_summary(self, async_client: AsyncCzlai) -> None:
        response = await async_client.medication_analysis.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        medication_analysis = await response.parse()
        assert medication_analysis is None

    @parametrize
    async def test_streaming_response_summary(self, async_client: AsyncCzlai) -> None:
        async with async_client.medication_analysis.with_streaming_response.summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            medication_analysis = await response.parse()
            assert medication_analysis is None

        assert cast(Any, response.is_closed) is True
