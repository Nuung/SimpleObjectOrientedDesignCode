"""
Badge Giver v4 - Python conversion from Java
Refactored version with a static method to create rules
"""

from typing import List

from python.ch5.v1.employee import Employee
from python.ch5.v1.badge import Badge
from python.ch5.v4.badge_rule import BadgeRule, BadgeForTrainings, BadgeForQuantity


class BadgeGiver:
    """Assigns badges to employees based on a list of rules"""

    def __init__(self, rules: List[BadgeRule]):  # 1
        self._rules = rules

    def give(self, employee: Employee) -> None:
        """Applies each rule to the employee and assigns badges accordingly"""
        for rule in self._rules:  # 2
            if rule.give(employee):
                employee.win_badge(rule.badge_to_give())

    @staticmethod
    def create_rules() -> List[BadgeRule]:
        """Creates a predefined list of badge rules"""
        quality_hero = BadgeForTrainings(
            ["TESTING", "CODE QUALITY"],
            Badge.QUALITY_HERO,
        )  # 4
        security_cop = BadgeForTrainings(
            ["SECURITY 101", "SECURITY FOR MOBILE DEVS"],
            Badge.SECURITY_COP,
        )  # 5
        five_trainings = BadgeForQuantity(5, Badge.FIVE_TRAININGS)  # 3
        return [
            quality_hero,
            security_cop,
            five_trainings,
        ]
