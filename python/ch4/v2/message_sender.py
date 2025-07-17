"""
Message Sender v2 - Python conversion from Java
Enhanced version with email sending capabilities
"""

from typing import List

from python.ch4.v1.message_sender import (
    Bot,
    UserDirectory,
    MessageRepository,
    Message,
)


class EmailSender:
    """Interface for an email sender"""

    def send_message(self, message: Message) -> None:
        """Send a message via email"""
        pass


class UserPreferences:
    """Interface for user preferences"""

    def send_via_email(self, email: str) -> bool:
        """Check if a user wants to receive messages via email"""
        pass


class MessageSender:
    """Service for sending messages via multiple channels"""

    def __init__(
        self,
        bot: Bot,
        user_directory: UserDirectory,
        repository: MessageRepository,
        email_sender: EmailSender,  # 1
        user_prefs: UserPreferences,  # 1
    ):
        self._bot = bot
        self._user_directory = user_directory
        self._repository = repository
        self._email_sender = email_sender
        self._user_prefs = user_prefs

    def send_messages(self) -> None:
        """Send all messages that need to be sent"""
        messages_to_be_sent = self._repository.get_messages_to_be_sent()
        for message_to_be_sent in messages_to_be_sent:
            user_id = self._user_directory.get_account(message_to_be_sent.email)
            self._bot.send_private_message(user_id, message_to_be_sent.body_in_markdown)
            if self._user_prefs.send_via_email(message_to_be_sent.email):  # 2
                self._email_sender.send_message(message_to_be_sent)
            # 메시지를 보낸 것으로 표시한다
            message_to_be_sent.mark_as_sent()
