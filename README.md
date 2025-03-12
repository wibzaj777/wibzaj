# wibzaj
Wallet Imitating Bot 

Given the changes and the updates you’ve made in the `websocket_client.py` file, I can refine and update the summary to better reflect how the program is currently working. Here’s an updated version of the high-level summary based on your code and current execution:

---

### **Updated High-Level Summary of Components and Their Roles:**

---

### 1. **`solana_utils.py`**
   - **`get_transaction_details(signature)`**: Fetches detailed information about a specific transaction using its signature. It includes checks for rate-limiting and retries in case of errors (making the system more resilient to connectivity issues).
   - **`get_recent_transactions(wallet_address, limit=10)`**: Retrieves recent transaction signatures for a specific wallet address, then fetches detailed transaction data for each one. This is useful for monitoring the most recent actions on the wallet.
   - **`get_balance(wallet_address)`**: Retrieves the balance of a wallet address. This is used to calculate the proportional trade amount when a relevant transaction occurs.

---

### 2. **`transaction_parser.py`**
   - **`parse_transaction(transaction)`**: Parses a transaction to check if it involves token transfers (such as SOL or custom tokens). It extracts the amount and token involved in the transaction, helping identify trade-related actions (e.g., "Buy" or "Sell").

---

### 3. **`trade_executor.py`**
   - **`execute_trade(amount, token)`**: Placeholder function for executing trades. It logs the trade action (amount and token), but you still need to add logic to interact with Solana’s API or a trading platform to actually execute the trade (e.g., using `solana-py` or another relevant method).

---

### 4. **`websocket_client.py`**
   - **`listen_for_transactions()`**: This is the central asynchronous WebSocket listener that:
     - Connects to a Solana RPC WebSocket endpoint (`SOLANA_RPC_URL`).
     - Subscribes to logs related to the high-performing wallet (`HIGH_PERFORMING_WALLET`) to monitor transactions involving it.
     - As it receives messages, it processes and parses logs for specific actions (such as "Buy" or "Sell").
     - It retrieves transaction details using `get_transaction_details()` and processes them through `parse_transaction()`.
     - If the transaction involves SOL, it calculates a proportional trade amount based on the balance of `HIGH_PERFORMING_WALLET` and `MY_WALLET`.
     - The system is designed to log the calculated trade amount and is ready for further trade execution logic (though trade execution is not implemented yet).
     - **Graceful WebSocket Handling**: It includes retry logic for handling WebSocket connection failures (retries after connection losses) and keeps the connection alive using periodic ping messages.
   
   **New Updates**:
   - The WebSocket connection is now more resilient, with retry logic and keepalive pings.
   - It also ensures that subscription requests to the Solana RPC WebSocket endpoint are sent properly and logs the success response to verify it is properly subscribed to the transaction logs.
   - When a trade is detected, it calculates the proportional trade amount and prepares for execution.

---

### 5. **`bot.py`**
   - This is the main entry point of the program.
   - Calls the `listen_for_transactions()` function from `websocket_client.py` to start monitoring and processing transactions asynchronously.
   - The event loop is run here, allowing the WebSocket listener to continuously listen for and process relevant transactions in real-time.

---

### 6. **`logger.py`**
   - Provides a logging utility that formats logs with timestamps and log levels (INFO, ERROR, etc.), which helps in debugging and monitoring the system’s operation.
   - Logs include information on WebSocket connection statuses, subscription successes, ping responses, and transaction processing.

---

### 7. **`config.py`**
   - Loads configuration variables (e.g., wallet addresses, RPC URLs) from environment variables using `dotenv`, ensuring security and flexibility.
   - Stores critical wallet addresses (`HIGH_PERFORMING_WALLET`, `MY_WALLET`) and the Solana RPC URL for the WebSocket connection.

---

### **Updated Overall Flow:**

1. **WebSocket Monitoring**: 
   - The system uses a WebSocket connection (`listen_for_transactions()`) to monitor transactions on the Solana blockchain that involve a specific wallet (`HIGH_PERFORMING_WALLET`). 
   - It subscribes to logs related to this wallet, using the `logsSubscribe` method to stay updated with any transactions.
   
2. **Transaction Parsing**: 
   - When a relevant transaction (like a "Buy" or "Sell") is detected, the system fetches the transaction details and parses them using the `parse_transaction()` function to extract the token and amount involved.
   
3. **Balance Calculation**:
   - If the transaction involves **SOL**, the program calculates a **proportional trade amount**. This is done by comparing the balances of the `HIGH_PERFORMING_WALLET` and `MY_WALLET`. The idea is that your wallet will trade a proportionate amount of SOL based on the balance comparison.
   - This calculation is logged for debugging and monitoring purposes.

4. **Logging**:
   - Logs of key actions, such as connection status, subscription success, pings, and transaction processing, are generated and stored via the `logger` utility.

5. **Graceful WebSocket Handling**:
   - The program uses retry logic and keepalive pings to ensure the WebSocket connection is stable and persistent. If the connection drops, the system will attempt to reconnect automatically.
   
6. **Trade Execution (Placeholder)**:
   - **Trade Execution Placeholder**: If the trade is detected and the proportional trade amount is calculated, the system is ready for execution. However, the actual trade execution logic (e.g., interacting with Solana’s API or CLI to execute a trade) is still to be added.

---

### **Updated Summary**:
The program is designed to monitor **Solana blockchain transactions** involving a high-performing wallet, parse them for trade actions (like "Buy" or "Sell"), calculate proportional trade amounts based on wallet balances, and log these activities for potential execution.

- The WebSocket connection is set up with **retry logic** to handle any interruptions in the connection.
- The system can **calculate the amount** to trade (based on the balance of two wallets), but **actual trade execution** is yet to be implemented.
- **Logging** ensures transparency and traceability of the process, helping with debugging and tracking.
- **Graceful WebSocket handling** ensures that the system maintains stability during real-time transaction monitoring.

---

This update reflects the current state of the system, including the retry logic, keep-alive pinging, and subscription request handling. It also highlights that while the core structure for transaction monitoring, parsing, and trade calculation is in place, **trade execution** is yet to be implemented.

Let me know if you need further details or modifications to the summary!


