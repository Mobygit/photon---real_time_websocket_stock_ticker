import asyncio
import json
import random
from .config import STOCKS, INITIAL_PRICES, UPDATE_INTERVAL
from .websocket_manager import ConnectionManager


class StockGenerator:
    """
    Generates mock stock prices and broadcasts updates via WebSocket.
    """

    def __init__(self, manager: ConnectionManager):
        self.manager = manager
        self.prices = INITIAL_PRICES.copy()

    async def generate_prices(self):
        """
        Continuously generate price updates for all stocks and broadcast them.
        """
        while True:
            updates = []
            for stock in STOCKS:
                # Simulate price change: random fluctuation between -5 and +5
                change = random.uniform(-5, 5)
                self.prices[stock] += change
                # Ensure price doesn't go negative
                self.prices[stock] = max(0, self.prices[stock])
                updates.append({
                    "stock": stock,
                    "price": round(self.prices[stock], 2),
                    "change": round(change, 2)
                })
            # Broadcast all updates as a JSON array
            await self.manager.broadcast(json.dumps(updates))
            await asyncio.sleep(UPDATE_INTERVAL)