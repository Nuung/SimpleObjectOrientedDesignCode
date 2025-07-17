"""
Offering class v5 - Python conversion from Java
Represents a training offering with methods to check update status and waiting list
"""

import random
from typing import Set

from python.ch2.v1.employee import Employee


class Offering:
    """Represents a training offering with methods to check update status and waiting list"""

    def __init__(self):
        self._employees: Set[Employee] = set()

    @property
    def employees(self) -> Set[Employee]:
        """Get the set of employees associated with this offering"""
        return self._employees

    def is_date_updated(self) -> bool:
        """Check if the offering date has been updated (simulated) """
        # 개설 날짜가 변경되었는지 확인하는 로직
        return random.choice([True, False])

    def is_description_updated(self) -> bool:
        """Check if the offering description has been updated (simulated) """
        # 개설 설명이 변경되었는지 확인하는 로직
        return random.choice([True, False])

    def is_important_info_updated(self) -> bool:  # 1
        """Check if important information about the offering has been updated"""
        return self.is_date_updated() or self.is_description_updated()

    def get_waiting_list(self) -> Set[Employee]:
        """Get the waiting list (simulated) """
        # 대기자 목록을 가져오는 로직
        return set()
