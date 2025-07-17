"""
Add Employee to Offering Service v2 - Python conversion from Java
Enhanced service with validation for enrolling employees
"""

from python.ch2.v1.employee_repository import EmployeeRepository
from python.ch3.v2.offering_repository import OfferingRepository
from python.ch3.v2.add_employee_to_offering_validator import (
    AddEmployeeToOfferingValidator,
    ValidationException,
)
from python.ch3.v2.invalid_request_exception import InvalidRequestException


class AddEmployeeToOfferingService:
    """Service for adding an employee to a training offering with validation"""

    def __init__(
        self,
        offerings: OfferingRepository,
        employees: EmployeeRepository,
        validator: AddEmployeeToOfferingValidator,
    ):
        self._offerings = offerings
        self._employees = employees
        self._validator = validator

    def add_employee(self, offering_id: int, employee_email: str) -> None:
        """Add an employee to an offering after validation"""
        offering_opt = self._offerings.find_by_id(offering_id)
        employee_opt = self._employees.find_by_email(employee_email)

        if not offering_opt or not employee_opt:  # 1
            raise InvalidRequestException("Offering and employee IDs should be valid")

        offering = offering_opt
        employee = employee_opt

        validation = self._validator.validate(offering, employee)  # 2
        if validation.has_errors():  # 3
            raise ValidationException(validation)

        offering.add_employee(employee)  # 4
