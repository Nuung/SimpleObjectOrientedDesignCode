"""
Offering Update Service v3 - Python conversion from Java
Refactored version with improved notification logic
Maintains exact OOP structure and separation of concerns
"""

from python.ch2.v1.employee import Employee
from python.ch2.v3.offering import Offering


class OfferingUpdateService:
    """Service for updating offerings and notifying employees"""

    def update(self, updated_offering: Offering) -> None:
        """Update offering and notify relevant employees"""
        # ...
        # 개설 내용을 변경하는 로직
        # ...

        for employee in updated_offering.employees:
            if employee.wants_email_updates or (
                updated_offering.is_date_updated()
                or updated_offering.is_description_updated()
            ):  # 1
                # 직원들에게 변경된 내용을 알리는 이메일을 보낸다
                pass
