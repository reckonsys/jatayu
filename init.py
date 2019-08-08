import asyncio
import asyncpg

from pgorm.postgresql import PostgreSQL
from jatayu.user.models import User


async def run():
    connection = await asyncpg.connect(
        user='jatayu', password='jatayu', database='jatayu', host='127.0.0.1')
    pg = PostgreSQL(connection)
    values = await pg.create_extension_uuid_ossp()
    foo = await pg.create_table(User)
    print(values, foo)
    await connection.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
