import socket

HOST = '127.0.0.1'
PORT = 8080

TIMEOUT_SEC = 1.0  # Check for interrupt every 1 second

with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen()
    s.settimeout(TIMEOUT_SEC) # To make sure we can interrupt the execution with CTRL+C
    
    print(f"TCP server listening on {HOST}:{PORT}...")
    try:
        while True:
            try:
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by {addr}")
                    data = conn.recv(1024)
                    print(f"Received: {data.decode()}")
                    conn.sendall(b"Server echo: Got your message!")
            except socket.timeout:
                pass  
                
    except KeyboardInterrupt:
        print("Server shutting down.")