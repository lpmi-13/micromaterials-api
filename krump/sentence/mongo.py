# -*- coding: utf-8 -*-

import logging

from flask import current_app

from krump import required_value

PROJECT = 1
DO_NOT_PROJECT = 0

_logger = logging.getLogger(__name__)


def get_sentences_with_feature(request):
    query = to_query_for_feature(request)
    return _get_sentences(request, query)


def get_sentences_containing_word(request):
    query = to_query_for_word(request)
    return _get_sentences(request, query)


def to_query_for_feature(request):
    return _to_query(request, {'features': request['feature']})


def to_query_for_word(request):
    if request.get('pos', None) is None:
        query = {'words.original': request['word']}
    else:
        query = {
            'words': {
                '$elemMatch': {
                    'pos': request['pos'],
                    'original': request['word']
                }
            }
        }
    return _to_query(request, query)


def _to_query(request, other):
    query = dict(other)

    maximum_words = request.get('maximum_words', None)
    if maximum_words is not None:
        query['$where'] = 'this.words.length <= {}'.format(maximum_words)

    _logger.debug('Request is [%s], MongoDB query is [%s].', request, query)
    return query


def _get_sentences(request, query):
    _logger.debug('Getting sentences for [%s].', request)

    projections = dict(sentence=PROJECT,
                       words=PROJECT,
                       _id=DO_NOT_PROJECT
                       # add further fields such as POStags to project them
                       )
    sentences = sentences_collection() \
        .find(query, projections) \
        .limit(request['count'])

    return list(sentences)


def sentences_collection():
    db_name = required_value(current_app.config, 'MONGO_DB')
    collection_name = required_value(current_app.config, 'MONGO_COLLECTION_SENTENCES')

    db = current_app.mongo_client[db_name]
    return db[collection_name]
