# -*- coding: utf-8 -*-

import logging
from functools import wraps

from krump.support import factory
from krump.support.web import *
from krump.support.web.responsifiers import ContentNegotiatingResponsifier, \
    SimpleJsonResponsifier

STRICT_SLASHES = 'strict_slashes'

_logger = logging.getLogger(__name__)


def create_app(settings_override=None):
    app = factory.create_app(__name__, __path__, settings_override)
    app.responsifier = ContentNegotiatingResponsifier(
        dict(json=SimpleJsonResponsifier()))
    return app


def route(blueprint, *args, **kwargs):
    kwargs[STRICT_SLASHES] = kwargs.get(STRICT_SLASHES, False)

    def decorator(f):
        @blueprint.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*the_args, **the_kwargs):
            response_data = f(*the_args, **the_kwargs)
            return respond(response_data, *the_args, **the_kwargs)

        return wrapper

    return decorator


def required_value(config, key):
    value = config.get(key, None)
    if value is None:
        raise Exception('No value for [{}]; check your configuration.'.format(key))
    return value
