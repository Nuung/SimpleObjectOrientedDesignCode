"""
Badge Giver v3 - Python conversion from Java
Refactored version using a list of BadgeRule objects
"""

from typing import List

from python.ch5.v1.employee import Employee
from python.ch5.v1.badge import Badge
from python.ch5.v1.trainings_taken import TrainingsTaken


class BadgeRule:
    """Interface for a badge rule"""

    def give(self, employee: Employee) -> bool:
        """Determines if the badge should be given to the employee"""
        pass

    def badge_to_give(self) -> Badge:
        """Returns the badge associated with this rule"""
        pass


class QualityHero(BadgeRule):
    """Badge rule for Quality Hero badge"""

    def give(self, employee: Employee) -> bool:
        trainings_taken: TrainingsTaken = employee.trainings_taken
        return trainings_taken.has("TESTING") and trainings_taken.has("CODE QUALITY")

    def badge_to_give(self) -> Badge:
        return Badge.QUALITY_HERO


class SecurityCop(BadgeRule):
    """Badge rule for Security Cop badge"""

    def give(self, employee: Employee) -> bool:
        trainings_taken: TrainingsTaken = employee.trainings_taken
        return trainings_taken.has("SECURITY 101") and trainings_taken.has("SECURITY FOR MOBILE DEVS")

    def badge_to_give(self) -> Badge:
        return Badge.SECURITY_COP


class FiveTrainings(BadgeRule):
    """Badge rule for Five Trainings badge"""

    def give(self, employee: Employee) -> bool:
        trainings_taken: TrainingsTaken = employee.trainings_taken
        return trainings_taken.total_trainings() >= 5

    def badge_to_give(self) -> Badge:
        return Badge.FIVE_TRAININGS


class TenTrainings(BadgeRule):
    """Badge rule for Ten Trainings badge"""

    def give(self, employee: Employee) -> bool:
        trainings_taken: TrainingsTaken = employee.trainings_taken
        return trainings_taken.total_trainings() >= 10

    def badge_to_give(self) -> Badge:
        return Badge.TEN_TRAININGS


class OnFire(BadgeRule):
    """Badge rule for On Fire badge"""

    def give(self, employee: Employee) -> bool:
        trainings_taken: TrainingsTaken = employee.trainings_taken
        return trainings_taken.trainings_in_past_3_months() >= 3

    def badge_to_give(self) -> Badge:
        return Badge.ON_FIRE


class BadgeGiver:
    """Assigns badges to employees based on a list of rules"""

    def __init__(self, rules: List[BadgeRule]):  # 1
        self._rules = rules

    def give(self, employee: Employee) -> None:
        """Applies each rule to the employee and assigns badges accordingly"""
        for rule in self._rules:  # 2
            if rule.give(employee):
                employee.win_badge(rule.badge_to_give())
