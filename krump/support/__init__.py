# -*- coding: utf-8 -*-

from krump.support.strings import safe_string, has_text

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


class IdBased(object):
    """
    A mixin for classes that support an ID value.
    """

    # noinspection PyShadowingBuiltins,PyUnusedLocal
    def __init__(self, id=None, *args, **kwargs):
        self._id = id

    @property
    def id(self):
        """
        Return the persistent identity value.

        Will be L{None} if this instance is transient.
        """

        return self._id

    def is_persistent(self):
        """
        Is this instance persistent?

        An ID value that is not L{None} indicates persistence.

        @return: C{True} iff this class is persistent.
        """

        return self._id is not None

    def is_transient(self):
        """
        Is this instance transient?

        An ID value that is L{None} indicates transience.

        @return: C{True} iff this class is transient.
        """

        return not self.is_persistent()


class CodedError(IdBased):
    """
    An error that has both a code and a message.

    The code is useful in deriving localized error messages.

    The message is intended as a default description, to be used when there is
    no localised error message.
    """

    def __init__(self, code, message=None, **kwargs):
        super(CodedError, self).__init__(**kwargs)

        self.code = code
        self.message = safe_string(message)

    def __str__(self):
        return '{} [{}, "{}"]'.format(self.__class__.__name__, self.code,
                                      self.message)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.code == other.code and self.message == other.message
        else:
            return False

    def with_message(self, message):
        """
        Build a new C{CodedError} customised with the supplied C{message}.

        @param message: the message; can be C{None}.
        @return: a new C{CodedError}; never C{None}.
        """

        return CodedError(self.code, message=message)
