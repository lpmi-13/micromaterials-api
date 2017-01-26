# -*- coding: utf-8 -*-

import unittest

from flask import Request

from krump.sentence.to_request import to_request_for_sentences as to_request


def stub_request(query_parameters=''):
    return Request({'QUERY_STRING': query_parameters})


class ToRequestForSentencesTests(unittest.TestCase):
    def test_to_request_with_just_feature(self):
        actual_request = to_request(stub_request(), feature='modal')
        expected_request = dict(
            count=10,
            maximum_words=None,
            feature='modal',
            skip=0
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_with_just_word(self):
        actual_request = to_request(stub_request(), word='free')
        expected_request = dict(
            count=10,
            maximum_words=None,
            word='free',
            skip=0
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_with_feature_and_count(self):
        actual_request = to_request(stub_request('count=2'), feature='modal')
        expected_request = dict(
            count=2,
            maximum_words=None,
            feature='modal',
            skip=0
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_with_feature_and_maximum_words(self):
        actual_request = to_request(stub_request('max-words=2'), feature='modal')
        expected_request = dict(
            count=10,
            maximum_words=2,
            feature='modal',
            skip=0
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_with_feature_and_count_and_maximum_words(self):
        actual_request = to_request(stub_request('count=33&max-words=2'), feature='modal')
        expected_request = dict(
            count=33,
            maximum_words=2,
            feature='modal',
            skip=0
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_with_feature_and_count_and_maximum_words_and_skip(self):
        actual_request = to_request(stub_request('count=33&max-words=2&skip=2'), feature='modal')
        expected_request = dict(
            count=33,
            maximum_words=2,
            feature='modal',
            skip=2)

    def test_to_request_imposes_maximum_on_count(self):
        actual_request = to_request(stub_request('count=123456'), feature='modal')
        expected_request = dict(
            count=1000,
            maximum_words=None,
            feature='modal',
            skip=0
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_imposes_maximum_on_maximum_words(self):
        actual_request = to_request(stub_request('max-words=123456'), feature='modal')
        expected_request = dict(
            count=10,
            maximum_words=100,
            feature='modal',
            skip=0
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_imposes_lower_bound_when_count_is_zero(self):
        actual_request = to_request(stub_request('count=0'), feature='modal')
        expected_request = dict(
            count=10,
            maximum_words=None,
            feature='modal',
            skip=0
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_imposes_lower_bound_when_maximum_words_is_zero(self):
        actual_request = to_request(stub_request('max-words=0'), feature='modal')
        expected_request = dict(
            count=10,
            maximum_words=None,
            feature='modal',
            skip=0
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_imposes_lower_bound_when_skip_is_zero(self):
        actual_request = to_request(stub_request('skip=0'), feature='modal')
        expected_request = dict(
            count=10,
            maximum_words=None,
            feature='modal',
            skip=0)

    def test_to_request_imposes_lower_bound_when_count_is_negative(self):
        actual_request = to_request(stub_request('count=-6534'), feature='modal')
        expected_request = dict(
            count=10,
            maximum_words=None,
            feature='modal',
            skip=0
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_imposes_lower_bound_when_maximum_words_is_negative(self):
        actual_request = to_request(stub_request('max-words=-68'), feature='modal')
        expected_request = dict(
            count=10,
            maximum_words=None,
            feature='modal',
            skip=0
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_imposes_lower_bound_when_skip_is_negative(self):
        actual_request = to_request(stub_request('skip=-6534'), feature='modal')
        expected_request = dict(
            count=10,
            maximum_words=None,
            feature='modal',
            skip=0)

    def test_to_request_imposes_default_when_count_is_malformed(self):
        actual_request = to_request(stub_request('count=Sixteen%20Horsepower'), feature='modal')
        expected_request = dict(
            count=10,
            maximum_words=None,
            feature='modal',
            skip=0
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_imposes_default_when_maximum_words_is_malformed(self):
        actual_request = to_request(stub_request('max-words=Tosh'), feature='modal')
        expected_request = dict(
            count=10,
            maximum_words=None,
            feature='modal',
            skip=0
        )
        self.assertDictEqual(expected_request, actual_request)

    def test_to_request_imposes_default_when_skip_is_malformed(self):
        actual_request = to_request(stub_request('skip=Tosh'), feature='modal')
        expected_request = dict(
            count=10,
            maximum_words=None,
            feature='modal',
            skip=0)