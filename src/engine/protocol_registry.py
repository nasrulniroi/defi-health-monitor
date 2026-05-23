"""Protocol metadata registry with chain and category information."""
from typing import Dict, List, Optional

CHAIN_IDS = {1: "Ethereum", 42161: "Arbitrum", 137: "Polygon", 56: "BSC", 43114: "Avalanche", 10: "Optimism", 250: "Fantom", 1101: "Polygon zkEVM"}

CATEGORIES = ["Lending", "DEX", "Yield", "Bridge", "Liquid Staking", "CDP", "Derivatives", "Yield Aggregator", "Insurance", "Indexes"]

class ProtocolRegistry:
    def __init__(self):
        self._protocols: Dict[str, Dict] = {}

    def register(self, slug: str, metadata: Dict) -> None:
        self._protocols[slug] = metadata

    def get(self, slug: str) -> Optional[Dict]:
        return self._protocols.get(slug)

    def get_all(self) -> List[Dict]:
        return list(self._protocols.values())

    def get_by_chain(self, chain: str) -> List[Dict]:
        return [p for p in self._protocols.values() if p.get("chain", "").lower() == chain.lower()]

    def get_by_category(self, category: str) -> List[Dict]:
        return [p for p in self._protocols.values() if p.get("category", "").lower() == category.lower()]

    def get_supported_chains(self) -> List[str]:
        chains = set()
        for p in self._protocols.values():
            c = p.get("chain", "")
            if c:
                chains.add(c)
        return sorted(chains)
