"""
Enrollment class - Python conversion from Java
Represents an employee's enrollment in a training offering
"""

from datetime import date
from typing import Optional

from python.ch5.v1.employee import Employee


class Enrollment:
    """Represents an employee's enrollment in a training offering"""

    def __init__(self, employee: Employee, date_of_enrollment: date):
        self._employee = employee
        self._date_of_enrollment = date_of_enrollment
        self._status = True
        self._date_of_cancellation: Optional[date] = None

    def cancel(self, date_of_cancellation: date) -> None:
        """Cancel the enrollment"""
        self._status = False
        self._date_of_cancellation = date_of_cancellation

    @property
    def employee(self) -> Employee:
        """Get the enrolled employee"""
        return self._employee

    # getters
