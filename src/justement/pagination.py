# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional, cast
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncPageNumberPagination", "AsyncPageNumberPagination"]

_T = TypeVar("_T")


class SyncPageNumberPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    result_count: Optional[object] = None
    results: Optional[object] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


class AsyncPageNumberPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    result_count: Optional[object] = None
    results: Optional[object] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})
