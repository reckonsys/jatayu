import asyncio
import asyncpg


async def run():
    conn = await asyncpg.connect(user='cerberus', password='cerberus',
                                 database='cerberus', host='127.0.0.1')
    values = await conn.fetch('''SELECT * FROM contacts''')
    __import__('ipdb').set_trace()
    print(values)
    await conn.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
