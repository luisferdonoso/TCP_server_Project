# TCP Server and Client for Cybersecurity Portfolio Project

This project contains a simple implementation of a TCP server and client written in Python. It's designed to demonstrate the basic principles of network communication and is intended for educational purposes within the scope of a cybersecurity learning project.

## Project Overview

The TCP (Transmission Control Protocol) server and client scripts enable basic communication over a network. The server listens for incoming TCP connections from clients, and upon establishing a successful connection, it sends a greeting message. The client connects to the server, receives the message, and then closes the connection.

## Features

- TCP Server that listens on a configurable port.
- TCP Client that connects to the server.
- Simple message exchange to demonstrate the TCP handshake and data transfer.

## How to Use

### Server

To start the server, run the `server.py` script. By default, the server will listen on localhost and port 8000. Make sure the port is open and not blocked by any firewall. Then run the `client.py` to receive the message. Enjoy!!

```bash
python3 server.py
python3 client.py
