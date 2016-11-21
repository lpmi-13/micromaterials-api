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


def assert_sentences(expected_sentences, response_data):
    actual_sentences = map(pluck('sentence'), response_data['sentences'])
    assert_that(actual_sentences, only_contains(*expected_sentences))


def data_from(response):
    return json.loads(response.data)
