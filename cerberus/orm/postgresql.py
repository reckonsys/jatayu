from dataclasses import dataclass
from asyncpg.connection import Connection


@dataclass
class PostgreSQL:
    """A PostgreSQL DB wrapper"""
    connection: Connection

    async def create_extension(
            self, extention_name: str, if_not_exists: bool = True):
        condition = 'IF NOT EXISTS' if if_not_exists else ''
        stmt = f'CREATE EXTENSION {condition} "{extention_name}";'
        return await self.connection.fetchrow(stmt)

    async def create_extension_uuid_ossp(self):
        return await self.create_extension('uuid-ossp')
