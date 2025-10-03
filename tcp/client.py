import socket

HOST, PORT = '127.0.0.1', 8080

with socket.socket() as s:
    s.connect((HOST, PORT))
    print(f"Connected to {HOST}:{PORT}")
    message = "Hello, this is the TCP client!"
    payload = message.encode()
    s.sendall(payload)
    data = s.recv(1024) # number of bytes to receive
    print(f"Received: {data.decode()}")