from abc import ABC, abstractmethod
from typing import Optional

from peoplegrow.entity.employee import Employee


class EmployeeRepository(ABC):
    @abstractmethod
    def find_by_email(self, email: str) -> Optional[Employee]:
        pass

    @abstractmethod
    def save(self, employee: Employee) -> None:
        pass

    @abstractmethod
    def update(self, employee: Employee) -> None:
        # In JPA, this might be handled automatically by the entity manager.
        # In Python, this could be a no-op or a call to save depending on the ORM.
        pass
