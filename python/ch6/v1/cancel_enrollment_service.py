"""
Cancel Enrollment Service v1 - Python conversion from Java
Initial version of the service for canceling employee enrollments
"""

from datetime import date

from python.ch6.v1.offering_repository import OfferingRepository
from python.ch6.v1.enrollment import Enrollment
from python.ch6.v1.offering import Offering
from python.ch6.v1.enrollment_doesnt_exist_exception import EnrollmentDoesntExistException


class CancelEnrollmentService:
    """Service for canceling an employee's enrollment in an offering"""

    def __init__(self, offerings: OfferingRepository):
        self._offerings = offerings

    def cancel(self, offering_id: int, employee_id: int) -> None:  # 1
        """Cancel an enrollment given offering and employee IDs"""
        if offering_id <= 0 or employee_id <= 0:
            raise ValueError("Offering ID and Employee ID must be positive integers")

        offering: Offering = self._offerings.get_by_id(offering_id)
        enrollment: Enrollment = self._offerings.get_enrollment(offering_id, employee_id)  # 2

        if enrollment is None:
            raise EnrollmentDoesntExistException()

        enrollment.cancel(date.today())
        offering.increase_available_spots()  # 3
