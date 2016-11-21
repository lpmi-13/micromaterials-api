# -*- coding: utf-8 -*-
"""
Helper methods to keep the steps for sentences lean.
"""
import json

from hamcrest import *

from krump.support.collections import pluck


def assert_response(expected_sentences, response):
    response_data = data_from(response)

    assert_sentences(expected_sentences, response_data)


def assert_response_for_feature(expected_sentences, expected_feature, response):
    response_data = data_from(response)

    assert_that(response_data['feature'], equal_to(expected_feature))

    assert_sentences(expected_sentences, response_data)


# noinspection PyUnusedLocal
def assert_response_for_word(expected_sentences, expected_word, response):
    assert_sentences(expected_sentences, data_from(response))


def assert_sentences(expected_sentences, response_data):
    assert_that(actual_sentences_from(response_data), only_contains(*expected_sentences))


def actual_sentences_from(response_data):
    return map(pluck('sentence'), response_data['sentences'])


def data_from(response):
    return json.loads(response.data)
