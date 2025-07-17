from typing import List, Optional
from peoplegrow.entity.employee import Employee
from peoplegrow.lib.csv.csv_parser_library import CsvParserLibrary, Mode
from peoplegrow.lib.csv.employee_parsed_data import EmployeeParsedData
from peoplegrow.repository.employee_repository import EmployeeRepository
from peoplegrow.service.entity.import_result import ImportResult


class EmployeeImportCSVParser:
    def __init__(self):
        pass

    def parse(self, csv: str) -> List[EmployeeParsedData]:  # 1
        csv_parser = CsvParserLibrary()
        csv_parser.set_mode(Mode.IGNORE_ERRORS)
        csv_parser.set_object_type(EmployeeParsedData)
        return csv_parser.parse(csv)


class ImportEmployeesService:
    def __init__(
        self, employees: EmployeeRepository, csv_parser: EmployeeImportCSVParser
    ):  # 1
        self.employees = employees
        self.csv_parser = EmployeeImportCSVParser()  # Note: Creates new instance, ignoring parameter

    def import_from_csv_string(self, csv: str) -> ImportResult:
        result = ImportResult()

        import_employees = self.csv_parser.parse(csv)  # 2

        for employee_data in import_employees:
            maybe_an_employee: Optional[Employee] = self.employees.find_by_email(
                employee_data.email
            )  # 3
            if maybe_an_employee is None:  # 4
                self._create_new_employee(employee_data, result)

            else:  # 4
                self._update_employee(employee_data, maybe_an_employee, result)
        return result

    def _create_new_employee(
        self, imported_employee: EmployeeParsedData, result: ImportResult
    ) -> None:  # 5
        new_employee = Employee(
            imported_employee.name,
            imported_employee.email,
            imported_employee.startingDate,
            imported_employee.role,
        )

        self.employees.save(new_employee)
        result.added_new_employee(new_employee)

    def _update_employee(
        self,
        imported_employee: EmployeeParsedData,
        current_employee: Employee,
        result: ImportResult,
    ) -> None:  # 6
        current_employee.name = imported_employee.name
        current_employee.starting_date = imported_employee.startingDate
        current_employee.role = imported_employee.role

        self.employees.update(current_employee)
        result.updated_employee(current_employee)
