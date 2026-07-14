from retrieval.models import SearchResponse


class PromptBuilder:
    """
    Responsible for constructing prompts sent to the LLM.
    """

    SYSTEM_PROMPT = """
You are an AI Search Assistant.

Your responsibilities:

- Answer using ONLY the provided search results.
- If the answer is unavailable, clearly say so.
- Be factual.
- Be concise.
- Never hallucinate information.
- Mention sources naturally when appropriate.
"""

    def build(
        self,
        search_response: SearchResponse
    ) -> str:

        prompt = self.SYSTEM_PROMPT.strip()

        prompt += "\n\n"

        prompt += f"User Question:\n{search_response.query}\n\n"

        prompt += "Search Results:\n\n"

        for index, result in enumerate(search_response.results, start=1):

            prompt += (
                f"Result {index}\n"
                f"Title: {result.title}\n"
                f"URL: {result.url}\n"
                f"Content: {result.content}\n\n"
            )

        prompt += (
            "Answer the user's question using only the search results above."
        )

        return prompt