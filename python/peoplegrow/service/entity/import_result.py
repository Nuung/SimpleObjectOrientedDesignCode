from typing import List, Collection
from peoplegrow.entity.employee import Employee


class ImportResult:
    def __init__(self):
        self._employees: List[Employee] = []

    def added_new_employee(self, new_employee: Employee) -> None:
        self._employees.append(new_employee)

    def updated_employee(self, updated_employee: Employee) -> None:
        # Remove existing employee with same email and add updated one
        self._employees = [
            emp for emp in self._employees if emp.email != updated_employee.email
        ]
        self._employees.append(updated_employee)

    @property
    def employees(self) -> Collection[Employee]:
        # Return an immutable collection (tuple in Python) of employees
        return tuple(self._employees)
