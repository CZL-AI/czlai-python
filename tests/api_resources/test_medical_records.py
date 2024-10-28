# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai
from czlai.types import (
    MedicalRecordRetrieveResponse,
    MedicalRecordCreateListResponse,
)
from tests.utils import assert_matches_type
from czlai._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMedicalRecords:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Czlai) -> None:
        medical_record = client.medical_records.retrieve(
            report_id=0,
        )
        assert_matches_type(MedicalRecordRetrieveResponse, medical_record, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Czlai) -> None:
        response = client.medical_records.with_raw_response.retrieve(
            report_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        medical_record = response.parse()
        assert_matches_type(MedicalRecordRetrieveResponse, medical_record, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Czlai) -> None:
        with client.medical_records.with_streaming_response.retrieve(
            report_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            medical_record = response.parse()
            assert_matches_type(MedicalRecordRetrieveResponse, medical_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Czlai) -> None:
        medical_record = client.medical_records.update()
        assert medical_record is None

    @parametrize
    def test_method_update_with_all_params(self, client: Czlai) -> None:
        medical_record = client.medical_records.update(
            is_read=0,
            report_id=0,
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            stage="stage",
            status=0,
        )
        assert medical_record is None

    @parametrize
    def test_raw_response_update(self, client: Czlai) -> None:
        response = client.medical_records.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        medical_record = response.parse()
        assert medical_record is None

    @parametrize
    def test_streaming_response_update(self, client: Czlai) -> None:
        with client.medical_records.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            medical_record = response.parse()
            assert medical_record is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_list(self, client: Czlai) -> None:
        medical_record = client.medical_records.create_list()
        assert_matches_type(MedicalRecordCreateListResponse, medical_record, path=["response"])

    @parametrize
    def test_method_create_list_with_all_params(self, client: Czlai) -> None:
        medical_record = client.medical_records.create_list(
            limit=0,
            module_type=[0, 0, 0],
            page=0,
            pet_profile_id=[0, 0, 0],
        )
        assert_matches_type(MedicalRecordCreateListResponse, medical_record, path=["response"])

    @parametrize
    def test_raw_response_create_list(self, client: Czlai) -> None:
        response = client.medical_records.with_raw_response.create_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        medical_record = response.parse()
        assert_matches_type(MedicalRecordCreateListResponse, medical_record, path=["response"])

    @parametrize
    def test_streaming_response_create_list(self, client: Czlai) -> None:
        with client.medical_records.with_streaming_response.create_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            medical_record = response.parse()
            assert_matches_type(MedicalRecordCreateListResponse, medical_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_ongoing_record(self, client: Czlai) -> None:
        medical_record = client.medical_records.ongoing_record(
            module_type=0,
            pet_profile_id=0,
        )
        assert medical_record is None

    @parametrize
    def test_raw_response_ongoing_record(self, client: Czlai) -> None:
        response = client.medical_records.with_raw_response.ongoing_record(
            module_type=0,
            pet_profile_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        medical_record = response.parse()
        assert medical_record is None

    @parametrize
    def test_streaming_response_ongoing_record(self, client: Czlai) -> None:
        with client.medical_records.with_streaming_response.ongoing_record(
            module_type=0,
            pet_profile_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            medical_record = response.parse()
            assert medical_record is None

        assert cast(Any, response.is_closed) is True


class TestAsyncMedicalRecords:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCzlai) -> None:
        medical_record = await async_client.medical_records.retrieve(
            report_id=0,
        )
        assert_matches_type(MedicalRecordRetrieveResponse, medical_record, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCzlai) -> None:
        response = await async_client.medical_records.with_raw_response.retrieve(
            report_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        medical_record = await response.parse()
        assert_matches_type(MedicalRecordRetrieveResponse, medical_record, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCzlai) -> None:
        async with async_client.medical_records.with_streaming_response.retrieve(
            report_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            medical_record = await response.parse()
            assert_matches_type(MedicalRecordRetrieveResponse, medical_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncCzlai) -> None:
        medical_record = await async_client.medical_records.update()
        assert medical_record is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCzlai) -> None:
        medical_record = await async_client.medical_records.update(
            is_read=0,
            report_id=0,
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            stage="stage",
            status=0,
        )
        assert medical_record is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCzlai) -> None:
        response = await async_client.medical_records.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        medical_record = await response.parse()
        assert medical_record is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCzlai) -> None:
        async with async_client.medical_records.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            medical_record = await response.parse()
            assert medical_record is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_list(self, async_client: AsyncCzlai) -> None:
        medical_record = await async_client.medical_records.create_list()
        assert_matches_type(MedicalRecordCreateListResponse, medical_record, path=["response"])

    @parametrize
    async def test_method_create_list_with_all_params(self, async_client: AsyncCzlai) -> None:
        medical_record = await async_client.medical_records.create_list(
            limit=0,
            module_type=[0, 0, 0],
            page=0,
            pet_profile_id=[0, 0, 0],
        )
        assert_matches_type(MedicalRecordCreateListResponse, medical_record, path=["response"])

    @parametrize
    async def test_raw_response_create_list(self, async_client: AsyncCzlai) -> None:
        response = await async_client.medical_records.with_raw_response.create_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        medical_record = await response.parse()
        assert_matches_type(MedicalRecordCreateListResponse, medical_record, path=["response"])

    @parametrize
    async def test_streaming_response_create_list(self, async_client: AsyncCzlai) -> None:
        async with async_client.medical_records.with_streaming_response.create_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            medical_record = await response.parse()
            assert_matches_type(MedicalRecordCreateListResponse, medical_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_ongoing_record(self, async_client: AsyncCzlai) -> None:
        medical_record = await async_client.medical_records.ongoing_record(
            module_type=0,
            pet_profile_id=0,
        )
        assert medical_record is None

    @parametrize
    async def test_raw_response_ongoing_record(self, async_client: AsyncCzlai) -> None:
        response = await async_client.medical_records.with_raw_response.ongoing_record(
            module_type=0,
            pet_profile_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        medical_record = await response.parse()
        assert medical_record is None

    @parametrize
    async def test_streaming_response_ongoing_record(self, async_client: AsyncCzlai) -> None:
        async with async_client.medical_records.with_streaming_response.ongoing_record(
            module_type=0,
            pet_profile_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            medical_record = await response.parse()
            assert medical_record is None

        assert cast(Any, response.is_closed) is True
