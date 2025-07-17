"""
Employee class - Python conversion from Java
Maintains exact OOP structure and design patterns
"""


class Employee:
    """Employee entity class maintaining Java structure"""

    def __init__(
        self,
        name: str = None,
        email: str = None,
        starting_date: str = None,
        role: str = None,
    ):
        self._name = name
        self._email = email
        self._starting_date = starting_date
        self._role = role

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        self._email = email

    @property
    def starting_date(self) -> str:
        return self._starting_date

    @starting_date.setter
    def starting_date(self, starting_date: str) -> None:
        self._starting_date = starting_date

    @property
    def role(self) -> str:
        return self._role

    @role.setter
    def role(self, role: str) -> None:
        self._role = role
