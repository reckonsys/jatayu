from dataclasses import dataclass
from pgorm.resources.table import Table
from pgorm.fields import BigIntField, CharField


@dataclass
class User(Table):
    cf: str = CharField(default="DASJFH")
    bif: int = BigIntField()
    dfcf: str = CharField(default_factory=lambda: 'WOOT!!!')
