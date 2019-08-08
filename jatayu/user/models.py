from dataclasses import dataclass
from pgorm.models import BaseModel
from pgorm.fields import BigIntField, CharField


@dataclass
class User(BaseModel):
    cf: str = CharField(default="DASJFH")
    bif: int = BigIntField()
    dfcf: str = CharField(default_factory=lambda: 'WOOT!!!')
