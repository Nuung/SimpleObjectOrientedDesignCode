"""
Message Sender v1 - Python conversion from Java
Initial version of the message sending service
"""

from typing import List


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


class Bot:
    """Interface for a message sending bot"""

    def send_private_message(self, user_id: str, message_to_be_sent: str) -> None:
        """Send a private message to a user"""
        pass


class UserDirectory:
    """Interface for a user directory"""

    def get_account(self, email: str) -> str:
        """Get a user's account ID from their email address"""
        pass


class MessageRepository:
    """Interface for a message repository"""

    def get_messages_to_be_sent(self) -> List[Message]:
        """Get a list of messages to be sent"""
        pass


class MessageSender:
    """Service for sending messages"""

    def __init__(
        self, bot: Bot, user_directory: UserDirectory, repository: MessageRepository
    ):
        self._bot = bot
        self._user_directory = user_directory
        self._repository = repository

    def send_messages(self) -> None:
        """Send all messages that need to be sent"""
        messages_to_be_sent = self._repository.get_messages_to_be_sent()
        for message_to_be_sent in messages_to_be_sent:  # 1
            user_id = self._user_directory.get_account(
                message_to_be_sent.email
            )  # 2
            self._bot.send_private_message(
                user_id, message_to_be_sent.body_in_markdown
            )  # 3
            message_to_be_sent.mark_as_sent()  # 4
