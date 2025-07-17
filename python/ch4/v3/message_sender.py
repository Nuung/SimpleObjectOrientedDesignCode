"""
Message Sender v3 - Python conversion from Java
Refactored version using MessageBot for sending messages
"""

from typing import List

from python.ch4.v1.message_sender import MessageRepository, Message
from python.ch4.v2.message_sender import EmailSender, UserPreferences
from python.ch4.v3.message_bot import MessageBot


class MessageSender:
    """
    Service for sending messages via multiple channels, utilizing a MessageBot.
    """

    def __init__(
        self,
        message_bot: MessageBot,
        repository: MessageRepository,
        email_sender: EmailSender,  # 1
        user_prefs: UserPreferences,  # 1
    ):
        self._message_bot = message_bot
        self._repository = repository
        self._email_sender = email_sender
        self._user_prefs = user_prefs

    def send_messages(self) -> None:
        """Send all messages that need to be sent."""
        messages_to_be_sent = self._repository.get_messages_to_be_sent()
        for message_to_be_sent in messages_to_be_sent:
            self._message_bot.send(message_to_be_sent)
            if self._user_prefs.send_via_email(message_to_be_sent.email):  # 2
                self._email_sender.send_message(message_to_be_sent)
            # 메시지를 보낸 것으로 표시한다
            message_to_be_sent.mark_as_sent()
