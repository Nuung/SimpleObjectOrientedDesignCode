"""
Import Result class - Python conversion from Java
Maintains exact OOP structure and encapsulation
"""

from typing import List, Collection

from python.ch2.v1.employee import Employee


class ImportResult:
    """Manages the result of employee import operations"""

    def __init__(self):
        self._employees: List[Employee] = []

    def added_new_employee(self, new_employee: Employee) -> None:
        """Add a newly created employee to the result"""
        self._employees.append(new_employee)

    def updated_employee(self, updated_employee: Employee) -> None:
        """Update an existing employee in the result"""
        # Remove existing employee with same email and add updated one
        self._employees = [
            emp for emp in self._employees if emp.email != updated_employee.email
        ]
        self._employees.append(updated_employee)

    @property
    def employees(self) -> Collection[Employee]:
        """Get immutable collection of employees"""
        return tuple(self._employees)  # Return immutable tuple instead of list
