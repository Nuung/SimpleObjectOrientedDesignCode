"""
Message class - Python conversion from Java
Represents a message to be sent
"""


class Message:
    """Represents a message to be sent"""

    def __init__(self, email: str, body: str):
        self._email = email
        self._body = body
        self._sent = False

    @property
    def email(self) -> str:
        """Get the recipient's email address"""
        return self._email

    @property
    def body_in_markdown(self) -> str:
        """Get the message body in Markdown format"""
        # body를 마크다운 형식으로 변환
        return self._body

    def mark_as_sent(self) -> None:
        """Mark the message as sent"""
        self._sent = True
