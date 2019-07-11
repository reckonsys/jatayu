from dataclasses import MISSING, Field as _Field


class Field(_Field):
    """A custom field definition."""

    def __init__(
            self, default=MISSING, default_factory=MISSING, init=True,
            repr=True, hash=None, compare=True, metadata=None):
        # It is an error to specify both default and default_factory.
        if default is not MISSING and default_factory is not MISSING:
            raise ValueError('cannot specify both default and default_factory')
        super(Field, self).__init__(
            default, default_factory, init, repr, hash, compare, metadata)
