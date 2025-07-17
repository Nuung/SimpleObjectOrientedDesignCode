"""
Training Repository Interface - Python conversion from Java
Interface for training data access
"""

from abc import ABC, abstractmethod

from python.ch5.v1.employee import Employee
from python.ch5.v1.training import Training


class TrainingRepository(ABC):
    """Abstract repository for managing trainings"""

    @abstractmethod
    def count_participations(self, employee: Employee, training: Training) -> int:
        """Count how many times an employee has participated in a training"""
        pass
