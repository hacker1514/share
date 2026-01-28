import asyncio, websockets

clients = set()

async def h(ws):
    clients.add(ws)
    try:
        async for m in ws:
            for c in clients:
                if c != ws:
                    await c.send(m)
    finally:
        clients.remove(ws)

async def main():
    async with websockets.serve(h, "0.0.0.0", 8765):
        print(' ----------------------------')
        print("| Server switched on !       |")
        print(' - - - - - - - - - - - - - - ')
        print("| Hello From Hacker !        |")
        print("|        Bye from Niranjan ! |")
        print(' ----------------------------')
        await asyncio.Future()

asyncio.run(main())