# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import search_execute_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.search_result_snippets import SearchResultSnippets

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/justement-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/justement-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def execute(
        self,
        *,
        classification_facet: List[str] | NotGiven = NOT_GIVEN,
        language: Literal["de", "en", "fr", "it", "rm"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchResultSnippets:
        """
        Search Justement and receive a result page with up to 10 snippets of matching
        documents, ranked by relevance.

        Args:
          classification_facet: **Classification facet**: Filters results based on hierarchical categories. Each
              element in the list represents a level in the hierarchy:

              - `["Staatsrecht", "Grundrecht"]`: filters to Staatsrecht (Public Law) and
                Grundrecht (Fundamental Rights).
              - `["Privatrecht", "Zivilrecht", "Vertragsrecht"]`: filters to Privatrecht
                (Private Law), Zivilrecht (Civil Law), and Vertragsrecht (Contract Law).
              - `["Strafrecht", "Straftaten"]`: filters to Strafrecht (Criminal Law) and
                Straftaten (Offenses).

              See the full classification hierarchy:

              ```plaintext
              Staatsrecht
              ├── Abgaberecht & öffentliche Finanzen
              ├── Bau- & Planungsrecht
              ├── Bürger- & Ausländerrecht
              ├── Energie/Verkehr/Medien
              │   └── Verkehr
              ├── Grundrecht
              ├── Gesundheit & soziale Sicherheit
              ├── Öffentliches Dienstverhältnis
              ├── Ökologisches Gleichgewicht
              ├── Politische Rechte
              ├── Rechtshilfe & Auslieferung
              ├── Schuldbetreibungs- & Konkursrecht
              ├── Sozialversicherungsrecht
              │   ├── AHV
              │   ├── ALV
              │   ├── BV
              │   ├── EL
              │   ├── IV
              │   ├── KV
              │   └── UV
              ├── Unterrichtswesen & Berufsausbildung
              ├── Verfahren
              │   ├── Strafprozess
              │   ├── Zivilprozess
              │   └── Zuständigkeitsfragen
              └── Verfahrensrecht

              Privatrecht
              ├── Immaterialgüter-, Wettbewerbs- & Kartellrecht
              ├── Obligationen- & Handelsrecht
              │   ├── Gesellschaftsrecht
              │   ├── Haftpflichtrecht
              │   ├── Obligationsrecht (allgemein)
              │   └── Vertragsrecht
              └── Zivilrecht
                 ├── Erbrecht
                 ├── Familienrecht
                 ├── Personenrecht
                 └── Sachenrecht

              Strafrecht
              ├── Straf- & Massnahmenvollzug
              ├── Straftaten
              └── Strafrecht (allgemein)
              ```

          language: Preferred language for snippets.

          page: Result page (1-based). Maximum page is total results / 10 rounded up.

          query: **Search query**: Retrieves the count of documents matching the criteria.

              - Terms are **implicitly ANDed** (e.g., `hund biss` only matches documents
                containing both terms).
              - Supports **exact phrases** (e.g., `"hund spazieren"`) and **proximity
                searches** (e.g., `"hund biss"~10`).
              - **Excludes terms** with `-term` (e.g., `beschattung -besonnung`).
              - **Prefix search** with `term*` for terms with at least 3 characters.
              - **Synonym expansion and translations** with lower relevance ranking.

              For advanced operators and tips, see
              [Justement Search Tips](https://justement.ch/en/search).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "classification_facet": classification_facet,
                        "language": language,
                        "page": page,
                        "query": query,
                    },
                    search_execute_params.SearchExecuteParams,
                ),
            ),
            cast_to=SearchResultSnippets,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/justement-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/justement-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def execute(
        self,
        *,
        classification_facet: List[str] | NotGiven = NOT_GIVEN,
        language: Literal["de", "en", "fr", "it", "rm"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchResultSnippets:
        """
        Search Justement and receive a result page with up to 10 snippets of matching
        documents, ranked by relevance.

        Args:
          classification_facet: **Classification facet**: Filters results based on hierarchical categories. Each
              element in the list represents a level in the hierarchy:

              - `["Staatsrecht", "Grundrecht"]`: filters to Staatsrecht (Public Law) and
                Grundrecht (Fundamental Rights).
              - `["Privatrecht", "Zivilrecht", "Vertragsrecht"]`: filters to Privatrecht
                (Private Law), Zivilrecht (Civil Law), and Vertragsrecht (Contract Law).
              - `["Strafrecht", "Straftaten"]`: filters to Strafrecht (Criminal Law) and
                Straftaten (Offenses).

              See the full classification hierarchy:

              ```plaintext
              Staatsrecht
              ├── Abgaberecht & öffentliche Finanzen
              ├── Bau- & Planungsrecht
              ├── Bürger- & Ausländerrecht
              ├── Energie/Verkehr/Medien
              │   └── Verkehr
              ├── Grundrecht
              ├── Gesundheit & soziale Sicherheit
              ├── Öffentliches Dienstverhältnis
              ├── Ökologisches Gleichgewicht
              ├── Politische Rechte
              ├── Rechtshilfe & Auslieferung
              ├── Schuldbetreibungs- & Konkursrecht
              ├── Sozialversicherungsrecht
              │   ├── AHV
              │   ├── ALV
              │   ├── BV
              │   ├── EL
              │   ├── IV
              │   ├── KV
              │   └── UV
              ├── Unterrichtswesen & Berufsausbildung
              ├── Verfahren
              │   ├── Strafprozess
              │   ├── Zivilprozess
              │   └── Zuständigkeitsfragen
              └── Verfahrensrecht

              Privatrecht
              ├── Immaterialgüter-, Wettbewerbs- & Kartellrecht
              ├── Obligationen- & Handelsrecht
              │   ├── Gesellschaftsrecht
              │   ├── Haftpflichtrecht
              │   ├── Obligationsrecht (allgemein)
              │   └── Vertragsrecht
              └── Zivilrecht
                 ├── Erbrecht
                 ├── Familienrecht
                 ├── Personenrecht
                 └── Sachenrecht

              Strafrecht
              ├── Straf- & Massnahmenvollzug
              ├── Straftaten
              └── Strafrecht (allgemein)
              ```

          language: Preferred language for snippets.

          page: Result page (1-based). Maximum page is total results / 10 rounded up.

          query: **Search query**: Retrieves the count of documents matching the criteria.

              - Terms are **implicitly ANDed** (e.g., `hund biss` only matches documents
                containing both terms).
              - Supports **exact phrases** (e.g., `"hund spazieren"`) and **proximity
                searches** (e.g., `"hund biss"~10`).
              - **Excludes terms** with `-term` (e.g., `beschattung -besonnung`).
              - **Prefix search** with `term*` for terms with at least 3 characters.
              - **Synonym expansion and translations** with lower relevance ranking.

              For advanced operators and tips, see
              [Justement Search Tips](https://justement.ch/en/search).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "classification_facet": classification_facet,
                        "language": language,
                        "page": page,
                        "query": query,
                    },
                    search_execute_params.SearchExecuteParams,
                ),
            ),
            cast_to=SearchResultSnippets,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.execute = to_raw_response_wrapper(
            search.execute,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.execute = async_to_raw_response_wrapper(
            search.execute,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.execute = to_streamed_response_wrapper(
            search.execute,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.execute = async_to_streamed_response_wrapper(
            search.execute,
        )
