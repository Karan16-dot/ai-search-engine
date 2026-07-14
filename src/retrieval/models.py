from dataclasses import dataclass


@dataclass
class SearchResult:
    title: str
    url: str
    content: str


@dataclass
class SearchResponse:
    query: str
    results: list[SearchResult]