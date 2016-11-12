# -*- coding: utf-8 -*-

# noinspection PyUnresolvedReferences
from behave import *

from features.sentence import assert_sentences
from features.sentence.api import request_sentence_with
from features.steps import *
from krump.support.collections import pluck


@given("these sentences exist")
def these_sentences_exist(context):
    context.sentence_repository.add_all(context.table)


@then("these sentences are returned")
def these_sentences_are_returned(context):
    assert_status_code_ok(context.response)
    assert_sentences(map(pluck('sentence'), context.table), context.response)


@given("no sentences exist")
def no_sentences_exist(context):
    context.sentence_repository.purge()


@then("no sentences are returned")
def no_sentences_are_returned(context):
    assert_status_code_no_content(context.response)


@when("we request sentences")
def request_sentences(context):
    request = context.request_for_sentences
    context.response = context.sentence_api.get_sentences(
        request['feature'],
        count=request['count'],
        max_words=request['max_words'])


def request_for_sentences(context, **kwargs):
    context.request_for_sentences = request_sentence_with(
        context.request_for_sentences, **kwargs)


@step("we want (?P<count>\d+?) sentences?")
def request_sentence_with_feature(context, count):
    request_for_sentences(context, count=count)


@step("we want a sentence with the '(?P<feature>.+?)' feature")
@step("we want sentences with the '(?P<feature>.+?)' feature")
def request_sentence_with_feature(context, feature):
    request_for_sentences(context, feature=feature)


@step("we want a sentence with a maximum of (?P<max_words>\d+?) words")
@step("we want sentences with a maximum of (?P<max_words>\d+?) words")
def request_sentence_with_max_words(context, max_words):
    request_for_sentences(context, max_words=max_words)
