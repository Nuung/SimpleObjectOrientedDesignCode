"""
Enrollment Does Not Exist Exception - Python conversion from Java
Custom exception for when an enrollment does not exist
"""


class EnrollmentDoesntExistException(Exception):
    """Exception raised when an enrollment does not exist"""

    def __init__(self):
        super().__init__()
