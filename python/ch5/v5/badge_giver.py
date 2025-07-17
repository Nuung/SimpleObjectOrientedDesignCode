"""
Badge Giver v5 - Python conversion from Java
Refactored version using factories to create badge rules
"""

from typing import List

from python.ch5.v1.employee import Employee
from python.ch5.v4.badge_rule import BadgeRule
from python.ch5.v5.badge_for_quantity_factory import BadgeForQuantityFactory
from python.ch5.v5.badge_for_trainings_factory import BadgeForTrainingsFactory


class BadgeGiver:
    """Assigns badges to employees based on a list of rules provided by factories"""

    def __init__(
        self,
        quantity_factory: BadgeForQuantityFactory,
        trainings_factory: BadgeForTrainingsFactory,
    ):  # 1
        self._rules: List[BadgeRule] = []
        self._rules.extend(quantity_factory.create_rules())
        self._rules.extend(trainings_factory.create_rules())

    def give(self, employee: Employee) -> None:
        """Applies each rule to the employee and assigns badges accordingly"""
        for rule in self._rules:  # 2
            if rule.give(employee):
                employee.win_badge(rule.badge_to_give())
