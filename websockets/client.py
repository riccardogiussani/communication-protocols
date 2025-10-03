import websocket 

uri = "ws://127.0.0.1:8080"

ws = websocket.create_connection(uri)
ws.send("Hello from the WebSocket client.")

reply = ws.recv()
print("Received: ", reply)

ws.close()