"""
Offering class v3 - Python conversion from Java
Refactored version with Enrollment aggregate root
"""

from datetime import date
from typing import List, Optional

from python.ch2.v1.employee import Employee
from python.ch3.v1.training import Training
from python.ch3.v3.enrollment import Enrollment
from python.ch3.v2.offering import OfferingIsFullException
from python.ch3.v3.employee_not_enrolled_exception import EmployeeNotEnrolledException


class Offering:
    """Represents a training offering with enrollment management"""

    def __init__(
        self,
        training: Training,
        date_: date,
        maximum_number_of_attendees: int,
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

    def _find_enrollment_of(self, employee: Employee) -> Optional[Enrollment]:  # 4
        """Find the enrollment for a specific employee"""
        for enrollment in self._enrollments:
            if enrollment.employee == employee:
                return enrollment
        return None

    def has_available_spots(self) -> bool:
        """Check if there are available spots in the offering"""
        return self._available_spots > 0

    @property
    def training(self) -> Training:
        """Get the training for this offering"""
        return self._training

    def is_employee_registered(self, employee: Employee) -> bool:  # 5
        """Check if an employee is registered for this offering"""
        return any(enrollment.employee == employee for enrollment in self._enrollments)
