"""DeFiLlama API client for protocol and TVL data."""
import aiohttp
from typing import Dict, List, Optional

BASE_URL = "https://api.llama.fi"

class DefiLlamaClient:
    def __init__(self):
        self.session: Optional[aiohttp.ClientSession] = None

    async def _get_session(self) -> aiohttp.ClientSession:
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()
        return self.session

    async def get_all_protocols(self) -> List[Dict]:
        session = await self._get_session()
        async with session.get(f"{BASE_URL}/protocols") as resp:
            data = await resp.json()
            return data if isinstance(data, list) else []

    async def get_protocol(self, slug: str) -> Dict:
        session = await self._get_session()
        async with session.get(f"{BASE_URL}/protocol/{slug}") as resp:
            return await resp.json()

    async def get_tvl_history(self, slug: str) -> List[Dict]:
        session = await self._get_session()
        async with session.get(f"{BASE_URL}/protocol/{slug}") as resp:
            data = await resp.json()
            return data.get("tvl", []) if isinstance(data, dict) else []

    async def get_chains_tvl(self) -> List[Dict]:
        session = await self._get_session()
        async with session.get(f"{BASE_URL}/v2/chains") as resp:
            return await resp.json()

    async def close(self):
        if self.session and not self.session.closed:
            await self.session.close()
