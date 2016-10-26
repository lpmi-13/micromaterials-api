# -*- coding: utf-8 -*-

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
    return to_bounded_int(None, MAXIMUM_WORDS, raw_maximum_words)


def to_request_for_sentences(request, inclusion):
    return dict(
        inclusion=inclusion,
        count=to_count(request.args.get('count', DEFAULT_COUNT)),
        maximum_words=to_maximum_words(request.args.get('max-words', None))
    )
