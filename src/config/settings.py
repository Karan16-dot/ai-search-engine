import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """
    Centralized application configuration.
    """

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    MODEL_NAME = "gemini-2.5-flash"

    def validate(self):
        if not self.GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY is missing. Please check your .env file."
            )

        if not self.TAVILY_API_KEY:
            raise ValueError(
                "TAVILY_API_KEY is missing. Please check your .env file."
            )


settings = Settings()
settings.validate()