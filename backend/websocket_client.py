import asyncio
import websockets
import json
from config import HIGH_PERFORMING_WALLET, SOLANA_RPC_URL, MY_WALLET
from solana_utils import get_balance, get_transaction_details
from transaction_parser import parse_transaction  # We import the parser here
import time
import logging

# Set up logging to output to console
logging.basicConfig(level=logging.DEBUG)

async def send_ping(websocket):
    """ Send ping every 30 seconds to keep the WebSocket connection alive """
    while True:
        try:
            await websocket.ping()
            logging.debug("Sent ping to keep connection alive")
            await asyncio.sleep(30)  # Send ping every 30 seconds
        except websockets.exceptions.ConnectionClosedError:
            logging.error("Connection closed during ping, stopping pings.")
            break

async def listen_for_transactions():
    websocket_url = SOLANA_RPC_URL
    while True:
        try:
            # Establish WebSocket connection
            async with websockets.connect(websocket_url) as websocket:
                logging.info("WebSocket connection established")

                # Set up subscription request
                subscription_request = {
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "logsSubscribe",
                    "params": [{"mentions": [HIGH_PERFORMING_WALLET]}]
                }

                # Send subscription request
                await websocket.send(json.dumps(subscription_request))
                logging.info(f"Sent subscription request: {json.dumps(subscription_request)}")

                # Start the ping task to keep connection alive
                asyncio.create_task(send_ping(websocket))

                # Listen for incoming messages
                while True:
                    message = await websocket.recv()

                    try:
                        # Parse the message data
                        message_data = json.loads(message)

                        # Print the raw message data for debugging (pretty print)
                        logging.debug("Received raw message data: %s", json.dumps(message_data, indent=4))

                        # Parse the logs from the received message
                        if "params" in message_data:
                            result = message_data["params"].get("result", {})
                            signature = result.get("signature", None)  # Correct extraction of signature

                            if signature:
                                logging.info(f"Processing transaction with signature: {signature}")
                                logs = result.get("value", {}).get("logs", [])

                                # Check if logs contain relevant information
                                if logs:
                                    for log in logs:
                                        if "Buy" in log or "Sell" in log:
                                            logging.info(f"Relevant log found: {log}")
                                            
                                            # Now, fetch transaction details
                                            transaction_details = await get_transaction_details(signature)
                                            
                                            if transaction_details:
                                                amount, token = parse_transaction(transaction_details)
                                                logging.info(f"Trade detected: Amount - {amount} {token}")
                                                
                                                # Example: Calculate proportional trade amount based on wallet balances
                                                if token == "SOL":  # Example for Solana transactions
                                                    high_wallet_balance = await get_balance(HIGH_PERFORMING_WALLET)
                                                    my_wallet_balance = await get_balance(MY_WALLET)

                                                    # Log wallet balances
                                                    logging.info(f"High performing wallet balance: {high_wallet_balance}")
                                                    logging.info(f"My wallet balance: {my_wallet_balance}")

                                                    # Proportional calculation
                                                    if high_wallet_balance > 0 and my_wallet_balance > 0:
                                                        proportion = my_wallet_balance / high_wallet_balance
                                                        trade_amount = amount * proportion
                                                        logging.info(f"Proportional trade amount to execute: {trade_amount} SOL")
                                                    else:
                                                        logging.warning("Cannot calculate proportional trade due to zero balance.")
                                else:
                                    logging.info("No relevant logs found in the message.")
                            else:
                                logging.error("Signature not found in the received log data.")
                    except json.JSONDecodeError:
                        logging.error(f"Failed to parse message: {message}")

                    await asyncio.sleep(1)  # Wait before checking for more messages

        except websockets.ConnectionClosed as e:
            logging.error(f"Connection closed: {e}")
            logging.info("Reconnecting...")
            time.sleep(10)

        except Exception as e:
            logging.error(f"Error: {e}")
            logging.info("Retrying in 10 seconds...")
            time.sleep(10)
