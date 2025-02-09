# transaction_parser.py
def parse_transaction(transaction):
    """
    Parse the transaction to extract relevant details like token amounts and types.
    This assumes that the transaction contains instructions with token transfers.
    """
    # Extract the transaction's instructions, which may contain the transfer information
    instructions = transaction.get("transaction", {}).get("message", {}).get("instructions", [])

    # Initialize variables
    amount = 0
    token = "SOL"  # Default to SOL, if we don't find any token information

    for instruction in instructions:
        # Check if the instruction involves a token transfer (spl-token)
        if "parsed" in instruction:
            parsed_data = instruction["parsed"]
            if parsed_data.get("type") == "transfer":
                # For token transfer instructions, extract the amount and token
                amount = parsed_data.get("amount", 0)
                token = parsed_data.get("mint", "Unknown Token")  # Get the mint address or token symbol
                break  # We're only interested in the first token transfer we find

    return amount, token
