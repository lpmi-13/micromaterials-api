# -*- coding: utf-8 -*-
"""
Collections-related utility methods.
"""


def has_elements(l):
    return l is not None and len(l) > 0


def pluck(field):
    return lambda s: s[field]
