"""
Badge For Trainings Factory - Python conversion from Java
Factory for creating badge rules based on specific training completions
"""

from typing import List

from python.ch5.v1.employee import Employee
from python.ch5.v1.badge import Badge
from python.ch5.v1.trainings_taken import TrainingsTaken
from python.ch5.v4.badge_rule import BadgeRule
from python.ch5.v5.badge_rule_factory import BadgeRuleFactory


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


class BadgeForTrainingsFactory(BadgeRuleFactory):
    """Factory for creating BadgeForTrainings rules"""

    def create_rules(self) -> List[BadgeRule]:
        """Creates and returns a list of BadgeForTrainings rules"""
        # DB에 접근해 데이터를 얻고,
        # 각각의 데이터에 대해 BadgeForQuantity 클래스를 인스턴스화한다
        # 다음은 그냥 결과만 돌려줌
        return [
            BadgeForTrainings(
                ["TESTING", "CODE QUALITY"],
                Badge.QUALITY_HERO,
            ),
            BadgeForTrainings(
                ["SECURITY 101", "SECURITY FOR MOBILE DEVS"],
                Badge.SECURITY_COP,
            ),
        ]
