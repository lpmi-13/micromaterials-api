# -*- coding: utf-8 -*-

import unittest

from krump.support import IdBased, CodedError


class IdBasedTests(unittest.TestCase):
    def test_is_transient_from_the_off(self):
        obj = IdBased()

        self.assertTrue(obj.is_transient())
        self.assertFalse(obj.is_persistent())

    def test_is_persistent(self):
        obj = IdBased(id=12)

        self.assertFalse(obj.is_transient())
        self.assertTrue(obj.is_persistent())


class CodedErrorTests(unittest.TestCase):
    def test_equal_with_equal_instances(self):
        one = CodedError(1, message='one')
        one_ = CodedError(1, message='one')

        self.assertEqual(one, one_)

    def test_equal_with_same_instance(self):
        one = CodedError(1, message='one')

        self.assertEqual(one, one)

    def test_equal_with_unequal_instances(self):
        one = CodedError(1, message='one')
        two = CodedError(2, message='two')

        self.assertNotEqual(one, two)

    def test_equal_with_unequal_instances_of_differing_types(self):
        one = CodedError(1, message='one')
        two = 'ohilovearainynight'

        self.assertNotEqual(one, two)

    def test_equal_with_unequal_instances_of_none(self):
        one = CodedError(1, message='one')
        two = None

        self.assertNotEqual(one, two)
