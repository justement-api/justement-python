# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SearchResultSnippets", "Result"]


class Result(BaseModel):
    doc_id: str = FieldInfo(alias="docId")

    document_url: str = FieldInfo(alias="documentUrl")

    language: str

    name: str

    snippet: str

    source: str

    year: int


class SearchResultSnippets(BaseModel):
    result_count: int = FieldInfo(alias="resultCount")

    results: Optional[List[Result]] = None
