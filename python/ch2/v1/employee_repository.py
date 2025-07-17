"""
Employee Repository Interface - Python conversion from Java
Maintains exact OOP structure and interface design
"""

from abc import ABC, abstractmethod
from typing import Optional

from python.ch2.v1.employee import Employee


class EmployeeRepository(ABC):
    """Abstract repository interface for Employee operations"""

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[Employee]:
        """Find employee by email address"""
        pass

    @abstractmethod
    def save(self, employee: Employee) -> None:
        """Save employee to repository"""
        pass

    @abstractmethod
    def update(self, employee: Employee) -> None:
        """Update existing employee in repository"""
        pass
