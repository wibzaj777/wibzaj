# solana_utils.py
import requests
from config import SOLANA_RPC_URL

LAMPORTS_PER_SOL = 1_000_000_000  # 1 SOL = 1,000,000,000 lamports

def get_recent_transactions(wallet_address, limit=10):
    url = SOLANA_RPC_URL
    params = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getConfirmedSignaturesForAddress2",
        "params": [wallet_address, {"limit": limit}],
    }
    response = requests.post(url, json=params)
    return response.json().get("result", [])

def get_balance(wallet_address):
    url = SOLANA_RPC_URL
    params = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBalance",
        "params": [wallet_address],
    }
    response = requests.post(url, json=params)
    lamports = response.json().get("result", {}).get("value", 0)
    return lamports / LAMPORTS_PER_SOL  # Convert lamports to SOL
