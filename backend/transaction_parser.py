def parse_transaction(transaction):
    # Initialize defaults
    amount = 0
    token = "SOL"  # Default token in case no token is involved in the transaction

    # Check for token transfers in the transaction
    token_transfers = transaction.get('meta', {}).get('postTokenBalances', [])

    if token_transfers:
        for transfer in token_transfers:
            # Extract the token amount (using 'uiAmount')
            if 'uiAmount' in transfer:
                amount = transfer['uiAmount']
            
            # Token mint address identifies the token involved (e.g., memecoin token)
            if 'mint' in transfer:
                token = transfer['mint']  # Mint address is a unique identifier for the token
    return amount, token
