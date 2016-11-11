# -*- coding: utf-8 -*-

from flask import current_app

from krump import required_value


def get_sentences(request):
    query = {}

    maximum_words = request.get('maximum_words', None)
    if maximum_words is not None:
        query['$where'] = 'this.words.length <= {}'.format(maximum_words)

    return list(map(pluck('sentence'), sentences().find(query).limit(request['count'])))


def pluck(field):
    return lambda s: s[field]


def sentences():
    db_name = required_value(current_app.config, 'MONGO_DB')
    collection_name = required_value(current_app.config, 'MONGO_COLLECTION_SENTENCES')

    db = current_app.mongo_client[db_name]
    return db[collection_name]
