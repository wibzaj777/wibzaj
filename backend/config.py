import os

# Environment variables for sensitive information
HIGH_PERFORMING_WALLET = os.getenv("HIGH_PERFORMING_WALLET")
MY_WALLET = os.getenv("MY_WALLET")
SOLANA_RPC_URL = os.getenv("SOLANA_RPC_URL", "https://api.mainnet-beta.solana.com")

# Optional: Validate required variables
if not HIGH_PERFORMING_WALLET or not MY_WALLET:
    raise ValueError("Both HIGH_PERFORMING_WALLET and MY_WALLET must be set!")
