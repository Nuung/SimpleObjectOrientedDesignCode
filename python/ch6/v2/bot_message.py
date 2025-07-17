"""
Bot Message - Python conversion from Java
Represents a message to be sent by a bot
"""


class BotMessage:
    """Represents a message to be sent by a bot"""

    def __init__(self, id_: str, message: str):
        self._id = id_
        self._message = message

    @property
    def id(self) -> str:
        return self._id

    @property
    def message(self) -> str:
        return self._message
