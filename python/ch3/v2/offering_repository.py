"""
Offering Repository Interface v2 - Python conversion from Java
Enhanced interface for offering data access
"""

from abc import ABC, abstractmethod
from typing import Optional

from python.ch3.v2.offering import Offering


class OfferingRepository(ABC):
    """Abstract repository for managing training offerings"""

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
        """Find an offering by its ID"""
        pass

    @abstractmethod
    def get_offering_from(self, enrollment_id: int) -> Offering:
        """Get an offering from an enrollment ID"""
        pass
