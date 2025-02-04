import requests
import logging
from config import SOLANA_RPC_URL

# Set up logger for Solana-related actions
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

def get_recent_transactions(wallet_address, limit=10):
    try:
        url = SOLANA_RPC_URL
        params = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getConfirmedSignaturesForAddress2",
            "params": [wallet_address, {"limit": limit}],
        }
        response = requests.post(url, json=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching transactions for {wallet_address}: {e}")
        return None

def get_balance(wallet_address):
    try:
        url = SOLANA_RPC_URL
        params = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getBalance",
            "params": [wallet_address],
        }
        response = requests.post(url, json=params)
        response.raise_for_status()
        return response.json()["result"]["value"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching balance for {wallet_address}: {e}")
        return 0
