# -*- coding: utf-8 -*-

# noinspection PyUnresolvedReferences
from behave import *

from cukes.sentence import *
from cukes.sentence.api import request_sentence_with
from cukes.steps import *
from krump.support.collections import pluck


@given("these sentences exist")
def these_sentences_exist(context):
    context.sentence_repository.add_all(context.table)


@then("these sentences are returned")
def these_sentences_are_returned(context):
    assert_status_code_ok(context.response)
    assert_response(map(pluck('sentence'), context.table), context.response)


@then("these sentences are returned for the '(?P<feature>.+?)' feature")
def these_sentences_are_returned(context, feature):
    assert_status_code_ok(context.response)
    assert_response_for_feature(map(pluck('sentence'), context.table), feature, context.response)


@given("no sentences exist")
def no_sentences_exist(context):
    context.sentence_repository.purge()


@then("no sentences are returned")
def no_sentences_are_returned(context):
    assert_status_code_no_content(context.response)


@when("we request sentences")
def request_sentences(context):
    context.response = context.sentence_api.get_sentences(context.request_for_sentences)


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


@step("we want a sentence containing the word '(?P<word>.+?)'")
@step("we want sentences containing the word '(?P<word>.+?)'")
def request_sentence_containing_word(context, word):
    request_for_sentences(context, word=word)


@step("we want sentences with the word '(?P<word>.+?)' as a '(?P<pos>.+?)'")
def request_sentence_containing_word_of_type(context, word, pos):
    request_for_sentences(context, word=word, pos=pos)
