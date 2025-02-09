from solana_utils import get_recent_transactions
from config import HIGH_PERFORMING_WALLET

def test_get_recent_transactions():
    # Fetch the most recent transactions
    transactions = get_recent_transactions(HIGH_PERFORMING_WALLET)
    
    # Print each transaction with its details
    if transactions:
        print(f"Found {len(transactions)} transactions:")
        for tx in transactions:
            print(f"Signature: {tx['signature']} | Confirmed at: {tx['blockTime']}")
    else:
        print("No transactions found.")

if __name__ == "__main__":
    test_get_recent_transactions()
