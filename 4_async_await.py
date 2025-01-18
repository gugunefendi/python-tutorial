import asyncio

async def greet():
    await asyncio.sleep(5)
    print( 'Hello, asyncio' )

asyncio.run(greet())