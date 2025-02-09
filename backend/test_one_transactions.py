from solana_utils import get_recent_transactions, get_balance
from transaction_parser import parse_transaction
from config import HIGH_PERFORMING_WALLET, MY_WALLET

def calculate_scaling_factor(my_balance, target_balance):
    """
    Calculate the scaling factor based on my balance and target balance.
    """
    if target_balance == 0:
        return 0  # Avoid division by zero if the target balance is 0
    return my_balance / target_balance

def test_transaction():
    """
    Fetch one transaction, parse it, and calculate the scaling factor.
    """
    print("Fetching recent transactions...")

    # Fetch recent transactions for the target wallet (try a higher limit)
    transactions = get_recent_transactions(HIGH_PERFORMING_WALLET, limit=10)

    print("Raw Response from Solana RPC:", transactions)  # Print the full response for debugging

    if not transactions:
        print("No transactions found.")
    else:
        # Process the first transaction only
        tx = transactions[0]
        print(f"Transaction found: {tx['signature']}")
        
        # Parse the transaction details (amount and token)
        amount, token = parse_transaction(tx)
        print(f"Parsed amount: {amount}, Token: {token}")
        
        # Fetch the balance of your wallet and the target wallet
        my_balance = get_balance(MY_WALLET)
        target_balance = get_balance(HIGH_PERFORMING_WALLET)
        
        # Calculate the scaling factor based on your balance and target wallet's balance
        scaling_factor = calculate_scaling_factor(my_balance, target_balance)
        
        # Print the scaling factor and wallet balances for debugging
        print(f"My Balance: {my_balance} SOL")
        print(f"Target Wallet Balance: {target_balance} SOL")
        print(f"Scaling Factor: {scaling_factor}")

if __name__ == "__main__":
    test_transaction()
