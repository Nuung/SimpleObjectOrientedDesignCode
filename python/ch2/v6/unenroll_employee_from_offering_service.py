"""
Unenroll Employee From Offering Service v6 - Python conversion from Java
Refactored version with a dedicated notifier class
Maintains exact OOP structure and separation of concerns
"""

from typing import Set

from python.ch2.v1.employee import Employee
from python.ch2.v5.offering import Offering
from python.ch2.v5.emailer import Emailer
from python.ch2.v5.offering_repository import OfferingRepository


class UnenrollEmployeeFromOfferingService:
    """Service for unenrolling an employee from an offering"""

    def __init__(self, offerings: OfferingRepository, notifier: "WaitingListNotifier"):
        self._offerings = offerings
        self._notifier = notifier  # 1

    def unenroll(self, enrollment_id: int) -> None:
        """Unenroll an employee and notify the waiting list"""
        # ...
        # 직원 등록 취소 로직
        # ...
        offering = self._offerings.get_offering_from(enrollment_id)
        self._notifier.notify(offering)  # 2


class WaitingListNotifier:
    """Notifier for employees on the waiting list"""

    def __init__(self, emailer: Emailer):  # 3
        self._emailer = emailer

    def notify(self, offering: Offering) -> None:  # 4
        """Notify all employees on the waiting list"""
        employees: Set[Employee] = offering.get_waiting_list()
        for employee in employees:
            self._emailer.send_waiting_list_email(offering, employee)
