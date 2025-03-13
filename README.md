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

When you run this program currently, the terminal output will look something like this. Here is an explanation of what you'll be seeing in the terminal and what it means. This should help with continuing to debug and develop. 

Let's break down the output you're seeing step-by-step and highlight the key points that you should make note of:

### 1. **Initial Debug Information**
   ```
   DEBUG:asyncio:Using proactor: IocpProactor
   DEBUG:websockets.client:= connection is CONNECTING
   ```
   - **`Using proactor: IocpProactor`**: This is the `asyncio` event loop you're using in Windows to handle asynchronous I/O. It's just part of the asyncio setup and isn't a problem, but it's useful for diagnosing issues related to concurrency.
   - **`connection is CONNECTING`**: The WebSocket client is trying to establish the connection at this point.

---

### 2. **WebSocket Handshake (HTTP → WebSocket Upgrade)**
   ```
   DEBUG:websockets.client:> GET / HTTP/1.1
   DEBUG:websockets.client:> Host: api.mainnet-beta.solana.com
   DEBUG:websockets.client:> Upgrade: websocket
   DEBUG:websockets.client:> Connection: Upgrade
   DEBUG:websockets.client:> Sec-WebSocket-Key: M+zuT9iqO9Or66Vp8enH4g==
   DEBUG:websockets.client:> Sec-WebSocket-Version: 13
   DEBUG:websockets.client:> Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits
   ```
   - These are part of the WebSocket **handshake** that happens when a connection is established.
   - The client is sending an HTTP `GET` request to the WebSocket server (`api.mainnet-beta.solana.com`) to initiate the WebSocket connection. It's upgrading the connection to a WebSocket (`Upgrade: websocket`).

---

### 3. **WebSocket Connection Upgrade Success**
   ```
   DEBUG:websockets.client:< HTTP/1.1 101 Switching Protocols
   DEBUG:websockets.client:< upgrade: websocket
   DEBUG:websockets.client:< connection: Upgrade
   DEBUG:websockets.client:< sec-websocket-accept: OK6m5SLDmrDrhxP+5f8acNa7DTo=
   DEBUG:websockets.client:< x-rpc-node: dal17
   DEBUG:websockets.client:< x-ratelimit-tier: free
   DEBUG:websockets.client:< x-ratelimit-method-limit: 40
   DEBUG:websockets.client:< x-ratelimit-method-remaining: 39
   DEBUG:websockets.client:< x-ratelimit-rps-limit: 100
   DEBUG:websockets.client:< x-ratelimit-rps-remaining: 99
   DEBUG:websockets.client:< x-ratelimit-endpoint-limit: unlimited
   DEBUG:websockets.client:< x-ratelimit-endpoint-remaining: -2204
   DEBUG:websockets.client:< x-ratelimit-conn-limit: 40
   DEBUG:websockets.client:< x-ratelimit-conn-remaining: 39
   DEBUG:websockets.client:< x-ratelimit-connrate-limit: 40
   DEBUG:websockets.client:< x-ratelimit-connrate-remaining: 39
   DEBUG:websockets.client:< x-ratelimit-pubsub-limit: 5
   DEBUG:websockets.client:< x-ratelimit-pubsub-remaining: 5
   DEBUG:websockets.client:< access-control-allow-origin: backend_traffic
   ```
   - **Connection Upgrade**: The server responds with a `101 Switching Protocols`, which means the WebSocket connection has been successfully established.
   - **Rate Limit Information**: These `x-ratelimit-*` headers are important to monitor since they inform you about the limits the server places on requests. For example:
     - **`x-ratelimit-method-limit: 40`** indicates you can make up to 40 requests per method in a given time frame.
     - **`x-ratelimit-rps-limit: 100`** indicates 100 requests per second are allowed.
   - **`x-ratelimit-pubsub-limit: 5`**: This is crucial because it means you can only subscribe to 5 different topics at the same time.

