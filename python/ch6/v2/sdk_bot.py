"""
SDK Bot - Python conversion from Java
Implements the Bot interface using a ChatBotV1
"""

from python.ch5.v1.bot import Bot
from python.ch6.v2.chat_bot_v1 import ChatBotV1
from python.ch6.v2.bot_message import BotMessage


class SDKBot(Bot):
    """Implementation of the Bot interface using ChatBotV1"""

    def send_private_message(self, user_id: str, msg: str) -> None:
        """Sends a private message using ChatBotV1"""
        chat_bot = ChatBotV1()  # 1
        message = BotMessage(user_id, msg)  # 2
        chat_bot.write_message(message)  # 3
