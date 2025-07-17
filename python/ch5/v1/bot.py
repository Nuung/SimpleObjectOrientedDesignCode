"""
Bot Interface - Python conversion from Java
Defines the contract for a message sending bot
"""


class Bot:
    """Interface for a message sending bot"""

    def send_private_message(self, user_id: str, message_to_be_sent: str) -> None:
        """Send a private message to a user"""
        pass
