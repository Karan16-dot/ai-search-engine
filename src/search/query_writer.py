class QueryRewriter:
    """
    Rewrites user queries before sending them to the search engine.
    """

    def rewrite(self, query: str) -> str:
        """
        Currently returns the original query.

        In future versions this will:
        - expand abbreviations
        - resolve pronouns
        - use conversation history
        - optimize search keywords
        """
        return query.strip()