"""
Badge For Quantity Factory - Python conversion from Java
Factory for creating badge rules based on training quantity
"""

from typing import List

from python.ch5.v1.employee import Employee
from python.ch5.v1.badge import Badge
from python.ch5.v1.trainings_taken import TrainingsTaken
from python.ch5.v4.badge_rule import BadgeRule
from python.ch5.v5.badge_rule_factory import BadgeRuleFactory


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


class BadgeForQuantityFactory(BadgeRuleFactory):
    """Factory for creating BadgeForQuantity rules"""

    def create_rules(self) -> List[BadgeRule]:
        """Creates and returns a list of BadgeForQuantity rules"""
        # DB에 접근해 데이터를 얻고,
        # 각각의 데이터에 대해 BadgeForQuantity 클래스를 인스턴스화한다
        # 다음은 그냥 결과만 돌려줌
        return [
            BadgeForQuantity(5, Badge.FIVE_TRAININGS),
            BadgeForQuantity(10, Badge.TEN_TRAININGS),
        ]
