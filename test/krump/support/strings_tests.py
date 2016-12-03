# -*- coding: utf-8 -*-

import unittest

from krump.support.strings import is_stringy, has_text


class StringsTests(unittest.TestCase):
    def test_is_stringy_with_string(self):
        self.assertTrue(is_stringy(''))

    def test_is_stringy_with_unicode(self):
        self.assertTrue(is_stringy(u''))

    def test_is_stringy_with_none(self):
        self.assertFalse(is_stringy(None))

    def test_is_stringy_with_other_object(self):
        self.assertFalse(is_stringy([]))

    def test_has_text_with_none(self):
        self.assertFalse(has_text(None))

    def test_has_text_with_empty_string(self):
        self.assertFalse(has_text(''))

    def test_has_text_with_empty_unicode_string(self):
        self.assertFalse(has_text(u''))

    def test_has_text_with_unicode_string_filled_with_just_whitespace(self):
        self.assertFalse(has_text(u'    '))

    def test_has_text_with_string_filled_with_just_whitespace(self):
        self.assertFalse(has_text('\t    '))

    def test_has_text_with_not_empty_string(self):
        self.assertTrue(has_text('a'))

    def test_has_text_with_not_empty_unicode_string(self):
        self.assertTrue(has_text(u'a   '))
        self.assertTrue(has_text('a'))
