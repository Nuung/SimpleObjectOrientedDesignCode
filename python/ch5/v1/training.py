"""
Training class - Python conversion from Java
Represents a training course
"""

from datetime import date


class Training:
    """Represents a training course"""

    def __init__(self, name: str = None, end_date: date = None):
        self._name = name
        self._end_date = end_date

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def end_date(self) -> date:
        return self._end_date
