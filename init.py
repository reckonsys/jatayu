# file: app.py
import asyncio
import asyncpg

from pgorm.postgresql import PostgreSQL
from myapp.tables import User


async def run():
    connection = await asyncpg.connect(
        user='reckonsys', password='we ❤️ python',
        database='demo', host='db.reckonsys.com')
    pg = PostgreSQL(connection)
    # Lets create UUID OSSP extention (because UUIDField)
    await pg.create_extension_uuid_ossp()
    await pg.create(User)  # Create Table
    user = await pg.insert(User(name='dhilipsiva', age=30))
    print(user)
    # User(pk=UUID('f46863...'), name='dhilipsiva', age=30)
    await connection.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
