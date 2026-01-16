from typing import List
from fastapi import WebSocket


class ConnectionManager:
    """
    Manages WebSocket connections for broadcasting stock price updates.
    """

    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        """
        Accept a new WebSocket connection and add it to the active connections.
        """
        await websocket.accept()
        self.active_connections.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        """
        Remove a WebSocket connection from the active connections.
        """
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        """
        Broadcast a message to all active WebSocket connections.
        """
        for connection in self.active_connections:
            await connection.send_text(message)