import asyncio
import websockets

HOST = '127.0.0.1'
PORT = 8080

async def handler(websocket):
    async for message in websocket:
        print(f"Received from client: {message}")
        await websocket.send(f"Received: {message}")

async def main():
    async with websockets.serve(handler, HOST, PORT):
        print(f"WebSocket server listening on ws://{HOST}:{PORT}")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())