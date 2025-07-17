"""
Invalid Request Exception - Python conversion from Java
Custom exception for invalid requests
"""


class InvalidRequestException(Exception):
    """Exception raised for invalid requests"""

    def __init__(self, message: str):
        super().__init__(message)
