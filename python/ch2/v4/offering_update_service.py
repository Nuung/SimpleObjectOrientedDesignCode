"""
Offering Update Service v4 - Python conversion from Java
Refactored version with improved notification logic
Maintains exact OOP structure and separation of concerns
"""

from python.ch2.v1.employee import Employee
from python.ch2.v4.offering import Offering


class OfferingUpdateService:
    """Service for updating offerings and notifying employees"""

    def update(self, updated_offering: Offering) -> None:
        """Update offering and notify relevant employees"""
        # ...
        # 개설 내용을 변경하는 로직
        # ...

        for employee in updated_offering.employees:
            if self._should_receive_an_email(updated_offering, employee):
                # 변경 내용을 수강자들에게 보낸다
                pass

    def _should_receive_an_email(
        self, updated_offering: Offering, employee: Employee
    ) -> bool:
        """직원들은 이메일을 받도록 등록한 경우나
        중요한 정보가 변경된 경우 이메일을 받아야 한다.
        """
        important_info_was_updated = updated_offering.is_important_info_updated()
        employee_wants_updates = employee.wants_any_email_updates()

        return employee_wants_updates or important_info_was_updated
