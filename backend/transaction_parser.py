def parse_transaction(transaction):
    amount = transaction.get("amount", 0)
    token = transaction.get("token", "SOL")  # Example placeholder, adjust as per actual transaction data
    return amount, token
