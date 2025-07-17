"""
Offering class v2 - Python conversion from Java
Enhanced offering with better encapsulation and validation
Maintains exact OOP structure and business logic
"""

from datetime import date
from typing import Set
from python.ch2.v1.employee import Employee
from .training import Training


class OfferingIsFullException(Exception):
    """Exception raised when offering has no available spots"""
    pass


class Offering:
    """Training offering with enhanced enrollment management"""
    
    def __init__(self, training: Training, date_: date, maximum_number_of_attendees: int):
        self._id: int = None
        self._training = training
        self._date = date_
        self._employees: Set[Employee] = set()
        self._maximum_number_of_attendees = maximum_number_of_attendees
        self._available_spots = maximum_number_of_attendees
    
    @property
    def employees(self) -> Set[Employee]:
        """Get immutable copy of enrolled employees"""
        return frozenset(self._employees)  # Return immutable set
    
    @available_spots.setter
    def available_spots(self, available_spots: int) -> None:
        """Set available spots"""
        self._available_spots = available_spots
    
    def add_employee(self, employee: Employee) -> None:
        """Add employee to offering with validation"""
        if self._available_spots == 0:
            raise OfferingIsFullException()
        
        self._employees.add(employee)
        self._available_spots -= 1
    
    def has_available_spots(self) -> bool:
        """Check if offering has available spots"""
        return self._available_spots > 0
    
    @property
    def available_spots(self) -> int:
        """Get number of available spots"""
        return self._available_spots
    
    @property
    def training(self) -> Training:
        """Get training for this offering"""
        return self._training
    
    def is_employee_registered(self, employee: Employee) -> bool:
        """Check if employee is registered for this offering"""
        return employee in self._employees