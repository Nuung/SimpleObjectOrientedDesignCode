from enum import Enum
from typing import List, Any, Type
from datetime import date, datetime

class Mode(Enum):
    IGNORE_ERRORS = "IGNORE_ERRORS"

class EmployeeParsedData:
    def __init__(self):
        self.name: str = None
        self.email: str = None
        self.startingDate: date = None
        self.role: str = None

class CsvParserLibrary:
    def __init__(self):
        self.mode: Mode = Mode.IGNORE_ERRORS
        self.object_type: Type = object

    def set_mode(self, mode: Mode):
        self.mode = mode

    def set_object_type(self, object_type: Type):
        self.object_type = object_type

    def parse(self, csv: str) -> List[Any]:
        result: List[Any] = []
        lines = csv.split("\n")

        if len(lines) < 2:
            return result

        headers = [header.strip() for header in lines[0].split(",")]
        for i in range(1, len(lines)):
            values = [value.strip() for value in lines[i].split(",")]
            try:
                instance = self.object_type()
                for j, header in enumerate(headers):
                    if j < len(values): # Ensure value exists for header
                        field_name = header
                        field_type = self._get_field_type(self.object_type, field_name)
                        setattr(instance, field_name, self._convert_value(field_type, values[j]))
                result.append(instance)
            except Exception as e:
                if self.mode != Mode.IGNORE_ERRors:
                    raise RuntimeError("CSV 파싱 중 오류 발생") from e
        return result

    def _get_field_type(self, obj_type: Type, field_name: str) -> Type:
        # This is a simplified version. In a real scenario, you might inspect
        # the __annotations__ of the class or have a mapping.
        # For EmployeeParsedData, we know the types.
        if obj_type == EmployeeParsedData:
            if field_name == "name":
                return str
            elif field_name == "email":
                return str
            elif field_name == "startingDate":
                return date
            elif field_name == "role":
                return str
        return str # Default to string if type is unknown or not EmployeeParsedData

    def _convert_value(self, type_class: Type, value: str) -> Any:
        if type_class == str:
            return value
        elif type_class == int:
            return int(value)
        elif type_class == float:
            return float(value)
        elif type_class == bool:
            return value.lower() == "true"
        elif type_class == date:
            return date.fromisoformat(value)
        elif type_class == datetime:
            return datetime.fromisoformat(value)
        raise UnsupportedOperationError(f"Unsupported type: {type_class}")

class UnsupportedOperationError(Exception):
    pass
