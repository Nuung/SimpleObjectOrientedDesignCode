"""
Badge Rule Factory Interface - Python conversion from Java
Defines the contract for creating badge rules
"""

from abc import ABC, abstractmethod
from typing import List

from python.ch5.v4.badge_rule import BadgeRule


class BadgeRuleFactory(ABC):
    """Interface for a factory that creates badge rules"""

    @abstractmethod
    def create_rules(self) -> List[BadgeRule]:
        """Creates and returns a list of badge rules"""
        pass
