"""
Employee class - Python conversion from Java
Maintains exact OOP structure and design patterns
"""

from typing import Set
from python.ch5.v1.badge import Badge
from python.ch5.v1.trainings_taken import TrainingsTaken
from python.ch5.v1.badge_already_exists_exception import BadgeAlreadyExistsException


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
        self._wants_email_updates = False
        self._trainings_taken: TrainingsTaken = None  # Placeholder
        self._badges: Set[Badge] = set()

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

    def wants_any_email_updates(self) -> bool:
        return self._wants_email_updates

    def set_wants_email_updates(self, wants_email_updates: bool) -> None:
        self._wants_email_updates = wants_email_updates

    @property
    def trainings_taken(self) -> TrainingsTaken:
        return self._trainings_taken

    def win_badge(self, badge: Badge) -> None:
        if badge in self._badges:
            raise BadgeAlreadyExistsException()
        self._badges.add(badge)
