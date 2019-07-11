# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""

from functools import partial
from rsutils.env import env, cast_bool

env = partial(env, prefix='CB_')


DEBUG = env('DEBUG', cast_to=cast_bool)
SECRET_KEY = env("SECRET_KEY")
