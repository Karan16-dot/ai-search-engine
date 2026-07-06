from dataclasses import dataclasses


@dataclass
class Message:
    role: str
    content: str