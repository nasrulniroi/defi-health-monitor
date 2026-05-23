"""Alert data model."""
from dataclasses import dataclass
from typing import Optional

@dataclass
class Alert:
    protocol: str
    severity: str
    message: str
    score: float
    factor: str
    timestamp: Optional[str] = None
