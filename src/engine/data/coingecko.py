"""CoinGecko API client for token price data."""
import aiohttp
from typing import Dict, List, Optional

BASE_URL = "https://api.coingecko.com/api/v3"

class CoinGeckoClient:
    def __init__(self):
        self.session: Optional[aiohttp.ClientSession] = None

    async def _get_session(self) -> aiohttp.ClientSession:
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()
        return self.session

    async def get_token_price(self, token_id: str, vs_currency: str = "usd") -> Dict:
        session = await self._get_session()
        async with session.get(f"{BASE_URL}/simple/price", params={"ids": token_id, "vs_currencies": vs_currency}) as resp:
            return await resp.json()

    async def get_market_data(self, token_id: str) -> Dict:
        session = await self._get_session()
        async with session.get(f"{BASE_URL}/coins/{token_id}") as resp:
            return await resp.json()

    async def close(self):
        if self.session and not self.session.closed:
            await self.session.close()
