from search.models import SearchResult


class PromptBuilder:

    def build(
        self,
        query: str,
        results: list[SearchResult]
    ) -> str:

        prompt = f"Answer the following question using the provided search results.\n\n"

        prompt += f"Question:\n{query}\n\n"

        prompt += "Search Results:\n\n"

        for result in results:
            prompt += f"Title: {result.title}\n"
            prompt += f"URL: {result.url}\n"
            prompt += f"Content: {result.content}\n\n"

        prompt += "Provide a helpful and factual answer."

        return prompt