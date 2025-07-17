"""
Offering class v1 - Python conversion from Java
Initial offering model with basic attributes
"""

from datetime import date
from typing import Set

from python.ch2.v1.employee import Employee
from python.ch3.v1.training import Training


class Offering:
    """Represents a training offering with enrollment details"""

    def __init__(
        self,
        training: Training,
        date_: date,
        maximum_number_of_attendees: int,
        available_spots: int,  # 2
    ):
        self._id: int = None  # 1
        self._training = training
        self._date = date_
        self._employees: Set[Employee] = set()
        self._maximum_number_of_attendees = maximum_number_of_attendees
        self._available_spots = maximum_number_of_attendees  # 3

    @property
    def employees(self) -> Set[Employee]:  # 4
        """Get the set of enrolled employees"""
        return self._employees

    @property
    def available_spots(self) -> int:  # 5
        """Get the number of available spots"""
        return self._available_spots

    @available_spots.setter
    def available_spots(self, available_spots: int) -> None:  # 6
        """Set the number of available spots"""
        self._available_spots = available_spots
