from dataclasses import dataclass
from jatayu.orm.models import BaseModel
from jatayu.orm.fields import BigIntField, CharField


@dataclass
class User(BaseModel):
    cf: CharField.py_type = CharField(default="DASJFH")
    bif: BigIntField.py_type = BigIntField()
    dfcf: CharField.py_type = CharField(default_factory=lambda: 'WOOT!!!')
