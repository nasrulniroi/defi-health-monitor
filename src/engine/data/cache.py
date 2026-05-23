"""Simple in-memory cache with TTL for API responses."""
import time
from typing import Any, Optional, Dict

class Cache:
    def __init__(self, ttl: int = 300):
        self._store: Dict[str, Dict] = {}
        self._ttl = ttl

    def get(self, key: str) -> Optional[Any]:
        if key in self._store:
            entry = self._store[key]
            if time.time() - entry["ts"] < self._ttl:
                return entry["value"]
            del self._store[key]
        return None

    def set(self, key: str, value: Any) -> None:
        self._store[key] = {"value": value, "ts": time.time()}

    def clear(self) -> None:
        self._store.clear()

    def size(self) -> int:
        return len(self._store)
