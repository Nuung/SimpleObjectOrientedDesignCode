"""
Hibernate Employee Repository - Python conversion from Java
Simulates a Hibernate-like repository for Employee operations.
"""

from typing import Optional, Set, Any, List
from python.ch6.v1.cache import Cache
from python.ch6.v1.employee import Employee
from python.ch5.v1.employee_repository import EmployeeRepository


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

    def get_single_result_or_null(self) -> Optional[Any]:
        # Simulate getting a single result or None
        print(f"MockQuery: Getting single result with parameters: {self._parameters}")
        return None


class HibernateEmployeeRepository(EmployeeRepository):
    """Employee repository implementation simulating Hibernate interaction"""

    def __init__(self, session: MockSession):
        self._cache: Cache[Employee, str] = Cache()
        self._session = session

    def find_by_id(self, id_: int) -> Optional[Employee]:
        """Find an employee by their ID"""
        return self._session.find(Employee, id_)

    def find_by_last_name(self, last_name: str) -> Set[Employee]:  # 2
        """Find employees by their last name, using cache"""
        if not self._cache.contains(last_name):
            # Simulate database query
            result_list = self._session.create_query(
                "from Employee e where e.lastName = :lastName", Employee
            ).set_parameter(":lastName", last_name).get_result_list()
            self._cache.add_all(last_name, set(result_list))
        return self._cache.get(last_name)

    def find_by_email(self, email: str) -> Optional[Employee]:
        """Find an employee by their email address"""
        return self._session.create_query(
            "from Employee e where e.email = :email", Employee
        ).set_parameter(":email", email).get_single_result_or_null()

    def save(self, employee: Employee) -> None:
        """Save a new employee"""
        self._session.persist(employee)

    def update(self, employee: Employee) -> None:
        """Update an existing employee"""
        self._session.merge(employee)
