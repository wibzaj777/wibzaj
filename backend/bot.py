# bot.py
import time
from solana_utils import get_recent_transactions, get_balance
from config import HIGH_PERFORMING_WALLET, MY_WALLET

def main():
    print(f"Monitoring transactions for wallet: {HIGH_PERFORMING_WALLET}")
    
    while True:
        print("Checking for recent transactions...")
        transactions = get_recent_transactions(HIGH_PERFORMING_WALLET)
        
        if transactions:
            print(f"Found {len(transactions)} transaction(s).")
            for tx in transactions:
                print(f"Transaction: {tx['signature']}")
                # You can process the transaction further here
                
        else:
            print("No transactions found.")
        
        time.sleep(5)  # Check every 5 seconds for new transactions

if __name__ == "__main__":
    main()

