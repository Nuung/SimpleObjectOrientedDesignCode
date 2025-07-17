"""
Offering Repository Interface - Python conversion from Java
Maintains exact OOP structure and interface design
"""

from abc import ABC, abstractmethod
from typing import Optional

from python.ch6.v1.offering import Offering
from python.ch6.v1.enrollment import Enrollment


class OfferingRepository(ABC):
    """Abstract repository interface for Offering operations"""

    @abstractmethod
    def save(self, offering: Offering) -> None:
        """Save offering to repository"""
        pass

    @abstractmethod
    def update(self, offering: Offering) -> None:
        """Update existing offering in repository"""
        pass

    @abstractmethod
    def find_by_id(self, id_: int) -> Optional[Offering]:
        """Find offering by ID"""
        pass

    @abstractmethod
    def get_by_id(self, id_: int) -> Offering:
        """Get offering by ID"""
        pass

    @abstractmethod
    def get_offering_from(self, enrollment_id: int) -> Offering:
        """Get offering from enrollment ID"""
        pass

    @abstractmethod
    def get_enrollment(self, offering_id: int, employee_id: int) -> Enrollment:
        """Get enrollment by offering ID and employee ID"""
        pass
