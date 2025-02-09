# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

HIGH_PERFORMING_WALLET = os.getenv("HIGH_PERFORMING_WALLET")
MY_WALLET = os.getenv("MY_WALLET")
SOLANA_RPC_URL = os.getenv("SOLANA_RPC_URL", "https://api.mainnet-beta.solana.com")
API_KEY = os.getenv("API_KEY", None)

# Test by printing the loaded values
print(f"HIGH_PERFORMING_WALLET: {HIGH_PERFORMING_WALLET}")
print(f"MY_WALLET: {MY_WALLET}")
print(f"SOLANA_RPC_URL: {SOLANA_RPC_URL}")
print(f"API_KEY: {API_KEY}")
