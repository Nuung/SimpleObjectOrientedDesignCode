"""
Badge Enum - Python conversion from Java
Defines various badges that can be awarded to employees
"""

from enum import Enum


class Badge(Enum):
    """Enum representing different types of badges"""

    SECURITY_COP = "SECURITY_COP"
    FIVE_TRAININGS = "FIVE_TRAININGS"
    TEN_TRAININGS = "TEN_TRAININGS"
    ON_FIRE = "ON_FIRE"
    QUALITY_HERO = "QUALITY_HERO"
