"""
Dispatch Time Enum - Python conversion from Java
Defines various dispatch times for notifications
"""

from enum import Enum


class DispatchTime(Enum):
    """Enum representing different notification dispatch times"""

    RIGHT_NOW = "RIGHT_NOW"
    ONE_WEEK_BEFORE = "ONE_WEEK_BEFORE"
    DAY_BEFORE = "DAY_BEFORE"
    ONE_HOUR_BEFORE = "ONE_HOUR_BEFORE"
