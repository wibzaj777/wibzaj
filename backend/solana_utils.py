import requests
from config import SOLANA_RPC_URL
import time


def get_transaction_details(signature):
    """ Fetch detailed information about a transaction by its signature, with rate limit handling and maxSupportedTransactionVersion """
    url = SOLANA_RPC_URL
    params = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTransaction",
        "params": [signature, {"encoding": "jsonParsed", "maxSupportedTransactionVersion": 0}],
    }

    retries = 5  # Retry a few times if rate-limited
    backoff_time = 10  # Start with a 10-second delay between retries
    for attempt in range(retries):
        try:
            response = requests.post(url, json=params)
            response_data = response.json()
            
            # Check for errors in the response
            if "error" in response_data:
                if response_data["error"]["code"] == 429:
                    # Rate-limited, wait and try again with exponential backoff
                    print(f"Rate-limited, retrying in {backoff_time} seconds...")
                    time.sleep(backoff_time)  # Wait before retrying
                    backoff_time *= 2  # Double the backoff time for the next attempt
                    continue  # Retry the request
                else:
                    raise Exception(f"Error in fetching transaction details: {response_data['error']}")
            
            return response_data.get("result", {})
        except Exception as e:
            print(f"Error: {e}")
            return {}

    print("Failed to fetch transaction details after several attempts")
    return {}

def get_recent_transactions(wallet_address, limit=10):
    url = SOLANA_RPC_URL
    params = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getSignaturesForAddress",
        "params": [wallet_address, {"limit": limit}],
    }
    try:
        response = requests.post(url, json=params)
        response_data = response.json()

        # Check for errors in the response
        if "error" in response_data:
            raise Exception(f"Error in fetching transactions: {response_data['error']}")

        # Get transaction signatures (IDs)
        signatures = response_data.get("result", [])

        # Fetch detailed data for each signature
        transactions = []
        for signature_info in signatures:
            signature = signature_info['signature']
            transaction_details = get_transaction_details(signature)
            if transaction_details:
                transactions.append(transaction_details)

        return transactions
    except Exception as e:
        print(f"Error: {e}")
        return []


def get_balance(wallet_address):
    url = SOLANA_RPC_URL
    params = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBalance",
        "params": [wallet_address],
    }
    try:
        response = requests.post(url, json=params)
        response_data = response.json()
        
        # Check for errors in the response
        if "error" in response_data:
            raise Exception(f"Error in fetching balance: {response_data['error']}")

        return response_data["result"]["value"]
    except Exception as e:
        print(f"Error: {e}")
        return 0
