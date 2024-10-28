# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import session_record_history_params
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

__all__ = ["SessionRecordsResource", "AsyncSessionRecordsResource"]


class SessionRecordsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SessionRecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return SessionRecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionRecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return SessionRecordsResourceWithStreamingResponse(self)

    def history(
        self,
        *,
        content: str,
        module_type: int,
        role: str,
        session_id: str,
        content_type: int | NotGiven = NOT_GIVEN,
        stage: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        保存聊天记录

        Args:
          content: 内容

          module_type: 1-智能问诊 2-健康检测 3-用药分析 4-知识问答 5-图像识别

          role: 角色, 取值为其中之一 ==>[user, ai]

          session_id: 会话 id

          content_type: 1-文字 2-图文

          stage: 1-用户主诉 2-用户回答 3-AI 提问 4-AI 病情小结 5-AI 病例报告 6-AI 输出 7-用户补充

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/session-record/history",
            body=maybe_transform(
                {
                    "content": content,
                    "module_type": module_type,
                    "role": role,
                    "session_id": session_id,
                    "content_type": content_type,
                    "stage": stage,
                },
                session_record_history_params.SessionRecordHistoryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSessionRecordsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSessionRecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionRecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionRecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncSessionRecordsResourceWithStreamingResponse(self)

    async def history(
        self,
        *,
        content: str,
        module_type: int,
        role: str,
        session_id: str,
        content_type: int | NotGiven = NOT_GIVEN,
        stage: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        保存聊天记录

        Args:
          content: 内容

          module_type: 1-智能问诊 2-健康检测 3-用药分析 4-知识问答 5-图像识别

          role: 角色, 取值为其中之一 ==>[user, ai]

          session_id: 会话 id

          content_type: 1-文字 2-图文

          stage: 1-用户主诉 2-用户回答 3-AI 提问 4-AI 病情小结 5-AI 病例报告 6-AI 输出 7-用户补充

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/session-record/history",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "module_type": module_type,
                    "role": role,
                    "session_id": session_id,
                    "content_type": content_type,
                    "stage": stage,
                },
                session_record_history_params.SessionRecordHistoryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SessionRecordsResourceWithRawResponse:
    def __init__(self, session_records: SessionRecordsResource) -> None:
        self._session_records = session_records

        self.history = to_raw_response_wrapper(
            session_records.history,
        )


class AsyncSessionRecordsResourceWithRawResponse:
    def __init__(self, session_records: AsyncSessionRecordsResource) -> None:
        self._session_records = session_records

        self.history = async_to_raw_response_wrapper(
            session_records.history,
        )


class SessionRecordsResourceWithStreamingResponse:
    def __init__(self, session_records: SessionRecordsResource) -> None:
        self._session_records = session_records

        self.history = to_streamed_response_wrapper(
            session_records.history,
        )


class AsyncSessionRecordsResourceWithStreamingResponse:
    def __init__(self, session_records: AsyncSessionRecordsResource) -> None:
        self._session_records = session_records

        self.history = async_to_streamed_response_wrapper(
            session_records.history,
        )
