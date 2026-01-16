// Photon Stock Ticker Frontend Script

// List of stocks to display
const stocks = ["AAPL", "GOOGL", "MSFT", "TSLA"];

// Object to hold references to DOM elements for each stock
const stockElements = {};

// Initialize stock cards in the DOM
function initStocks() {
    const container = document.getElementById('stocks-container');
    stocks.forEach(stock => {
        const card = document.createElement('div');
        card.className = 'stock-card';
        card.innerHTML = `
            <div class="stock-symbol">${stock}</div>
            <div class="stock-price price-neutral">$100.00</div>
            <div class="change-indicator">+0.00</div>
        `;
        container.appendChild(card);
        stockElements[stock] = card;
    });
}

// Establish WebSocket connection and handle messages
function connectWebSocket() {
    const ws = new WebSocket('ws://localhost:8000/ws');

    ws.onopen = () => {
        console.log('Connected to WebSocket server');
    };

    ws.onmessage = (event) => {
        console.log('Received message:', event.data);
        try {
            const updates = JSON.parse(event.data);
            console.log('Parsed updates:', updates);
            updates.forEach(update => {
                const { stock, price, change } = update;
                const card = stockElements[stock];
                if (card) {
                    const priceEl = card.querySelector('.stock-price');
                    const changeEl = card.querySelector('.change-indicator');

                    // Update price display
                    priceEl.textContent = `$${price.toFixed(2)}`;

                    // Update change indicator
                    changeEl.textContent = `${change >= 0 ? '+' : ''}${change.toFixed(2)}`;

                    // Apply color based on change
                    priceEl.className = 'stock-price ' +
                        (change > 0 ? 'price-increase' : change < 0 ? 'price-decrease' : 'price-neutral');
                }
            });
        } catch (error) {
            console.error('Error parsing WebSocket message:', error);
        }
    };

    ws.onclose = () => {
        console.log('WebSocket connection closed. Attempting to reconnect...');
        // Attempt to reconnect after 1 second
        setTimeout(connectWebSocket, 1000);
    };

    ws.onerror = (error) => {
        console.error('WebSocket error:', error);
    };
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    initStocks();
    connectWebSocket();
});