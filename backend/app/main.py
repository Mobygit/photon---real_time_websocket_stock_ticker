from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from contextlib import asynccontextmanager
from .websocket_manager import ConnectionManager
from .stock_generator import StockGenerator
import asyncio


manager = ConnectionManager()
generator = StockGenerator(manager)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    asyncio.create_task(generator.generate_prices())
    yield
    # Shutdown (if needed)


app = FastAPI(title="Photon Stock Ticker", description="Real-time WebSocket stock price streaming", lifespan=lifespan)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for real-time stock price updates.
    Clients connect here to receive broadcasted price data.
    """
    await manager.connect(websocket)
    try:
        while True:
            # Keep the connection alive; the server broadcasts updates
            data = await websocket.receive_text()
            # Optionally handle incoming messages from client (not implemented)
    except WebSocketDisconnect:
        await manager.disconnect(websocket)