"""
Add Employee to Offering Validator v1 - Python conversion from Java
Validator for business rules before enrolling an employee
"""

from typing import List

from python.ch5.v1.offering import Offering
from python.ch5.v1.employee import Employee
from python.ch5.v1.training_repository import TrainingRepository


class ValidationResult:
    """Result of a validation check, containing errors if any"""

    def __init__(self):
        self.errors: List[str] = []

    def has_errors(self) -> bool:
        """Check if there are any validation errors"""
        return bool(self.errors)

    def add_error(self, error: str) -> None:
        """Add a validation error message"""
        self.errors.append(error)


class ValidationException(Exception):
    """Exception raised for validation failures"""

    def __init__(self, validation_result: ValidationResult):
        self.validation_result = validation_result
        super().__init__(f"Validation failed with errors: {validation_result.errors}")


class AddEmployeeToOfferingValidator:
    """Validator for adding an employee to a training offering"""

    def __init__(self, trainings: TrainingRepository):
        self._trainings = trainings

    def validate(self, offering: Offering, employee: Employee) -> ValidationResult:
        """Validate if an employee can be added to an offering"""
        validation = ValidationResult()

        if not offering.has_available_spots():  # 1
            validation.add_error("Offering has no available spots.")

        times_participant_took_the_training = self._trainings.count_participations(
            employee, offering.training
        )

        if times_participant_took_the_training >= 3:  # 2
            validation.add_error("Participant can't take the training again.")

        if offering.is_employee_registered(employee):
            validation.add_error("Participant already in this offering.")

        return validation
