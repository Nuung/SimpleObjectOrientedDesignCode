"""
Unenroll Employee From Offering Service v5 - Python conversion from Java
Maintains exact OOP structure and business logic for unenrolling employees
"""

from typing import Set

from python.ch2.v1.employee import Employee
from python.ch2.v5.offering import Offering
from python.ch2.v5.emailer import Emailer
from python.ch2.v5.offering_repository import OfferingRepository


class UnenrollEmployeeFromOfferingService:
    """Service for unenrolling an employee from an offering"""

    def __init__(self, offerings: OfferingRepository, emailer: Emailer):
        self._offerings = offerings
        self._emailer = emailer  # 1

    def unenroll(self, enrollment_id: int) -> None:
        """Unenroll an employee and notify the waiting list"""
        # ...
        # 직원 등록 취소 로직
        # ...
        offering = self._offerings.get_offering_from(enrollment_id)
        self._notify_waiting_list(offering)  # 2

    def _notify_waiting_list(self, offering: Offering) -> None:  # 3
        """Notify employees on the waiting list"""
        employees: Set[Employee] = offering.get_waiting_list()
        for employee in employees:
            self._emailer.send_waiting_list_email(offering, employee)
