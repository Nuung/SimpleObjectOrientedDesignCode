from datetime import date
from typing import Optional

class Employee:
    def __init__(self, name: Optional[str] = None, email: Optional[str] = None, starting_date: Optional[date] = None, role: Optional[str] = None):
        self._name = name
        self._email = email
        self._starting_date = starting_date
        self._role = role

    @property
    def name(self) -> Optional[str]:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def email(self) -> Optional[str]:
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        self._email = email

    @property
    def starting_date(self) -> Optional[date]:
        return self._starting_date

    @starting_date.setter
    def starting_date(self, starting_date: date) -> None:
        self._starting_date = starting_date

    @property
    def role(self) -> Optional[str]:
        return self._role

    @role.setter
    def role(self, role: str) -> None:
        self._role = role
