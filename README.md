# Secure Data Exchange using Encoding and TLS

## Project Overview

This project demonstrates a simple implementation of secure file transfer using encoding techniques and modern web protocols. The goal of the system is to show how data can be safely transmitted between a client and a server by combining **Base64 encoding** with **HTTPS and TLS encryption**.

The project follows a basic client–server architecture. A client application reads a file, encodes its content, and sends it to a server over a secure HTTPS connection. The server receives the encoded data, decodes it, and reconstructs the original file.

## Technologies Used

* Python
* Flask (for server-side application)
* Requests library (for client-side communication)
* Base64 encoding
* TLS/HTTPS protocol
* generating certificates (cert.pem, key.pem)

## How the System Works

1. The client reads a file (example: `example.txt`).
2. The file content is converted into **Base64 encoded format**.
3. The encoded data is sent to the server using an **HTTPS POST request**.
4. The HTTPS connection uses **TLS encryption** to protect data during transmission.
5. The server receives the encoded data.
6. The server decodes the Base64 data back into the original file format.
7. The decoded file is saved as `received_example.txt`.

This process ensures that the file can travel safely across the network without corruption, while TLS protects the communication channel from unauthorized access.

## Project Structure

```
Secure-Data-Exchange/
│
├── README.md
├── client.py
├── example.txt
├── key.pem
├── received_example.txt
└── server.py
```

## Setup Instructions

### 1. Install Required Libraries

Run the following command:

```
pip install flask requests cryptography
```

### 2. Generate TLS Certificates

Use OpenSSL to generate a certificate and key:

```
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

### 3. Start the Server

Run the server:

```
python server.py
```

The server will start at:

```
https://127.0.0.1:5000
```

### 4. Run the Client

In another terminal, run:

```
python client.py
```

The file will be securely transferred and saved as:

```
received_example.txt
```

## Security Features

* Base64 encoding ensures safe formatting of file data.
* HTTPS provides encrypted communication.
* TLS protects the data from interception during transmission.

## Educational Purpose

This project is created for learning purposes to understand how encoding formats and secure protocols work together in modern networks to support secure data exchange.


