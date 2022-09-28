import asyncio
async def handle(reader, writer):
    addr = writer.get_extra_info('peernane')
    message = f"{addr!r} is connected !!!!"
    print(message)
    while True:
        data = await reader.read(100)
        message = data.decode().strip()
        writer.write(data)
        await writer.drain()
        if message == "exit":
            message = f"{addr!r} wants to close the connection."
            print(message)
            break
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle, '127.0.0.1', 8889)
    addr = server.sockets [0].getsockname()
    print(f'Serving on {addr}')
    async with server:
        await server.serve_forever()

asyncio.run(main())
