# Configuration for the Photon Stock Ticker

STOCKS = ["AAPL", "GOOGL", "MSFT", "TSLA"]

# Initial prices for simulation
INITIAL_PRICES = {stock: 100.0 for stock in STOCKS}

# Update interval in seconds
UPDATE_INTERVAL = 1