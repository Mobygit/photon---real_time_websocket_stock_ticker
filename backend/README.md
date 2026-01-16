# Photon Backend

## Overview

This is the backend component of the Photon Real-Time WebSocket Stock Ticker project. It provides a FastAPI-based server that streams mock stock price updates via WebSockets to connected clients.

## Architecture

The backend is structured as follows:

- **`main.py`**: The main FastAPI application with the WebSocket endpoint (`/ws`). It handles client connections and starts the price generation task on startup.
- **`websocket_manager.py`**: A connection manager class that handles WebSocket connections, disconnections, and broadcasting messages to all active clients.
- **`stock_generator.py`**: An asynchronous stock price generator that simulates price changes for predefined stocks and broadcasts updates every second.
- **`config.py`**: Configuration file containing stock symbols, initial prices, and update intervals.

## How WebSockets Work

WebSockets enable real-time, bidirectional communication between the client and server over a single TCP connection. Unlike HTTP, which is request-response based, WebSockets allow the server to push data to clients instantly without the client needing to poll for updates.

In this application:
- Clients establish a WebSocket connection to `/ws`.
- The server maintains a list of active connections.
- A background task generates price updates and broadcasts them to all connected clients as JSON data.
- Clients receive updates in real-time and update the UI accordingly.

## Running the Backend

1. Navigate to the `backend` directory.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the server:
   ```
   uvicorn app.main:app --reload
   ```
4. The server will be available at `http://127.0.0.1:8000`.
5. WebSocket endpoint: `ws://127.0.0.1:8000/ws`.

## API

- **WebSocket `/ws`**: Connect to receive real-time stock price updates. Messages are JSON arrays of stock data, e.g.:
  ```json
  [
    {"stock": "AAPL", "price": 150.25, "change": 2.5},
    {"stock": "GOOGL", "price": 2800.0, "change": -1.2}
  ]
  ```