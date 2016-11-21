# -*- coding: utf-8 -*-
"""
String-related utility methods.
"""

MODULE_SEPARATOR = '.'


def is_stringy(thing):
    return isinstance(thing, basestring)


def has_text(s):
    return s is not None and len(s.strip()) > 0
