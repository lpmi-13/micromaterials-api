# -*- coding: utf-8 -*-
"""
Helper methods to keep the steps for sentences lean.
"""
import json

from hamcrest import *


def assert_sentences(expected_sentences, response):
    actual_sentences = json.loads(response.data)['sentences']
    assert_that(actual_sentences, only_contains(*expected_sentences))
