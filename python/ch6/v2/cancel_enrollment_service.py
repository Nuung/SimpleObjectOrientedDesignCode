"""
Cancel Enrollment Service v2 - Python conversion from Java
Refactored version with improved error handling
"""

from datetime import date

from python.ch6.v2.offering_repository import OfferingRepository
from python.ch6.v2.enrollment import Enrollment
from python.ch6.v2.offering import Offering
from python.ch6.v2.offering_doesnt_exist_exception import OfferingDoesntExistException
from python.ch6.v2.enrollment_doesnt_exist_exception import EnrollmentDoesntExistException


class CancelEnrollmentService:
    """Service for canceling an employee's enrollment in an offering"""

    def __init__(self, offerings: OfferingRepository, enrollment: Enrollment):
        self._offerings = offerings
        self._enrollment = enrollment

    def cancel(self, offering_id: int, employee_id: int) -> None:
        """Cancel an enrollment given offering and employee IDs"""
        if offering_id <= 0 or employee_id <= 0:
            raise ValueError("Offering ID and Employee ID must be positive integers")

        offering: Offering = self._offerings.get_by_id(offering_id)
        if offering is None:
            raise OfferingDoesntExistException()

        enrollment: Enrollment = self._offerings.get_enrollment(offering_id, employee_id)
        if enrollment is None:
            raise EnrollmentDoesntExistException()

        now = date.today()
        enrollment.cancel(now)
