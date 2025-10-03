import asyncio
import websockets

async def handler(websocket):
    async for message in websocket:
        print(f"Received from client: {message}")
        await websocket.send(f"Server successfully received: {message}")

async def main():
    async with websockets.serve(handler, "localhost", 8080):
        print("WebSocket server running on ws://localhost:8080")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())