"""
Add Employee to Offering Service v1 - Python conversion from Java
Initial version of the service for enrolling employees in an offering
"""

from python.ch2.v1.employee import Employee
from python.ch3.v1.offering import Offering
from python.ch3.v1.offering_repository import OfferingRepository


class AddEmployeeToOfferingService:
    """Service for enrolling an employee in a training offering"""

    def __init__(self, offerings: OfferingRepository):
        self._offerings = offerings

    def enroll(
        self, offering_id: int, employee_that_wants_to_participate: Employee
    ) -> None:
        """Enroll an employee in a specific offering"""
        offering = self._offerings.get_offering_from(offering_id)  # 1

        if offering.available_spots > 0:  # 2
            offering.employees.add(employee_that_wants_to_participate)  # 3
            offering.available_spots -= 1  # 4
