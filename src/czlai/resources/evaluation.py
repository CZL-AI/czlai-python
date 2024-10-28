# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import evaluation_put_evaluation_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["EvaluationResource", "AsyncEvaluationResource"]


class EvaluationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return EvaluationResourceWithStreamingResponse(self)

    def put_evaluation(
        self,
        *,
        content: str,
        evaluation: int,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        修改评价

        Args:
          content: 文本内容

          evaluation: 评价 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/evaluation/put_evaluation",
            body=maybe_transform(
                {
                    "content": content,
                    "evaluation": evaluation,
                    "session_id": session_id,
                },
                evaluation_put_evaluation_params.EvaluationPutEvaluationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEvaluationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncEvaluationResourceWithStreamingResponse(self)

    async def put_evaluation(
        self,
        *,
        content: str,
        evaluation: int,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        修改评价

        Args:
          content: 文本内容

          evaluation: 评价 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/evaluation/put_evaluation",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "evaluation": evaluation,
                    "session_id": session_id,
                },
                evaluation_put_evaluation_params.EvaluationPutEvaluationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EvaluationResourceWithRawResponse:
    def __init__(self, evaluation: EvaluationResource) -> None:
        self._evaluation = evaluation

        self.put_evaluation = to_raw_response_wrapper(
            evaluation.put_evaluation,
        )


class AsyncEvaluationResourceWithRawResponse:
    def __init__(self, evaluation: AsyncEvaluationResource) -> None:
        self._evaluation = evaluation

        self.put_evaluation = async_to_raw_response_wrapper(
            evaluation.put_evaluation,
        )


class EvaluationResourceWithStreamingResponse:
    def __init__(self, evaluation: EvaluationResource) -> None:
        self._evaluation = evaluation

        self.put_evaluation = to_streamed_response_wrapper(
            evaluation.put_evaluation,
        )


class AsyncEvaluationResourceWithStreamingResponse:
    def __init__(self, evaluation: AsyncEvaluationResource) -> None:
        self._evaluation = evaluation

        self.put_evaluation = async_to_streamed_response_wrapper(
            evaluation.put_evaluation,
        )
