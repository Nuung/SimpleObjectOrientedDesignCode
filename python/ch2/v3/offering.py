"""
Offering class v3 - Python conversion from Java
Represents a training offering with basic update status
"""

import random
from typing import List

from python.ch2.v1.employee import Employee


class Offering:
    """Represents a training offering with methods to check update status"""

    def __init__(self):
        self._employees: List[Employee] = []

    @property
    def employees(self) -> List[Employee]:
        """Get the list of employees associated with this offering"""
        return self._employees

    def is_date_updated(self) -> bool:
        """Check if the offering date has been updated (simulated) """
        # 개설 날짜가 변경되었는지 확인하는 로직
        return random.choice([True, False])

    def is_description_updated(self) -> bool:
        """Check if the offering description has been updated (simulated) """
        # 개설 설명이 변경되었는지 확인하는 로직
        return random.choice([True, False])
