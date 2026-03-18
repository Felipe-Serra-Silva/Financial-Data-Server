# Financial Data Server
## Felipe Serra Silva (Aula 5 de Camadas Físicas da Computação)

## About the Project
A real-time financial data streaming application built on a TCP/IP client-server 
architecture. The server acts as a middleware layer, consuming the Brazilian Central 
Bank (BCB) public API to fetch up-to-date financial indicators (D+0) and 
transmitting them to connected clients via socket communication. Clients can 
dynamically select which assets to monitor, receiving live rates for instruments 
such as SELIC, CDI, USD/BRL and EUR/BRL.

## Architecture
BCB Public API → Server (Middleware) → TCP/IP Socket → Client → End User

## Tech Stack
- **Language:** Python 3.x
- **Communication:** TCP/IP Socket (low-level networking)
- **Data Source:** BCB Open Data API (Sistema Gerenciador de Séries Temporais)
- **Serialization:** JSON
- **Protocol:** Custom client-server handshake with asset validation

## How to Run:
1. Install dependencies: `pip install -r requirements.txt`
2. Start the server: `python server.py`
3. Start the client: `python client.py`
**Order matters!** Always start the server before the client
