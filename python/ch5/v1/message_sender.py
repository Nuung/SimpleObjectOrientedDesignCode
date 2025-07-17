"""
Message Sender v1 - Python conversion from Java
Service for sending messages via multiple channels
"""

from abc import ABC, abstractmethod
from typing import List

from python.ch5.v1.message_bot import MessageBot
from python.ch5.v1.message import Message


class EmailSender(ABC):
    """Interface for sending emails"""

    @abstractmethod
    def send_message(self, message: Message) -> None:
        """Sends a message via email"""
        pass


class UserPreferences(ABC):
    """Interface for user communication preferences"""

    @abstractmethod
    def send_via_email(self, email: str) -> bool:
        """Checks if the user prefers to receive messages via email"""
        pass


class MessageRepository(ABC):
    """Interface for retrieving messages to be sent"""

    @abstractmethod
    def get_messages_to_be_sent(self) -> List[Message]:
        """Retrieves a list of messages that are pending to be sent"""
        pass


class MessageSender:
    """Service responsible for dispatching messages through various channels"""

    def __init__(
        self,
        message_bot: MessageBot,
        repository: MessageRepository,
        email_sender: EmailSender,
        user_prefs: UserPreferences,
    ):
        self._message_bot = message_bot
        self._repository = repository
        self._email_sender = email_sender
        self._user_prefs = user_prefs

    def send_messages(self) -> None:
        """Processes and sends all pending messages"""
        messages_to_be_sent = self._repository.get_messages_to_be_sent()
        for message_to_be_sent in messages_to_be_sent:
            self._message_bot.send(message_to_be_sent)
            if self._user_prefs.send_via_email(message_to_be_sent.email):
                self._email_sender.send_message(message_to_be_sent)
            message_to_be_sent.mark_as_sent()
