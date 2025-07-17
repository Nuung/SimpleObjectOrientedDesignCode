"""
Notification class - Python conversion from Java
Represents a notification with its message, supported media, and dispatch times
"""

from typing import List

from python.ch7.v1.medium import Medium
from python.ch7.v1.dispatch_time import DispatchTime


class Notification:
    """Represents a notification with its message, supported media, and dispatch times"""

    def __init__(
        self, message: str, supported_media: List[Medium], dispatch_times: List[DispatchTime]
    ):
        self._message = message
        self._supported_media = supported_media
        self._dispatch_times = dispatch_times
