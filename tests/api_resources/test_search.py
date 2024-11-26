# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from justement import Justement, AsyncJustement
from tests.utils import assert_matches_type
from justement.types import SearchResultSnippets

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_execute(self, client: Justement) -> None:
        search = client.search.execute()
        assert_matches_type(SearchResultSnippets, search, path=["response"])

    @parametrize
    def test_method_execute_with_all_params(self, client: Justement) -> None:
        search = client.search.execute(
            classification_facet=["string"],
            language="de",
            page=1,
            query="query",
        )
        assert_matches_type(SearchResultSnippets, search, path=["response"])

    @parametrize
    def test_raw_response_execute(self, client: Justement) -> None:
        response = client.search.with_raw_response.execute()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchResultSnippets, search, path=["response"])

    @parametrize
    def test_streaming_response_execute(self, client: Justement) -> None:
        with client.search.with_streaming_response.execute() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchResultSnippets, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_execute(self, async_client: AsyncJustement) -> None:
        search = await async_client.search.execute()
        assert_matches_type(SearchResultSnippets, search, path=["response"])

    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncJustement) -> None:
        search = await async_client.search.execute(
            classification_facet=["string"],
            language="de",
            page=1,
            query="query",
        )
        assert_matches_type(SearchResultSnippets, search, path=["response"])

    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncJustement) -> None:
        response = await async_client.search.with_raw_response.execute()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchResultSnippets, search, path=["response"])

    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncJustement) -> None:
        async with async_client.search.with_streaming_response.execute() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchResultSnippets, search, path=["response"])

        assert cast(Any, response.is_closed) is True
