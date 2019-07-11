from dataclasses import MISSING, Field as _Field

'''Type Conversion.

https://magicstack.github.io/asyncpg/current/usage.html#type-conversion

anyarrar                       | list
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

    def __init__(
            self, default=MISSING, default_factory=MISSING, init=True,
            repr=True, hash=None, compare=True, pg_field='TEXT'):
        # It is an error to specify both default and default_factory.
        if default is not MISSING and default_factory is not MISSING:
            raise ValueError('cannot specify both default and default_factory')
        super(Field, self).__init__(
            default, default_factory, init, repr, hash, compare)


class CharField(Field):
    pass