---

### 4. **WebSocket Connection Established**
   ```
   DEBUG:websockets.client:= connection is OPEN
   INFO:root:WebSocket connection established
   ```
   - **Connection is Open**: This confirms the WebSocket connection is successfully established, and you're now ready to send and receive data over it.
   - **`INFO:root:WebSocket connection established`**: This is a custom log in your code, confirming the WebSocket connection was successfully opened.

---

### 5. **Subscription Request Sent**
   ```
   DEBUG:websockets.client:> TEXT '{"jsonrpc": "2.0", "id": 1, "method": "logsSubscribe", "params": [{"mentions": ["DfMxre4cKmvogbLrPigxmibVTTQDuzjdXojWzjCXXhzj"]}]}' [130 bytes]
   INFO:root:Sent subscription request: {"jsonrpc": "2.0", "id": 1, "method": "logsSubscribe", "params": [{"mentions": ["DfMxre4cKmvogbLrPigxmibVTTQDuzjdXojWzjCXXhzj"]}]}
   ```
   - The subscription request is being sent successfully. This is the request asking the WebSocket server to start sending logs related to transactions involving your **`HIGH_PERFORMING_WALLET`**.
   - The request is logged in the console under `INFO`, showing the payload being sent.

---

### 6. **WebSocket Keepalive Pings**
   ```
   DEBUG:websockets.client:> PING 86 db fe a3 [binary, 4 bytes]
   DEBUG:root:Sent ping to keep connection alive
   DEBUG:websockets.client:< PONG 86 db fe a3 [binary, 4 bytes]
   DEBUG:websockets.client:% sending keepalive ping
   DEBUG:websockets.client:> PING '[x\x1f\x02' [text, 4 bytes]
   DEBUG:websockets.client:< PONG '[x\x1f\x02' [text, 4 bytes]
   DEBUG:websockets.client:% received keepalive pong
   DEBUG:websockets.client:> PING 82 f6 65 6c [binary, 4 bytes]
   DEBUG:root:Sent ping to keep connection alive
   DEBUG:websockets.client:< PONG 82 f6 65 6c [binary, 4 bytes]
   ```
   - **Ping/Pong**: This is the WebSocket keepalive mechanism. Your client is sending "PING" messages every 30 seconds to keep the connection alive, and the server responds with "PONG".
   - **Keep Connection Alive**: This is important to ensure the WebSocket connection remains open and doesn't time out due to inactivity.

---

### 7. **First Subscription Response**
   ```
   DEBUG:websockets.client:< TEXT '{"jsonrpc":"2.0","result":106463270,"id":1}' [43 bytes]
   ```
   - **Response to Subscription**: This is the WebSocket server’s response confirming the subscription. The `"result": 106463270` indicates a successful subscription, and it may correspond to the subscription ID assigned by the server.

---

### Summary of Key Points:

1. **Connection Established**: Your WebSocket connection has been established successfully, as indicated by `INFO:root:WebSocket connection established`.
2. **Subscription Request Sent**: The system has sent a subscription request asking for logs related to transactions involving your high-performing wallet (`DfMxre4cKmvogbLrPigxmibVTTQDuzjdXojWzjCXXhzj`).
3. **Keepalive Ping**: The connection is being kept alive using ping/pong messages, as expected.
4. **Subscription Confirmation**: The server has responded with a success message, confirming that the subscription has been successfully established.

### Things to Monitor:
- **Rate Limiting**: Monitor the `x-ratelimit-*` headers to ensure you don’t exceed the rate limits of the WebSocket server, especially if you plan to scale up your subscription requests.
- **Handling Incoming Logs**: The logs you are receiving now will need to be parsed and processed according to your application’s logic. You’re subscribing to specific logs, but the actual processing logic (such as detecting a buy/sell action) needs to be triggered when the logs arrive.

If you have any specific concerns or questions about what you're seeing, feel free to let me know!


