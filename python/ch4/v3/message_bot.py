"""
Message Bot - Python conversion from Java
Encapsulates the logic for sending messages via a bot
"""

from python.ch4.v1.message_sender import Bot, UserDirectory, Message


class MessageBot:
    """Handles sending messages through a bot interface"""

    def __init__(self, bot: Bot, user_directory: UserDirectory):  # 1
        self._bot = bot
        self._user_directory = user_directory

    def send(self, msg: Message) -> None:  # 2
        """Send a message to a user via the bot"""
        user_id = self._user_directory.get_account(msg.email)
        self._bot.send_private_message(user_id, msg.body_in_markdown)
