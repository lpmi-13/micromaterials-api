# -*- coding: utf-8 -*-

from pymongo import MongoClient
from werkzeug.serving import run_simple

from krump import create_app, required_value

if __name__ == "__main__":
    application = create_app()

    url = required_value(application.config, 'MONGO_URL')
    connect_eagerly = application.config.get('MONGO_CONNECT_EAGERLY', True)

    application.mongo_client = MongoClient(url, connect=connect_eagerly)
    run_simple('0.0.0.0', 5000, application, use_reloader=True, use_debugger=True)
