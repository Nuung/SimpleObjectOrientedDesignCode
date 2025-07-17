"""
Emailer class - Python conversion from Java
Handles sending emails for application notifications
"""

from python.ch2.v1.employee import Employee
from python.ch3.v2.offering import Offering


class Emailer:
    """Service for sending emails to employees"""

    def send_waiting_list_email(self, offering: Offering, employee: Employee) -> None:
        """Send email to employee on the waiting list"""
        # 이메일을 보내는 로직
        pass
