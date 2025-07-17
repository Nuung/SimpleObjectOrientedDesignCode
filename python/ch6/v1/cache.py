"""
Cache class - Python conversion from Java
Implements a simple in-memory cache
"""

from typing import Dict, List, Set, Any


class Cache:
    """A simple in-memory cache for entities"""

    def __init__(self):
        self._store: Dict[Any, List[Any]] = {}

    def contains(self, key: Any) -> bool:
        """Check if the cache contains the given key"""
        return key in self._store

    def add(self, key: Any, entity: Any) -> None:
        """Add a single entity to the cache under the given key"""
        if key not in self._store:
            self._store[key] = []
        self._store[key].append(entity)

    def add_all(self, key: Any, entities: Set[Any]) -> None:
        """Add a set of entities to the cache under the given key"""
        if key not in self._store:
            self._store[key] = list(entities)
        else:
            self._store[key].extend(list(entities))

    def get(self, key: Any) -> Set[Any]:
        """Retrieve entities for the given key as a set"""
        if key not in self._store:
            return set()
        else:
            return set(self._store[key])
