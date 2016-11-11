# -*- coding: utf-8 -*-

from pymongo import MongoClient

from features.sentences import SentenceRepository, SentenceApi
from krump import create_app, required_value


# noinspection PyUnusedLocal
def before_feature(context, feature):
    app = create_app()
    app.testing = True

    setup_db(app, context)
    setup_api(app, context)


# noinspection PyUnusedLocal
def before_scenario(context, scenario):
    clean_db(context)


def clean_db(context):
    context.sentence_repository.purge()


def setup_api(app, context):
    context.sentence_api = SentenceApi(app.test_client())


def setup_db(app, context):
    mongo_client = create_mongo_client(app)
    app.mongo_client = mongo_client
    context.mongo_client = mongo_client
    context.sentence_repository = sentence_repository(app)


def create_mongo_client(app):
    url = required_value(app.config, 'MONGO_URL')
    connect_eagerly = app.config.get('MONGO_CONNECT_EAGERLY', True)
    return MongoClient(url, connect=connect_eagerly)


def sentence_repository(app):
    db_name = required_value(app.config, 'MONGO_DB')
    collection_name = required_value(app.config, 'MONGO_COLLECTION_SENTENCES')

    db = app.mongo_client[db_name]
    return SentenceRepository(db[collection_name])
