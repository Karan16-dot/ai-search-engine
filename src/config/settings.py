import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    MODEL_NAME = "gemini-2.5-flash"

    def validate(self):
        if not self.GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY is missing. Please configure your .env file."
            )


settings = Settings()
settings.validate()