"""
Hibernate Offering Repository - Python conversion from Java
Simulates a Hibernate-like repository for Offering operations.
"""

from typing import Optional, Any, List
from python.ch6.v1.cache import Cache
from python.ch6.v2.offering import Offering
from python.ch6.v2.enrollment import Enrollment
from python.ch6.v2.offering_repository import OfferingRepository


# Mock Session class to simulate Hibernate behavior
class MockSession:
    def find(self, entity_class: Any, id_: Any) -> Optional[Any]:
        # Simulate finding an entity by ID
        print(f"MockSession: Finding {entity_class.__name__} with ID {id_}")
        # In a real scenario, this would query a database
        return None

    def create_query(self, query_string: str, entity_class: Any) -> Any:
        # Simulate creating a query
        print(f"MockSession: Creating query: {query_string} for {entity_class.__name__}")
        return MockQuery()

    def persist(self, entity: Any) -> None:
        # Simulate persisting an entity
        print(f"MockSession: Persisting {entity.__class__.__name__}")

    def merge(self, entity: Any) -> None:
        # Simulate merging an entity
        print(f"MockSession: Merging {entity.__class__.__name__}")

    def get(self, entity_class: Any, id_: Any) -> Optional[Any]:
        # Simulate getting an entity by ID
        print(f"MockSession: Getting {entity_class.__name__} with ID {id_}")
        return None


class MockQuery:
    def __init__(self):
        self._parameters = {}

    def set_parameter(self, name: str, value: Any) -> "MockQuery":
        self._parameters[name] = value
        return self

    def get_result_list(self) -> List[Any]:
        # Simulate getting a list of results
        print(f"MockQuery: Getting result list with parameters: {self._parameters}")
        return []

    def get_single_result(self) -> Any:
        # Simulate getting a single result
        print(f"MockQuery: Getting single result with parameters: {self._parameters}")
        return None


class HibernateOfferingRepository(OfferingRepository):
    """Offering repository implementation simulating Hibernate interaction"""

    def __init__(self, session: MockSession):
        self._cache: Cache[int, Offering] = Cache()
        self._session = session

    def save(self, offering: Offering) -> None:
        """Save a new offering"""
        self._session.persist(offering)

    def update(self, offering: Offering) -> None:
        """Update an existing offering"""
        self._session.merge(offering)

    def find_by_id(self, id_: int) -> Optional[Offering]:
        """Find an offering by its ID"""
        return self._session.find(Offering, id_)

    def get_by_id(self, id_: int) -> Offering:
        """Get an offering by its ID"""
        return self._session.get(Offering, id_)

    def get_offering_from(self, enrollment_id: int) -> Offering:
        """Get an offering from an enrollment ID"""
        return self._session.create_query(
            "from Offering o inner join o.enrollments e where e.id = :enrollmentId", Offering
        ).set_parameter("enrollmentId", enrollment_id).get_single_result()

    def get_enrollment(self, offering_id: int, employee_id: int) -> Enrollment:
        """Get an enrollment by offering ID and employee ID"""
        return self._session.create_query(
            "select e from Enrollment e where e.offering.id = :offeringId and e.employee.id = :employeeId", Enrollment
        ).set_parameter("offeringId", offering_id).set_parameter("employeeId", employee_id).get_single_result()

    def available_spots(self, offering: Offering) -> int:
        """Get the number of available spots for an offering"""
        if not self._cache.contains(offering.id):
            # Simulate database query
            spots = self._session.create_query(
                "select maximumNumberOfAttendees - count(...) from Offering o where ...", int
            ).set_parameter("offeringId", offering.id).get_single_result()
            self._cache.add(offering.id, spots)
        return self._cache.get(offering.id).pop() # Assuming get returns a set, pop to get the single element
