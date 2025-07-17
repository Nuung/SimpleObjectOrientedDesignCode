"""
CSV Parser Library - Python conversion from Java
Maintains exact OOP structure and design patterns
"""

from enum import Enum
from typing import List, Any, Type
from datetime import datetime, date
from dataclasses import dataclass


class Mode(Enum):
    """Mode enum for CSV parsing error handling"""

    IGNORE_ERRORS = "IGNORE_ERRORS"
    THROW_EXCEPTIONS = "THROW_EXCEPTIONS"


@dataclass
class EmployeeParsedData:
    """Record class equivalent for parsed employee data"""

    name: str
    email: str
    starting_date: date
    role: str


class CsvParserLibrary:
    """CSV Parser maintaining Java class structure and behavior"""

    def __init__(self):
        self._mode = Mode.IGNORE_ERRORS
        self._object_type = object

    def set_object_type(self, object_type: Type) -> None:
        """Set the target object type for parsing"""
        self._object_type = object_type

    def set_mode(self, mode: Mode) -> None:
        """Set the error handling mode"""
        self._mode = mode

    def parse(self, csv: str) -> List[Any]:
        """Parse CSV string into list of objects"""
        result = []
        lines = csv.split("\n")

        if len(lines) < 2:
            return result  # 데이터가 없으면 빈 리스트 반환

        headers = [header.strip() for header in lines[0].split(",")]

        for i in range(1, len(lines)):
            values = [value.strip() for value in lines[i].split(",")]
            try:
                instance = self._create_instance(headers, values)
                result.append(instance)
            except Exception as e:
                if self._mode != Mode.IGNORE_ERRORS:
                    raise RuntimeError("CSV 파싱 중 오류 발생") from e

        return result

    def _create_instance(self, headers: List[str], values: List[str]) -> Any:
        """Create instance of target object type with field values"""
        if self._object_type == EmployeeParsedData:
            # Handle EmployeeParsedData specifically
            field_values = {}
            for j, header in enumerate(headers):
                if j < len(values):
                    field_values[header] = self._convert_value(
                        self._get_field_type(header), values[j]
                    )
            return EmployeeParsedData(**field_values)
        else:
            # Generic object creation
            instance = self._object_type()
            for j, header in enumerate(headers):
                if j < len(values):
                    converted_value = self._convert_value(str, values[j])
                    setattr(instance, header, converted_value)
            return instance

    def _get_field_type(self, field_name: str) -> Type:
        """Get the type for a specific field in EmployeeParsedData"""
        if field_name == "starting_date":
            return date
        return str

    def _convert_value(self, type_class: Type, value: str) -> Any:
        """Convert string value to appropriate type"""
        try:
            if type_class == str:
                return value
            elif type_class == int:
                return int(value)
            elif type_class == float:
                return float(value)
            elif type_class == bool:
                return value.lower() in ("true", "1", "yes")
            elif type_class == date:
                return datetime.fromisoformat(value).date()
            elif type_class == datetime:
                return datetime.fromisoformat(value)
            else:
                raise UnsupportedOperationError(f"Unsupported type: {type_class}")
        except ValueError as e:
            raise UnsupportedOperationError(
                f"Cannot convert '{value}' to {type_class}"
            ) from e


class UnsupportedOperationError(Exception):
    """Exception for unsupported type conversions"""

    pass
