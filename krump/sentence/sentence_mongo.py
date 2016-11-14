# -*- coding: utf-8 -*-
import logging

from flask import current_app

from krump import required_value
from krump.support.collections import pluck

FIELDS_TO_PROJECT = dict(sentence=1, _id=0)

_logger = logging.getLogger(__name__)


def get_sentences(request):
    _logger.debug('Getting sentences for [%s].', request)
    return map(pluck('sentence'), sentences()
               .find(to_query(request), FIELDS_TO_PROJECT)
               .limit(request['count']))


def to_query(request):
    query = {'features': request['feature']}

    maximum_words = request.get('maximum_words', None)
    if maximum_words is not None:
        query['$where'] = 'this.words.length <= {}'.format(maximum_words)

    _logger.debug('Request is [%s], MongoDB query is [%s].', request, query )
    return query


def sentences():
    db_name = required_value(current_app.config, 'MONGO_DB')
    collection_name = required_value(current_app.config, 'MONGO_COLLECTION_SENTENCES')

    db = current_app.mongo_client[db_name]
    return db[collection_name]
