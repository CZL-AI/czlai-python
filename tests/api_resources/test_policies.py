# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from czlai import Czlai, AsyncCzlai

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_policy_info(self, client: Czlai) -> None:
        policy = client.policies.policy_info()
        assert policy is None

    @parametrize
    def test_method_policy_info_with_all_params(self, client: Czlai) -> None:
        policy = client.policies.policy_info(
            keys="keys",
            policy_type=0,
        )
        assert policy is None

    @parametrize
    def test_raw_response_policy_info(self, client: Czlai) -> None:
        response = client.policies.with_raw_response.policy_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert policy is None

    @parametrize
    def test_streaming_response_policy_info(self, client: Czlai) -> None:
        with client.policies.with_streaming_response.policy_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True


class TestAsyncPolicies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_policy_info(self, async_client: AsyncCzlai) -> None:
        policy = await async_client.policies.policy_info()
        assert policy is None

    @parametrize
    async def test_method_policy_info_with_all_params(self, async_client: AsyncCzlai) -> None:
        policy = await async_client.policies.policy_info(
            keys="keys",
            policy_type=0,
        )
        assert policy is None

    @parametrize
    async def test_raw_response_policy_info(self, async_client: AsyncCzlai) -> None:
        response = await async_client.policies.with_raw_response.policy_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert policy is None

    @parametrize
    async def test_streaming_response_policy_info(self, async_client: AsyncCzlai) -> None:
        async with async_client.policies.with_streaming_response.policy_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True
