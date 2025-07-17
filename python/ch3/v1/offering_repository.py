"""
Offering Repository Interface v1 - Python conversion from Java
Initial interface for offering data access
"""

from abc import ABC, abstractmethod

from python.ch3.v1.offering import Offering


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
    def get_offering_from(self, id_: int) -> Offering:
        """Retrieve an offering by its ID"""
        pass
