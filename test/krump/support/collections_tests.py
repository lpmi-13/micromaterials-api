# -*- coding: utf-8 -*-

import unittest

from hamcrest import *

from krump.support.collections import pluck, copy_and_update


class PluckTests(unittest.TestCase):
    def test_pluck_with_key_that_exists(self):
        self.assertEqual('Adam', pluck('name')(dict(name='Adam')))

    def test_pluck_with_key_that_does_not_exist(self):
        self.assertRaises(KeyError, lambda: pluck('name')(dict()))


# noinspection PyMethodMayBeStatic
class CopyAndUpdateTests(unittest.TestCase):
    def test_sunny_day_kwargs(self):
        source = dict(foo=3)
        result = copy_and_update(source, bar=3)
        assert_that(result, not_none())
        assert_that(result, has_key('foo'))
        assert_that(result, has_key('bar'))

    def test_sunny_day_overrides_correctly(self):
        source = dict(foo=3)
        expected_value = 4
        result = copy_and_update(source, foo=expected_value)
        assert_that(result, not_none())
        assert_that(result, has_key('foo'))
        self.assertEquals(expected_value, result['foo'])

    def test_sunny_day_dict(self):
        source = dict(foo=3)
        updates = dict(bar=3)
        result = copy_and_update(source, **updates)
        assert_that(result, not_none())
        assert_that(result, has_key('foo'))
        assert_that(result, has_key('bar'))

    def test_missing_source(self):
        assert_that(calling(copy_and_update).with_args(None), raises(AssertionError))

    def test_missing_updates(self):
        source = dict(foo=3)
        result = copy_and_update(source)
        assert_that(result, not_none())
        assert_that(result, has_key('foo'))
        assert_that(result, has_length(1))
