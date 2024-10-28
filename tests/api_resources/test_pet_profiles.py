# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai
from czlai.types import (
    PetProfileListResponse,
    PetProfileDeleteResponse,
    PetProfileRetrieveResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPetProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Czlai) -> None:
        pet_profile = client.pet_profiles.create()
        assert pet_profile is None

    @parametrize
    def test_method_create_with_all_params(self, client: Czlai) -> None:
        pet_profile = client.pet_profiles.create(
            allergy_history="allergy_history",
            avatar="avatar",
            birthday="birthday",
            disease_history="disease_history",
            family_history="family_history",
            gender=0,
            is_neutered=0,
            is_vaccination=0,
            name="name",
            pet_type=0,
            pet_variety="pet_variety",
            vaccination_date="vaccination_date",
            weight="weight",
        )
        assert pet_profile is None

    @parametrize
    def test_raw_response_create(self, client: Czlai) -> None:
        response = client.pet_profiles.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet_profile = response.parse()
        assert pet_profile is None

    @parametrize
    def test_streaming_response_create(self, client: Czlai) -> None:
        with client.pet_profiles.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet_profile = response.parse()
            assert pet_profile is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Czlai) -> None:
        pet_profile = client.pet_profiles.retrieve(
            pet_profile_id=0,
        )
        assert_matches_type(PetProfileRetrieveResponse, pet_profile, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Czlai) -> None:
        response = client.pet_profiles.with_raw_response.retrieve(
            pet_profile_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet_profile = response.parse()
        assert_matches_type(PetProfileRetrieveResponse, pet_profile, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Czlai) -> None:
        with client.pet_profiles.with_streaming_response.retrieve(
            pet_profile_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet_profile = response.parse()
            assert_matches_type(PetProfileRetrieveResponse, pet_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Czlai) -> None:
        pet_profile = client.pet_profiles.update(
            pet_profile_id=0,
        )
        assert pet_profile is None

    @parametrize
    def test_method_update_with_all_params(self, client: Czlai) -> None:
        pet_profile = client.pet_profiles.update(
            pet_profile_id=0,
            allergy_history="allergy_history",
            avatar="avatar",
            birthday="birthday",
            disease_history="disease_history",
            family_history="family_history",
            gender=0,
            is_neutered=0,
            is_vaccination=0,
            name="name",
            pet_type=0,
            pet_variety="pet_variety",
            vaccination_date="vaccination_date",
            weight="weight",
        )
        assert pet_profile is None

    @parametrize
    def test_raw_response_update(self, client: Czlai) -> None:
        response = client.pet_profiles.with_raw_response.update(
            pet_profile_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet_profile = response.parse()
        assert pet_profile is None

    @parametrize
    def test_streaming_response_update(self, client: Czlai) -> None:
        with client.pet_profiles.with_streaming_response.update(
            pet_profile_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet_profile = response.parse()
            assert pet_profile is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Czlai) -> None:
        pet_profile = client.pet_profiles.list()
        assert_matches_type(PetProfileListResponse, pet_profile, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Czlai) -> None:
        response = client.pet_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet_profile = response.parse()
        assert_matches_type(PetProfileListResponse, pet_profile, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Czlai) -> None:
        with client.pet_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet_profile = response.parse()
            assert_matches_type(PetProfileListResponse, pet_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Czlai) -> None:
        pet_profile = client.pet_profiles.delete(
            pet_profile_id=0,
        )
        assert_matches_type(PetProfileDeleteResponse, pet_profile, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Czlai) -> None:
        response = client.pet_profiles.with_raw_response.delete(
            pet_profile_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet_profile = response.parse()
        assert_matches_type(PetProfileDeleteResponse, pet_profile, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Czlai) -> None:
        with client.pet_profiles.with_streaming_response.delete(
            pet_profile_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet_profile = response.parse()
            assert_matches_type(PetProfileDeleteResponse, pet_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_ex_info(self, client: Czlai) -> None:
        pet_profile = client.pet_profiles.ex_info()
        assert pet_profile is None

    @parametrize
    def test_method_ex_info_with_all_params(self, client: Czlai) -> None:
        pet_profile = client.pet_profiles.ex_info(
            pet_profile_id=0,
        )
        assert pet_profile is None

    @parametrize
    def test_raw_response_ex_info(self, client: Czlai) -> None:
        response = client.pet_profiles.with_raw_response.ex_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet_profile = response.parse()
        assert pet_profile is None

    @parametrize
    def test_streaming_response_ex_info(self, client: Czlai) -> None:
        with client.pet_profiles.with_streaming_response.ex_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet_profile = response.parse()
            assert pet_profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_variety(self, client: Czlai) -> None:
        pet_profile = client.pet_profiles.variety()
        assert_matches_type(str, pet_profile, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_variety_with_all_params(self, client: Czlai) -> None:
        pet_profile = client.pet_profiles.variety(
            user_input="虎皮鹦鹉",
        )
        assert_matches_type(str, pet_profile, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_variety(self, client: Czlai) -> None:
        response = client.pet_profiles.with_raw_response.variety()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet_profile = response.parse()
        assert_matches_type(str, pet_profile, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_variety(self, client: Czlai) -> None:
        with client.pet_profiles.with_streaming_response.variety() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet_profile = response.parse()
            assert_matches_type(str, pet_profile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPetProfiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCzlai) -> None:
        pet_profile = await async_client.pet_profiles.create()
        assert pet_profile is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCzlai) -> None:
        pet_profile = await async_client.pet_profiles.create(
            allergy_history="allergy_history",
            avatar="avatar",
            birthday="birthday",
            disease_history="disease_history",
            family_history="family_history",
            gender=0,
            is_neutered=0,
            is_vaccination=0,
            name="name",
            pet_type=0,
            pet_variety="pet_variety",
            vaccination_date="vaccination_date",
            weight="weight",
        )
        assert pet_profile is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCzlai) -> None:
        response = await async_client.pet_profiles.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet_profile = await response.parse()
        assert pet_profile is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCzlai) -> None:
        async with async_client.pet_profiles.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet_profile = await response.parse()
            assert pet_profile is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCzlai) -> None:
        pet_profile = await async_client.pet_profiles.retrieve(
            pet_profile_id=0,
        )
        assert_matches_type(PetProfileRetrieveResponse, pet_profile, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCzlai) -> None:
        response = await async_client.pet_profiles.with_raw_response.retrieve(
            pet_profile_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet_profile = await response.parse()
        assert_matches_type(PetProfileRetrieveResponse, pet_profile, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCzlai) -> None:
        async with async_client.pet_profiles.with_streaming_response.retrieve(
            pet_profile_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet_profile = await response.parse()
            assert_matches_type(PetProfileRetrieveResponse, pet_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncCzlai) -> None:
        pet_profile = await async_client.pet_profiles.update(
            pet_profile_id=0,
        )
        assert pet_profile is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCzlai) -> None:
        pet_profile = await async_client.pet_profiles.update(
            pet_profile_id=0,
            allergy_history="allergy_history",
            avatar="avatar",
            birthday="birthday",
            disease_history="disease_history",
            family_history="family_history",
            gender=0,
            is_neutered=0,
            is_vaccination=0,
            name="name",
            pet_type=0,
            pet_variety="pet_variety",
            vaccination_date="vaccination_date",
            weight="weight",
        )
        assert pet_profile is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCzlai) -> None:
        response = await async_client.pet_profiles.with_raw_response.update(
            pet_profile_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet_profile = await response.parse()
        assert pet_profile is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCzlai) -> None:
        async with async_client.pet_profiles.with_streaming_response.update(
            pet_profile_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet_profile = await response.parse()
            assert pet_profile is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncCzlai) -> None:
        pet_profile = await async_client.pet_profiles.list()
        assert_matches_type(PetProfileListResponse, pet_profile, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCzlai) -> None:
        response = await async_client.pet_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet_profile = await response.parse()
        assert_matches_type(PetProfileListResponse, pet_profile, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCzlai) -> None:
        async with async_client.pet_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet_profile = await response.parse()
            assert_matches_type(PetProfileListResponse, pet_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncCzlai) -> None:
        pet_profile = await async_client.pet_profiles.delete(
            pet_profile_id=0,
        )
        assert_matches_type(PetProfileDeleteResponse, pet_profile, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCzlai) -> None:
        response = await async_client.pet_profiles.with_raw_response.delete(
            pet_profile_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet_profile = await response.parse()
        assert_matches_type(PetProfileDeleteResponse, pet_profile, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCzlai) -> None:
        async with async_client.pet_profiles.with_streaming_response.delete(
            pet_profile_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet_profile = await response.parse()
            assert_matches_type(PetProfileDeleteResponse, pet_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_ex_info(self, async_client: AsyncCzlai) -> None:
        pet_profile = await async_client.pet_profiles.ex_info()
        assert pet_profile is None

    @parametrize
    async def test_method_ex_info_with_all_params(self, async_client: AsyncCzlai) -> None:
        pet_profile = await async_client.pet_profiles.ex_info(
            pet_profile_id=0,
        )
        assert pet_profile is None

    @parametrize
    async def test_raw_response_ex_info(self, async_client: AsyncCzlai) -> None:
        response = await async_client.pet_profiles.with_raw_response.ex_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet_profile = await response.parse()
        assert pet_profile is None

    @parametrize
    async def test_streaming_response_ex_info(self, async_client: AsyncCzlai) -> None:
        async with async_client.pet_profiles.with_streaming_response.ex_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet_profile = await response.parse()
            assert pet_profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_variety(self, async_client: AsyncCzlai) -> None:
        pet_profile = await async_client.pet_profiles.variety()
        assert_matches_type(str, pet_profile, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_variety_with_all_params(self, async_client: AsyncCzlai) -> None:
        pet_profile = await async_client.pet_profiles.variety(
            user_input="虎皮鹦鹉",
        )
        assert_matches_type(str, pet_profile, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_variety(self, async_client: AsyncCzlai) -> None:
        response = await async_client.pet_profiles.with_raw_response.variety()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet_profile = await response.parse()
        assert_matches_type(str, pet_profile, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_variety(self, async_client: AsyncCzlai) -> None:
        async with async_client.pet_profiles.with_streaming_response.variety() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet_profile = await response.parse()
            assert_matches_type(str, pet_profile, path=["response"])

        assert cast(Any, response.is_closed) is True
