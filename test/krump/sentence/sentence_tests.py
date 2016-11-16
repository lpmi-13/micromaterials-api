# -*- coding: utf-8 -*-

import unittest

from krump.sentence.sentence import apostrophe_sentences


def stub_request(feature_name):
    return dict(
        count=10,
        maximum_words=None,
        feature=feature_name
    )


# TODO: make these tests pass
class SentencesWithApostrophesTests(unittest.TestCase):
    def test_apostrophe_sentences_with_empty_sentences(self):
        request = stub_request('apostrophe')

        input_sentences = []

        actual_sentences = apostrophe_sentences(request, input_sentences)

        expected_sentences = []

        self.assertEqual(expected_sentences, actual_sentences)

    def test_apostrophe_sentences_with_single_word(self):
        request = stub_request('apostrophe')

        input_sentences = [
            dict(sentence="Adam's house is made of grits.")
        ]

        actual_sentences = apostrophe_sentences(request, input_sentences)

        expected_sentences = [dict(
            sentence="Adam's house is made of grits.",
            features=["Adam's"]
        )]

        self.assertEqual(expected_sentences, actual_sentences)

    def test_apostrophe_sentences_with_two_words(self):
        # TODO: make this test pass

        request = stub_request('apostrophe')

        input_sentences = [
            dict(sentence="Adam's house is Laura's too.")
        ]

        actual_sentences = apostrophe_sentences(request, input_sentences)

        expected_sentences = [dict(
            sentence="Adam's house is Laura's too.",
            features=["Adam's", "Laura's"]
        )]

        self.assertEqual(expected_sentences, actual_sentences)
