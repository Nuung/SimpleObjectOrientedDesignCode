"""
Notification API Interface - Python conversion from Java
Defines the contract for interacting with a notification service
"""

from abc import ABC, abstractmethod
from typing import List

from python.ch7.v1.notification import Notification
from python.ch7.v1.medium import Medium
from python.ch7.v1.dispatch_time import DispatchTime


class NotificationAPI(ABC):
    """Interface for a notification service"""

    @abstractmethod
    def create_notification(
        self,
        message: str,
        supported_medium: List[Medium],
        times: List[DispatchTime],
    ) -> Notification:
        """Creates a new notification"""
        pass

    @abstractmethod
    def add_participant(self, notification_id: int, participant_email: str) -> None:
        """Adds a participant to an existing notification"""
        pass

    @abstractmethod
    def remove_participant(self, notification_id: int, participant_email: str) -> None:
        """Removes a participant from an existing notification"""
        pass
