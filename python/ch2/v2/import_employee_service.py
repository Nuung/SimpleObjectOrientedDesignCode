"""
Import Employees Service v2 - Python conversion from Java
Refactored version with separated CSV parsing logic
Maintains exact OOP structure and separation of concerns
"""

from typing import List

from python.ch2.v1.employee import Employee
from python.ch2.v1.employee_repository import EmployeeRepository
from python.ch2.v1.csv_parser_library import CsvParserLibrary, EmployeeParsedData, Mode
from python.ch2.v1.import_result import ImportResult


class EmployeeImportCSVParser:
    """Separated CSV parsing logic for employee import"""

    def __init__(self):
        pass

    def parse(self, csv: str) -> List[EmployeeParsedData]:  # 1
        """Parse CSV string into EmployeeParsedData objects"""
        csv_parser = CsvParserLibrary()
        csv_parser.set_mode(Mode.IGNORE_ERRORS)
        csv_parser.set_object_type(EmployeeParsedData)
        return csv_parser.parse(csv)


class ImportEmployeesService:
    """Service for importing employees from CSV data - refactored version"""

    def __init__(
        self, employees: EmployeeRepository, csv_parser: EmployeeImportCSVParser
    ):  # 1
        self._employees = employees
        self._csv_parser = (
            EmployeeImportCSVParser()
        )  # Note: Creates new instance, ignoring parameter

    def import_from_csv_string(self, csv: str) -> ImportResult:
        """Import employees from CSV string"""
        result = ImportResult()

        import_employees = self._csv_parser.parse(csv)  # 2

        for employee_data in import_employees:
            maybe_an_employee = self._employees.find_by_email(employee_data.email)  # 3

            if maybe_an_employee is None:  # 4
                self._create_new_employee(employee_data, result)
            else:  # 4
                self._update_employee(employee_data, maybe_an_employee, result)

        return result

    def _create_new_employee(
        self, imported_employee: EmployeeParsedData, result: ImportResult
    ) -> None:  # 5
        """Create and save new employee"""
        new_employee = Employee(
            imported_employee.name,
            imported_employee.email,
            str(imported_employee.starting_date),  # Convert date to string
            imported_employee.role,
        )

        self._employees.save(new_employee)
        result.added_new_employee(new_employee)

    def _update_employee(
        self,
        imported_employee: EmployeeParsedData,
        current_employee: Employee,
        result: ImportResult,
    ) -> None:  # 6
        """Update existing employee with imported data"""
        current_employee.name = imported_employee.name
        current_employee.starting_date = str(imported_employee.starting_date)
        current_employee.role = imported_employee.role

        self._employees.update(current_employee)
        result.updated_employee(current_employee)
