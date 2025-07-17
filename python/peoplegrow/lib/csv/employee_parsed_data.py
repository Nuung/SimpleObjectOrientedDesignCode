from datetime import date
from typing import Optional

class EmployeeParsedData:
    def __init__(self):
        self.name: Optional[str] = None
        self.email: Optional[str] = None
        self.startingDate: Optional[date] = None
        self.role: Optional[str] = None

    @property
    def name(self) -> Optional[str]:
        return self.name

    @property
    def email(self) -> Optional[str]:
        return self.email

    @property
    def startingDate(self) -> Optional[date]:
        return self.startingDate

    @property
    def role(self) -> Optional[str]:
        return self.role
