# Photon - Real-Time WebSocket Stock Ticker

## Run Instructions

Follow these steps to run the Photon Stock Ticker application.

### Prerequisites

- Python 3.10 or higher
- A web browser

### Backend Setup

1. Navigate to the `backend` directory:
   ```
   cd backend
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:
   ```
   uvicorn app.main:app --reload
   ```

   The backend will start on `http://127.0.0.1:8000`.

### Frontend Setup

1. Open a web browser.

2. Navigate to the `frontend` directory.

3. Open `index.html` in your browser, or serve it using a local server.

   For a simple local server, you can use Python:
   ```
   cd frontend
   python -m http.server 8080
   ```
   Then open `http://localhost:8080` in your browser.

### Viewing the Application

- Ensure the backend is running.
- Open the frontend in your browser.
- You should see real-time stock price updates for AAPL, GOOGL, MSFT, and TSLA.
- Prices update every second with random changes.
- Green indicates price increase, red indicates decrease.

### Troubleshooting

- If the frontend doesn't connect, check that the backend is running on port 8000.
- Ensure no firewall is blocking WebSocket connections.
- Check browser console for any JavaScript errors.