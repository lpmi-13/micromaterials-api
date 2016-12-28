# -*- coding: utf-8 -*-

import logging
from functools import wraps

from krump.support import factory
from krump.support.web import *
from krump.support.web.filters import json_pretty
from krump.support.web.responsifiers import ContentNegotiatingResponsifier, \
    SimpleJsonResponsifier, TemplatedResponsifier
from support.web.resolvers import SimpleSuffixBasedViewResolver

STRICT_SLASHES = 'strict_slashes'

_logger = logging.getLogger(__name__)


def create_app(settings_override=None):
    app = factory.create_app(__name__, __path__, settings_override)
    initialise_web(app)
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


def initialise_web(app):
    html_responsifier = TemplatedResponsifier(SimpleSuffixBasedViewResolver())
    responsifiers = dict(html=html_responsifier, json=SimpleJsonResponsifier())
    app.responsifier = ContentNegotiatingResponsifier(responsifiers)

    app.jinja_env.filters['pretty'] = json_pretty
