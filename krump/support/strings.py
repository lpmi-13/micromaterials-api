# -*- coding: utf-8 -*-
"""
String-related utility methods.
"""

MODULE_SEPARATOR = '.'


def is_stringy(thing):
    return isinstance(thing, basestring)


def has_text(s):
    return s is not None and len(s.strip()) > 0


def safe_string(s, encoding='utf-8'):
    try:
        return ''.encode(encoding) if s is None else s.encode(encoding).strip()
    except LookupError:
        raise UnknownEncodingException.for_unknown_encoding(encoding)


class UnknownEncodingException(Exception):
    def __init__(self, message):
        self.message = message

    @staticmethod
    def for_unknown_encoding(name):
        """
        Thrown when an encoding cannot be looked up by name.

        @param name: the name of the unknown encoding.
        @return: an C{UnknownEncodingException}; never C{None}.
        """

        return UnknownEncodingException(
            'Cannot find encoding with name "{}".'.format(name))
