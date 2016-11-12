# -*- coding: utf-8 -*-

import unittest

from flask import Request

from krump.sentence.to_request import to_request_for_sentences as to_request


def stub_request(query_parameters=''):
    return Request({'QUERY_STRING': query_parameters})


class ToRequestForSentencesTests(unittest.TestCase):
    def test_to_request_with_just_feature(self):
        actual_request = to_request(stub_request(), 'modal')
        expected_request = dict(
            count=10,
            maximum_words=None,
            feature='modal'
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_with_feature_and_count(self):
        actual_request = to_request(stub_request('count=2'), 'modal')
        expected_request = dict(
            count=2,
            maximum_words=None,
            feature='modal'
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_with_feature_and_maximum_words(self):
        actual_request = to_request(stub_request('max-words=2'), 'modal')
        expected_request = dict(
            count=10,
            maximum_words=2,
            feature='modal'
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_with_feature_and_count_and_maximum_words(self):
        actual_request = to_request(stub_request('count=33&max-words=2'), 'modal')
        expected_request = dict(
            count=33,
            maximum_words=2,
            feature='modal'
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_imposes_maximum_on_count(self):
        actual_request = to_request(stub_request('count=123456'), 'modal')
        expected_request = dict(
            count=1000,
            maximum_words=None,
            feature='modal'
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_imposes_maximum_on_maximum_words(self):
        actual_request = to_request(stub_request('max-words=123456'), 'modal')
        expected_request = dict(
            count=10,
            maximum_words=100,
            feature='modal'
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_imposes_lower_bound_when_count_is_zero(self):
        actual_request = to_request(stub_request('count=0'), 'modal')
        expected_request = dict(
            count=10,
            maximum_words=None,
            feature='modal'
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_imposes_lower_bound_when_maximum_words_is_zero(self):
        actual_request = to_request(stub_request('max-words=0'), 'modal')
        expected_request = dict(
            count=10,
            maximum_words=None,
            feature='modal'
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_imposes_lower_bound_when_count_is_negative(self):
        actual_request = to_request(stub_request('count=-6534'), 'modal')
        expected_request = dict(
            count=10,
            maximum_words=None,
            feature='modal'
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_imposes_lower_bound_when_maximum_words_is_negative(self):
        actual_request = to_request(stub_request('max-words=-68'), 'modal')
        expected_request = dict(
            count=10,
            maximum_words=None,
            feature='modal'
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_imposes_default_when_count_is_malformed(self):
        actual_request = to_request(stub_request('count=Sixteen%20Horsepower'), 'modal')
        expected_request = dict(
            count=10,
            maximum_words=None,
            feature='modal'
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_imposes_default_when_maximum_words_is_malformed(self):
        actual_request = to_request(stub_request('max-words=Tosh'), 'modal')
        expected_request = dict(
            count=10,
            maximum_words=None,
            feature='modal'
        )
        self.assertDictEqual(expected_request, actual_request)
