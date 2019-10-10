# file: myapp/tables.py
from uuid import UUID, uuid4
from dataclasses import dataclass

from pgorm.resources.table import Table
from pgorm.fields import TextField, SmallIntField, UUIDField


@dataclass
class User(Table):
    pk: UUID = UUIDField(default_factory=uuid4)
    name: str = TextField()
    age: int = SmallIntField()
