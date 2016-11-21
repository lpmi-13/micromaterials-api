# -*- coding: utf-8 -*-

PARAMETER_COUNT = 'count'
PARAMETER_MAXIMUM_WORDS = 'max-words'

DEFAULT_COUNT = 10
MAXIMUM_WORDS = 100
MAXIMUM_COUNT = 1000


def to_bounded_int(lower_bound, upper_bound, raw_value):
    # noinspection PyBroadException
    try:
        value = int(raw_value)
        if value <= 0:
            value = lower_bound
        elif value > upper_bound:
            value = upper_bound
    except:
        value = lower_bound
    return value


def to_count(raw_count):
    return to_bounded_int(DEFAULT_COUNT, MAXIMUM_COUNT, raw_count)


def to_maximum_words(raw_maximum_words):
    return None if raw_maximum_words is None else to_bounded_int(None, MAXIMUM_WORDS, raw_maximum_words)


def to_request_for_sentences(request, **kwargs):
    return dict(
        kwargs,
        count=to_count(request.args.get(PARAMETER_COUNT, DEFAULT_COUNT)),
        maximum_words=to_maximum_words(request.args.get(PARAMETER_MAXIMUM_WORDS, None)))
