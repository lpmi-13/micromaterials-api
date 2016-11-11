# -*- coding: utf-8 -*-

import unittest

from krump.support.collections import pluck


class PluckTests(unittest.TestCase):
    def test_pluck_with_key_that_exists(self):
        self.assertEqual('Adam', pluck('name')(dict(name='Adam')))

    def test_pluck_with_key_that_does_not_exist(self):
        self.assertRaises(KeyError, lambda: pluck('name')(dict()))
