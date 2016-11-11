# -*- coding: utf-8 -*-

# noinspection PyUnresolvedReferences
from behave import *

from features.sentences import assert_sentences
from features.steps import *


@given("these sentences exist")
def these_sentences_exist(context):
    context.sentence_repository.add_all(context.table)


@when("we request sentences with the '(?P<feature>.+?)' feature")
def request_for_sentences(context, feature):
    context.response = context.sentence_api.get_sentences(feature)


@when("we request one sentence with the '(?P<feature>.+?)' feature")
def request_for_one_sentence(context, feature):
    context.response = context.sentence_api.get_sentences(feature, count=1)


@then("these sentences are returned")
def these_sentences_are_returned(context):
    assert_status_code_ok(context.response)
    assert_sentences(map(lambda row: row['sentence'], context.table), context.response)
