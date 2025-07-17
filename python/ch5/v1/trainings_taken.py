"""
Trainings Taken - Python conversion from Java
Represents the training history of an employee
"""

from datetime import date, timedelta
from typing import List

from python.ch3.v1.training import Training


class TrainingsTaken:
    """Manages the training history for an employee"""

    def __init__(self, trainings: List[Training]):
        self._trainings = trainings

    def has(self, training_name: str) -> bool:
        """Check if the employee has taken a specific training"""
        return any(training.name == training_name for training in self._trainings)

    def trainings_in_past_3_months(self) -> int:
        """Count trainings taken in the last 3 months"""
        three_months_ago = date.today() - timedelta(days=90)  # Approximately 3 months
        return sum(1 for training in self._trainings if training.end_date and training.end_date > three_months_ago)

    def total_trainings(self) -> int:
        """Get the total number of trainings taken"""
        return len(self._trainings)
