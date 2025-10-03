import websocket 

HOST = '127.0.0.1'
PORT = 8080

uri = f"ws://{HOST}:{PORT}"
ws = websocket.create_connection(uri)

ws.send("Hello from the WebSocket client.")

reply = ws.recv()
print(reply)

ws.close()