"""
Offering class and OfferingSummary DTO - Python conversion from Java
Demonstrates converting an entity to a DTO
"""

from __future__ import annotations
from datetime import date
from typing import List

from python.ch5.v1.employee import Employee
from python.ch5.v1.training import Training
from python.ch5.v1.enrollment import Enrollment
from python.ch5.v1.employee_not_enrolled_exception import (
    EmployeeNotEnrolledException,
)
from python.ch5.v1.offering_is_full_exception import OfferingIsFullException


class OfferingSummary:
    """DTO for summarizing offering information"""

    def __init__(
        self,
        id_: int,
        training: str,
        date_: date,
        number_of_enrollments: int,
        maximum_number_of_attendants: int,
    ):
        self.id = id_
        self.training = training
        self.date = date_
        self.number_of_enrollments = number_of_enrollments
        self.maximum_number_of_attendants = maximum_number_of_attendants

    @staticmethod
    def convert(offering: "Offering") -> "OfferingSummary":
        """Convert an Offering entity to an OfferingSummary DTO"""
        return OfferingSummary(
            offering.id,
            offering.training.name,
            offering.date,
            offering.number_of_enrollments,
            offering.maximum_number_of_attendees,
        )


class Offering:
    """Represents a training offering with enrollment management"""

    def __init__(
        self, training: Training, date_: date, maximum_number_of_attendees: int
    ):
        self._id: int = None
        self._training = training
        self._date = date_
        self._enrollments: List[Enrollment] = []  # 1
        self._maximum_number_of_attendees = maximum_number_of_attendees
        self._available_spots = maximum_number_of_attendees

    def enroll(self, employee: Employee) -> None:  # 2
        """Enroll an employee in the offering"""
        if not self.has_available_spots():
            raise OfferingIsFullException()

        now = date.today()
        self._enrollments.append(Enrollment(employee, now))
        self._available_spots -= 1

    def cancel(self, employee: Employee) -> None:  # 3
        """Cancel an employee's enrollment in the offering"""
        enrollment_to_cancel = self._find_enrollment_of(employee)
        if enrollment_to_cancel is None:
            raise EmployeeNotEnrolledException()

        now = date.today()
        enrollment_to_cancel.cancel(now)

        self._available_spots += 1

    def _find_enrollment_of(self, employee: Employee) -> Enrollment | None:  # 4
        """Find the enrollment for a specific employee"""
        for enrollment in self._enrollments:
            if enrollment.employee == employee:
                return enrollment
        return None

    def has_available_spots(self) -> bool:
        """Check if there are available spots in the offering"""
        return self._available_spots > 0

    @property
    def id(self) -> int:
        """Get the offering ID"""
        return self._id

    @property
    def training(self) -> Training:
        """Get the training for this offering"""
        return self._training

    @property
    def date(self) -> date:
        """Get the date of the offering"""
        return self._date

    @property
    def number_of_enrollments(self) -> int:
        """Get the number of enrolled employees"""
        return len(self._enrollments)

    @property
    def maximum_number_of_attendees(self) -> int:
        """Get the maximum number of attendees"""
        return self._maximum_number_of_attendees

    def is_employee_registered(self, employee: Employee) -> bool:  # 5
        """Check if an employee is registered for this offering"""
        return any(enrollment.employee == employee for enrollment in self._enrollments)
