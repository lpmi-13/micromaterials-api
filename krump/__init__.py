# -*- coding: utf-8 -*-

import logging
from functools import wraps

from krump.support import factory
from krump.support.web import *
from krump.support.web.responsifiers import *

_logger = logging.getLogger(__name__)


def create_app(settings_override=None):
    app = factory.create_app(__name__, __path__, settings_override)
    initialise_web(app)
    return app


def route(blueprint, *args, **kwargs):
    kwargs['strict_slashes'] = kwargs.get('strict_slashes', False)

    def decorator(f):
        @blueprint.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*the_args, **the_kwargs):
            response_data = f(*the_args, **the_kwargs)
            return respond(response_data, *the_args, **the_kwargs)

        return wrapper

    return decorator


def initialise_web(app):
    responsifiers = dict(json=SimpleJsonResponsifier())
    app.responsifier = ContentNegotiatingResponsifier(responsifiers)
