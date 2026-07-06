from models.message import Message


class ConversationHistory:
    def __init__(self):
        self.messages = []

    def add_user_message(self, content: str):
        self.messages.append(
            Message("user", content)
        )

    def add_ai_message(self, content: str):
        self.messages.append(
            Message("assistant", content)
        )

    def get_messages(self):
        return self.messages