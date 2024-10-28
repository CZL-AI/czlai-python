# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    aidoc_exotic_report_params,
    aidoc_exotic_options_params,
    aidoc_exotic_keywords_params,
    aidoc_exotic_question_params,
    aidoc_exotic_summarize_params,
    aidoc_exotic_pic_result_params,
    aidoc_exotic_report_task_params,
    aidoc_exotic_ask_continue_params,
    aidoc_exotic_if_need_image_params,
)
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
from ..types.aidoc_exotic_keywords_response import AidocExoticKeywordsResponse

__all__ = ["AidocExoticResource", "AsyncAidocExoticResource"]


class AidocExoticResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AidocExoticResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AidocExoticResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AidocExoticResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AidocExoticResourceWithStreamingResponse(self)

    def ask_continue(
        self,
        *,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        判断是否需要继续提问

        Args:
          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/aidoc-exotic/if-continue-ask",
            body=maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aidoc_exotic_ask_continue_params.AidocExoticAskContinueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def if_need_image(
        self,
        *,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        判断是否需要传图

        Args:
          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/aidoc-exotic/if-need-image",
            body=maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aidoc_exotic_if_need_image_params.AidocExoticIfNeedImageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def keywords(
        self,
        *,
        content: str | NotGiven = NOT_GIVEN,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AidocExoticKeywordsResponse:
        """
        获取关键词,科室

        Args:
          content: 用户主诉

          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/aidoc-exotic/keywords",
            body=maybe_transform(
                {
                    "content": content,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aidoc_exotic_keywords_params.AidocExoticKeywordsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AidocExoticKeywordsResponse,
        )

    def options(
        self,
        *,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        question: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        获取问题选项

        Args:
          pet_profile_id: 宠物档案 id

          question: 问题

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/aidoc-exotic/options",
            body=maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "question": question,
                    "session_id": session_id,
                },
                aidoc_exotic_options_params.AidocExoticOptionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def pic_result(
        self,
        *,
        img_url: str | NotGiven = NOT_GIVEN,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取图片结果(流式)

        Args:
          img_url: 图片 url

          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/aidoc-exotic/pic-result",
            body=maybe_transform(
                {
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aidoc_exotic_pic_result_params.AidocExoticPicResultParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def question(
        self,
        *,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        获取问题(流式)

        Args:
          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/aidoc-exotic/question",
            body=maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aidoc_exotic_question_params.AidocExoticQuestionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def report(
        self,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        发布获取诊断报告任务

        Args:
          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/aidoc-exotic/report",
            body=maybe_transform({"session_id": session_id}, aidoc_exotic_report_params.AidocExoticReportParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def report_task(
        self,
        *,
        session_id: str,
        report_type: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取诊断报告

        Args:
          session_id: 会话 id

          report_type: 报告类型

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/aidoc-exotic/report-task",
            body=maybe_transform(
                {
                    "session_id": session_id,
                    "report_type": report_type,
                },
                aidoc_exotic_report_task_params.AidocExoticReportTaskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def summarize(
        self,
        *,
        image_url: str | NotGiven = NOT_GIVEN,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取病情小结(流式)

        Args:
          image_url: 图片地址

          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/aidoc-exotic/summary",
            body=maybe_transform(
                {
                    "image_url": image_url,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aidoc_exotic_summarize_params.AidocExoticSummarizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAidocExoticResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAidocExoticResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CZL-AI/czlai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAidocExoticResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAidocExoticResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CZL-AI/czlai-python#with_streaming_response
        """
        return AsyncAidocExoticResourceWithStreamingResponse(self)

    async def ask_continue(
        self,
        *,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        判断是否需要继续提问

        Args:
          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/aidoc-exotic/if-continue-ask",
            body=await async_maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aidoc_exotic_ask_continue_params.AidocExoticAskContinueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def if_need_image(
        self,
        *,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        判断是否需要传图

        Args:
          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/aidoc-exotic/if-need-image",
            body=await async_maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aidoc_exotic_if_need_image_params.AidocExoticIfNeedImageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def keywords(
        self,
        *,
        content: str | NotGiven = NOT_GIVEN,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AidocExoticKeywordsResponse:
        """
        获取关键词,科室

        Args:
          content: 用户主诉

          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/aidoc-exotic/keywords",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aidoc_exotic_keywords_params.AidocExoticKeywordsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AidocExoticKeywordsResponse,
        )

    async def options(
        self,
        *,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        question: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        获取问题选项

        Args:
          pet_profile_id: 宠物档案 id

          question: 问题

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/aidoc-exotic/options",
            body=await async_maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "question": question,
                    "session_id": session_id,
                },
                aidoc_exotic_options_params.AidocExoticOptionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def pic_result(
        self,
        *,
        img_url: str | NotGiven = NOT_GIVEN,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取图片结果(流式)

        Args:
          img_url: 图片 url

          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/aidoc-exotic/pic-result",
            body=await async_maybe_transform(
                {
                    "img_url": img_url,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aidoc_exotic_pic_result_params.AidocExoticPicResultParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def question(
        self,
        *,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        获取问题(流式)

        Args:
          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/aidoc-exotic/question",
            body=await async_maybe_transform(
                {
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aidoc_exotic_question_params.AidocExoticQuestionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def report(
        self,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        发布获取诊断报告任务

        Args:
          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/aidoc-exotic/report",
            body=await async_maybe_transform(
                {"session_id": session_id}, aidoc_exotic_report_params.AidocExoticReportParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def report_task(
        self,
        *,
        session_id: str,
        report_type: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取诊断报告

        Args:
          session_id: 会话 id

          report_type: 报告类型

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/aidoc-exotic/report-task",
            body=await async_maybe_transform(
                {
                    "session_id": session_id,
                    "report_type": report_type,
                },
                aidoc_exotic_report_task_params.AidocExoticReportTaskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def summarize(
        self,
        *,
        image_url: str | NotGiven = NOT_GIVEN,
        pet_profile_id: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        获取病情小结(流式)

        Args:
          image_url: 图片地址

          pet_profile_id: 宠物档案 id

          session_id: 会话 id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/aidoc-exotic/summary",
            body=await async_maybe_transform(
                {
                    "image_url": image_url,
                    "pet_profile_id": pet_profile_id,
                    "session_id": session_id,
                },
                aidoc_exotic_summarize_params.AidocExoticSummarizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AidocExoticResourceWithRawResponse:
    def __init__(self, aidoc_exotic: AidocExoticResource) -> None:
        self._aidoc_exotic = aidoc_exotic

        self.ask_continue = to_raw_response_wrapper(
            aidoc_exotic.ask_continue,
        )
        self.if_need_image = to_raw_response_wrapper(
            aidoc_exotic.if_need_image,
        )
        self.keywords = to_raw_response_wrapper(
            aidoc_exotic.keywords,
        )
        self.options = to_raw_response_wrapper(
            aidoc_exotic.options,
        )
        self.pic_result = to_raw_response_wrapper(
            aidoc_exotic.pic_result,
        )
        self.question = to_raw_response_wrapper(
            aidoc_exotic.question,
        )
        self.report = to_raw_response_wrapper(
            aidoc_exotic.report,
        )
        self.report_task = to_raw_response_wrapper(
            aidoc_exotic.report_task,
        )
        self.summarize = to_raw_response_wrapper(
            aidoc_exotic.summarize,
        )


class AsyncAidocExoticResourceWithRawResponse:
    def __init__(self, aidoc_exotic: AsyncAidocExoticResource) -> None:
        self._aidoc_exotic = aidoc_exotic

        self.ask_continue = async_to_raw_response_wrapper(
            aidoc_exotic.ask_continue,
        )
        self.if_need_image = async_to_raw_response_wrapper(
            aidoc_exotic.if_need_image,
        )
        self.keywords = async_to_raw_response_wrapper(
            aidoc_exotic.keywords,
        )
        self.options = async_to_raw_response_wrapper(
            aidoc_exotic.options,
        )
        self.pic_result = async_to_raw_response_wrapper(
            aidoc_exotic.pic_result,
        )
        self.question = async_to_raw_response_wrapper(
            aidoc_exotic.question,
        )
        self.report = async_to_raw_response_wrapper(
            aidoc_exotic.report,
        )
        self.report_task = async_to_raw_response_wrapper(
            aidoc_exotic.report_task,
        )
        self.summarize = async_to_raw_response_wrapper(
            aidoc_exotic.summarize,
        )


class AidocExoticResourceWithStreamingResponse:
    def __init__(self, aidoc_exotic: AidocExoticResource) -> None:
        self._aidoc_exotic = aidoc_exotic

        self.ask_continue = to_streamed_response_wrapper(
            aidoc_exotic.ask_continue,
        )
        self.if_need_image = to_streamed_response_wrapper(
            aidoc_exotic.if_need_image,
        )
        self.keywords = to_streamed_response_wrapper(
            aidoc_exotic.keywords,
        )
        self.options = to_streamed_response_wrapper(
            aidoc_exotic.options,
        )
        self.pic_result = to_streamed_response_wrapper(
            aidoc_exotic.pic_result,
        )
        self.question = to_streamed_response_wrapper(
            aidoc_exotic.question,
        )
        self.report = to_streamed_response_wrapper(
            aidoc_exotic.report,
        )
        self.report_task = to_streamed_response_wrapper(
            aidoc_exotic.report_task,
        )
        self.summarize = to_streamed_response_wrapper(
            aidoc_exotic.summarize,
        )


class AsyncAidocExoticResourceWithStreamingResponse:
    def __init__(self, aidoc_exotic: AsyncAidocExoticResource) -> None:
        self._aidoc_exotic = aidoc_exotic

        self.ask_continue = async_to_streamed_response_wrapper(
            aidoc_exotic.ask_continue,
        )
        self.if_need_image = async_to_streamed_response_wrapper(
            aidoc_exotic.if_need_image,
        )
        self.keywords = async_to_streamed_response_wrapper(
            aidoc_exotic.keywords,
        )
        self.options = async_to_streamed_response_wrapper(
            aidoc_exotic.options,
        )
        self.pic_result = async_to_streamed_response_wrapper(
            aidoc_exotic.pic_result,
        )
        self.question = async_to_streamed_response_wrapper(
            aidoc_exotic.question,
        )
        self.report = async_to_streamed_response_wrapper(
            aidoc_exotic.report,
        )
        self.report_task = async_to_streamed_response_wrapper(
            aidoc_exotic.report_task,
        )
        self.summarize = async_to_streamed_response_wrapper(
            aidoc_exotic.summarize,
        )
