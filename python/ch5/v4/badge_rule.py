"""
Badge Rule Interface and Implementations - Python conversion from Java
Defines the contract for badge rules and provides concrete implementations
"""

from abc import ABC, abstractmethod
from typing import List

from python.ch5.v1.employee import Employee
from python.ch5.v1.badge import Badge
from python.ch5.v1.trainings_taken import TrainingsTaken


class BadgeRule(ABC):
    """Interface for a badge rule"""

    @abstractmethod
    def give(self, employee: Employee) -> bool:
        """Determines if the badge should be given to the employee"""
        pass

    @abstractmethod
    def badge_to_give(self) -> Badge:
        """Returns the badge associated with this rule"""
        pass


class BadgeForTrainings(BadgeRule):
    """Badge rule based on specific training completions"""

    def __init__(self, trainings: List[str], badge_to_give: Badge):  # 1
        self._trainings = trainings
        self._badge_to_give = badge_to_give

    def give(self, employee: Employee) -> bool:
        trainings_taken: TrainingsTaken = employee.trainings_taken
        return all(trainings_taken.has(training) for training in self._trainings)  # 2

    def badge_to_give(self) -> Badge:
        return self._badge_to_give  # 3


class BadgeForQuantity(BadgeRule):
    """Badge rule based on the quantity of trainings completed"""

    def __init__(self, quantity: int, badge_to_give: Badge):  # 1
        self._quantity = quantity
        self._badge_to_give = badge_to_give

    def give(self, employee: Employee) -> bool:
        trainings_taken: TrainingsTaken = employee.trainings_taken
        return trainings_taken.total_trainings() >= self._quantity  # 2

    def badge_to_give(self) -> Badge:
        return self._badge_to_give
