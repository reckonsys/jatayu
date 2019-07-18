import asyncio
import asyncpg

from jatayu.orm.postgresql import PostgreSQL
from jatayu.user.models import User


async def run():
    connection = await asyncpg.connect(
        user='jatayu', password='jatayu', database='jatayu',
        host='127.0.0.1')
    pg = PostgreSQL(connection)
    __import__('ipdb').set_trace()
    foo = await pg.create_table(User)
    values = await pg.create_extension_uuid_ossp()
    print(values)
    await connection.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
