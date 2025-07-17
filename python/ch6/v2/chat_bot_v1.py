"""
Chat Bot V1 - Python conversion from Java
Simulates a chat bot for sending messages
"""

from python.ch6.v2.bot_message import BotMessage


class ChatBotV1:
    """A simulated chat bot for sending messages"""

    def __init__(self):
        pass

    def write_message(self, message: BotMessage) -> None:
        """Sends a message by printing it to the console"""
        # send message
        print(f"Sending message: id={message.id} message={message.message}")
