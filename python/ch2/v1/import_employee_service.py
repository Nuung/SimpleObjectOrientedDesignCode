"""
Import Employees Service - Python conversion from Java
Maintains exact OOP structure and business logic
"""

from typing import List

from python.ch2.v1.employee import Employee
from python.ch2.v1.employee_repository import EmployeeRepository
from python.ch2.v1.csv_parser_library import CsvParserLibrary, EmployeeParsedData, Mode
from python.ch2.v1.import_result import ImportResult


class ImportEmployeesService:
    """Service for importing employees from CSV data"""

    def __init__(self, employees: EmployeeRepository):
        self._employees = employees

    def import_from_csv_string(self, csv: str) -> ImportResult:
        """Import employees from CSV string"""
        result = ImportResult()

        csv_parser = CsvParserLibrary()
        csv_parser.set_mode(Mode.IGNORE_ERRORS)
        csv_parser.set_object_type(EmployeeParsedData)
        imported_list: List[EmployeeParsedData] = csv_parser.parse(csv)  # 1

        for employee_data in imported_list:
            maybe_an_employee = self._employees.find_by_email(employee_data.email)  # 2

            if maybe_an_employee is None:  # 3
                new_employee = Employee(
                    employee_data.name,
                    employee_data.email,
                    str(employee_data.starting_date),  # Convert date to string
                    employee_data.role,
                )

                self._employees.save(new_employee)
                result.added_new_employee(new_employee)

            else:  # 4
                current_employee = maybe_an_employee
                # Note: Original Java code has a bug - it sets same values
                # Maintaining the exact same logic as in original
                current_employee.name = current_employee.name
                current_employee.starting_date = current_employee.starting_date
                current_employee.role = current_employee.role

                self._employees.update(current_employee)
                result.updated_employee(current_employee)

        return result
