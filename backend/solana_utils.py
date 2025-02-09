import requests
from config import SOLANA_RPC_URL

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

        return response_data.get("result", [])
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
