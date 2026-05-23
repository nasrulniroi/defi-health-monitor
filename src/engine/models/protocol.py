"""Protocol data model."""
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Protocol:
    name: str
    slug: str
    chain: str = "Multi"
    category: str = "Unknown"
    tvl: float = 0.0
    apy: float = 0.0
    apy_7d: float = 0.0
    apy_30d: float = 0.0
    audits: int = 0
    audit_links: List[str] = field(default_factory=list)
    chains: List[str] = field(default_factory=list)
    url: str = ""
    description: str = ""
    health_score: float = 0.0
    risk_level: str = "unknown"

    @classmethod
    def from_defillama(cls, data: dict) -> "Protocol":
        return cls(
            name=data.get("name", "Unknown"),
            slug=data.get("slug", ""),
            chain=data.get("chain", "Multi"),
            category=data.get("category", "Unknown"),
            tvl=data.get("tvl", 0),
            apy=data.get("apy", 0),
            apy_7d=data.get("apyMean7d", 0),
            apy_30d=data.get("apyMean30d", 0),
            audits=data.get("audits", 0),
            audit_links=data.get("audit_links", []),
            chains=data.get("chains", []),
            url=data.get("url", ""),
            description=data.get("description", ""),
        )
