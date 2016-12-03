# -*- coding: utf-8 -*-

from krump.support.strings import has_text

DEVELOPMENT = 'DEVELOPMENT'
PRODUCTION = 'PRODUCTION'
TEST = 'TEST'


def is_production(name):
    return PRODUCTION == name


def is_development(name):
    return DEVELOPMENT == name


def is_test(name):
    return TEST == name


def is_debug_mode(app):
    return app.config.get('DEBUG', False)


class KrumpException(Exception):
    """
    Base application exception class.
    """

    def __init__(self, message, cause=None):
        super(KrumpException, self).__init__()

        self.message = message
        self.cause = cause

    def __str__(self):
        return '{} "{}"'.format(self.__class__.__name__, self.message)
