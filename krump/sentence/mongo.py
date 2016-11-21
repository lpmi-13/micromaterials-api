# -*- coding: utf-8 -*-

import logging

from flask import current_app

from krump import required_value

_logger = logging.getLogger(__name__)


def get_sentences(request):
    _logger.debug('Getting sentences for [%s].', request)

    query = to_query(request)

    sentences = sentences_collection() \
        .find(query, dict(sentence=1, words=1, _id=0)) \
        .limit(request['count'])

    return list(sentences)


def to_query(request):
    query = {'features': request['feature']}

    maximum_words = request.get('maximum_words', None)
    if maximum_words is not None:
        query['$where'] = 'this.words.length <= {}'.format(maximum_words)

    _logger.debug('Request is [%s], MongoDB query is [%s].', request, query)
    return query


def sentences_collection():
    db_name = required_value(current_app.config, 'MONGO_DB')
    collection_name = required_value(current_app.config, 'MONGO_COLLECTION_SENTENCES')

    db = current_app.mongo_client[db_name]
    return db[collection_name]
