"""
Badge Giver v1 - Python conversion from Java
Initial version of the badge giving logic
"""

from python.ch2.v1.employee import Employee
from python.ch5.v1.badge import Badge
from python.ch5.v1.trainings_taken import TrainingsTaken


class BadgeGiver:
    """Assigns badges to employees based on their training history"""

    def give(self, employee: Employee) -> None:  # 1
        """Give badges to the employee"""
        self._per_training(employee)
        self._per_quantity(employee)

    def _per_training(self, employee: Employee) -> None:
        """Assigns badges based on specific training completions"""
        trainings_taken: TrainingsTaken = employee.trainings_taken
        # 품질 관련 교육을 받은 경우 배지를 받는다     # 2
        if trainings_taken.has("TESTING") and trainings_taken.has("CODE QUALITY"):
            self._assign(employee, Badge.QUALITY_HERO)
        # 보안 관련 교육을 모두 들으면 배지를 받는다
        if trainings_taken.has("SECURITY 101") and trainings_taken.has("SECURITY FOR MOBILE DEVS"):
            self._assign(employee, Badge.SECURITY_COP)
        # ... 다른 배치 수여 규칙들

    def _per_quantity(self, employee: Employee) -> None:  # 3
        """Assigns badges based on the quantity of trainings completed"""
        trainings_taken: TrainingsTaken = employee.trainings_taken
        if trainings_taken.total_trainings() >= 5:
            self._assign(employee, Badge.FIVE_TRAININGS)
        if trainings_taken.total_trainings() >= 10:
            self._assign(employee, Badge.TEN_TRAININGS)
        if trainings_taken.trainings_in_past_3_months() >= 3:
            self._assign(employee, Badge.ON_FIRE)

    def _assign(self, employee: Employee, badge: Badge) -> None:
        """Assign a badge to the employee"""
        employee.win_badge(badge)
