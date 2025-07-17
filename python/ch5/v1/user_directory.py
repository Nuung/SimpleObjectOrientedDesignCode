"""
User Directory Interface - Python conversion from Java
Defines the contract for a user directory service
"""


class UserDirectory:
    """Interface for a user directory"""

    def get_account(self, email: str) -> str:
        """Get a user's account ID from their email address"""
        pass
