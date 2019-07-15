from dataclasses import MISSING, Field as _Field

'''Type Conversion.

https://magicstack.github.io/asyncpg/current/usage.html#type-conversion

anyarray                       | list
anyenum                        | str
anyrange                       | asyncpg.Range
record                         | asyncpg.Record, tuple, Mapping
bit, varbit                    | asyncpg.BitString
bool                           | bool
box                            | asyncpg.Box
bytea                          | bytes
char, name, varchar, text, xml | str
cidr                           | ipaddress.IPv4Network, ipaddress.IPv6Network
inet                           | ipaddress.IPv4Network, ipaddress.IPv6Network, ipaddress.IPv4Address, ipaddress.IPv6Address  # noqa
macaddr                        | str
circle                         | asyncpg.Circle
date                           | datetime.date
time                           | offset-naïve datetime.time
time with timezone             | offset-aware datetime.time
timestamp                      | offset-naïve datetime.datetime
timestamp with timezone        | offset-aware datetime.datetime
interval                       | datetime.timedelta
float, double precision        | float [1]
smallint, integer, bigint      | int
numeric                        | Decimal
json, jsonb                    | str
line                           | asyncpg.Line
lseg                           | asyncpg.LineSegment
money                          | str
path                           | asyncpg.Path
point                          | asyncpg.Point
polygon                        | asyncpg.Polygon
uuid                           | uuid.UUID
tid                            | tuple
'''


class Field(_Field):
    """A custom field definition."""

    py_type: type = str
    pg_type: str = 'TEXT'

    def __init__(
            self, default=MISSING, default_factory=MISSING, init=True,
            repr=True, hash=None, compare=True):
        # It is an error to specify both default and default_factory.
        if default is not MISSING and default_factory is not MISSING:
            raise ValueError('cannot specify both default and default_factory')
        if default is MISSING and default_factory is MISSING:
            default = self.py_type()
        super(Field, self).__init__(
            default, default_factory, init, repr, hash, compare, None)


class BigIntField(Field):

    py_type: type = int
    pg_type: str = 'BIGINT'


class CharField(Field):

    py_type: type = str
    pg_type: str = 'CHAR'


'''
bigserial # serial
bit  # [ (n) ]
varbit  # [ (n) ]
boolean  # bool
box
bytea
varchar  # [ (n) ]
cidr
circle
date
double  # precision float8
inet
integer  # int, int4
interval  # [ fields ] [ (p) ]
json
jsonb
line
lseg
macaddr
macaddr8
money
numeric  # [ (p, s) ] 	decimal [ (p, s) ]
path
pg_lsn
point
polygon
real  # float4
smallint  # int2
smallserial  # serial2
serial  # serial4
text
time
timetz
timestamp
timestamptz
tsquery
tsvector
txid_snapshot
uuid
xml
'''
