# bot.py
import time
from solana_utils import get_recent_transactions, get_balance
from transaction_parser import parse_transaction  # Import parse_transaction function
from config import HIGH_PERFORMING_WALLET, MY_WALLET
import asyncio
from websocket_client import listen_for_transactions  # Import the WebSocket listener
from config import HIGH_PERFORMING_WALLET
from solana_utils import get_balance  # If you still need to check your balance or any other info


def main():
    print(f"Monitoring transactions for wallet: {HIGH_PERFORMING_WALLET}")
    
    # Run the WebSocket listener asynchronously
    asyncio.run(listen_for_transactions())

if __name__ == "__main__":
    main()
