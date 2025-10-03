import socket

HOST, PORT = '127.0.0.1', 8080

with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}...")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024)
            print(f"Received: {data.decode()}")
            conn.sendall(b"Server echo: Got your message!")

