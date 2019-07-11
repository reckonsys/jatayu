import asyncio
import asyncpg

from cerberus.orm.postgresql import PostgreSQL


async def run():
    connection = await asyncpg.connect(
        user='cerberus', password='cerberus', database='cerberus',
        host='127.0.0.1')
    pg = PostgreSQL(connection)
    values = await pg.create_extension_uuid_ossp()
    print(values)
    await connection.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
