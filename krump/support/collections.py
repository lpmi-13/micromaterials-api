# -*- coding: utf-8 -*-
"""
Collections-related utility methods.
"""


def has_elements(l):
    return l is not None and len(l) > 0


def pluck(field):
    return lambda s: s[field]


def copy_and_update(source, **updates):
    assert source is not None, 'The source is required.'

    result = source.copy()
    if updates:
        result.update(updates)
    return result
