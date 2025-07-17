"""
Offering Does Not Exist Exception - Python conversion from Java
Custom exception for when an offering does not exist
"""


class OfferingDoesntExistException(Exception):
    """Exception raised when an offering does not exist"""

    def __init__(self):
        super().__init__()
