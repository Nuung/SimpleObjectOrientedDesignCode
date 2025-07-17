"""
Medium Enum - Python conversion from Java
Defines various communication mediums for notifications
"""

from enum import Enum


class Medium(Enum):
    """Enum representing different communication mediums"""

    EMAIL = "EMAIL"
    CHAT = "CHAT"
    WHATSAPP = "WHATSAPP"
